from __future__ import annotations

import json
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Student implementation for Lab 17 Multi-Memory Agent."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # 1) Prime the thread slice for context relevance
        prime_eval_thread(self.client, user_id, thread_id, query)
        
        # 2) Get user context block from Zep Thread
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # 3) Search facts/edges to ensure recency, deadlines, and open-loop items are captured
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        # Put fact_text first so specific query facts are never trimmed by the token budget
        return join_nonempty([fact_text, context_block], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # Search episodic trajectory/experience on the user graph
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # Search domain knowledge on standalone graph with scope="episodes" (fallback to "nodes")
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
            text = render_graph_search(results)
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
            text = render_graph_search(results)

        # Normalize JSON episodes to their concise summaries to avoid duplicate token consumption
        cleaned_chunks: list[str] = []
        seen: set[str] = set()
        for chunk in text.split("EPISODE: "):
            cleaned = chunk.replace("metadata=", "").strip()
            if not cleaned:
                continue
            if cleaned.startswith("{") and cleaned.endswith("}"):
                try:
                    data = json.loads(cleaned)
                    cleaned = data.get("summary") or cleaned
                except Exception:
                    pass
            if cleaned not in seen:
                seen.add(cleaned)
                cleaned_chunks.append(f"EPISODE: {cleaned}")

        return "\n".join(cleaned_chunks) if cleaned_chunks else text

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # Enforce 10/4/3/3 token budget and STM -> Long-term -> Episodic -> Semantic priority
        return self.budget.assemble(layers)
