# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1855.1 ms**
- Average token reduction vs full source context: **14.5%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 4876.3 | 853 | 0.0% |  |
| G09 | semantic | PASS | 274.4 | 148 | 67.8% |  |
| G10 | semantic | PASS | 282.5 | 95 | 79.3% |  |
| G14 | mixed | PASS | 2979.7 | 431 | 0.0% |  |
| G03 | long_term | PASS | 1629.3 | 1329 | 0.0% |  |
| G04 | long_term | PASS | 1434.0 | 1323 | 0.0% |  |
| G07 | episodic | PASS | 289.6 | 564 | 0.0% |  |
| G08 | episodic | PASS | 311.9 | 578 | 0.0% |  |
| G11 | mixed | PASS | 1731.3 | 439 | 22.3% |  |
| G13 | mixed | PASS | 576.1 | 406 | 28.1% |  |
| G15 | mixed | PASS | 2543.2 | 736 | 0.0% |  |
| G16 | mixed | PASS | 1935.7 | 484 | 14.3% |  |
| G17 | mixed | PASS | 2441.4 | 484 | 14.3% |  |
| G18 | mixed | PASS | 3334.9 | 403 | 28.7% |  |
| G19 | mixed | PASS | 7622.7 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1432.6 | 1341 | 0.0% |  |
| G12 | mixed | PASS | 1660.6 | 431 | 31.8% |  |
| G20 | mixed | PASS | 1744.9 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`FACT: Lan Tran does not use Python for backend development. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lan Tran prioritizes using Java for development. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Da hieu uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes using Spring Boot for development. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran is managing the project LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: The Lab Assistant identifies 'Da hieu'. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Da hieu is related to LOTUS-88. [val`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> FACT: Lan Tran does not use Python for backend development. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Da hieu uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: The Lab Assistant identifies 'Da hieu'. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes using Java for development. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes using Spring Boot for development. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran is managing the project LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Da hieu is related to LO`

### G03 - long_term

`FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos like ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: When explaining code, Minh Nguyen prefers short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen dislikes Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen suggests setting concurrency to 20. `

### G04 - long_term

`FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen suggests setting concurrency to 20. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen must complete the benchmark report before Thursday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen `

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi EPISODE: Da ghi nha`

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook.`

### G11 - mixed

`<LONG_TERM> FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen reflects that the main issue is connection churn, not the timeout threshold. [valid_at=2026-08-03T10:03:00Z, invalid_at=2026-08-03T10:03:20Z] FACT: When explaining code, Minh Nguyen prefers short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_`

### G13 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playb`

### G15 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The async HTTP debugging failed despite the timeout being increased to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen asked for an explanation of async/await using a timeline if the topic comes up later. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen reflects that the main issue is connection churn, not the timeout`

### G16 - mixed

`<LONG_TERM> FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen believes that reusing aiohttp ClientSession is an effective approach. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Mi`

### G17 - mixed

`<LONG_TERM> FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Coroutine has priority over Task when explaining coroutine and Task. [valid_at=2026-08-01T09:02:20Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen believes that reusing aiohttp ClientSession is an effective approach. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT:`

### G18 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van `

### G19 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen believes that reusing aiohttp ClientSession is an effective approach. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen asked for an explanation of async/await using a timeline if the topic comes up later. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The async HTTP debugging failed despite the timeout being increased to 60s. [valid_at`

### G05 - long_term

`FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Python is not allowed for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos like ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The project BLUEBIRD-42 requires TypeScript for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [`

### G12 - mixed

`<LONG_TERM> FACT: The project BLUEBIRD-42 requires TypeScript for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The project BLUEBIRD-42 requires NestJS for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Python is not allowed for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FAC`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
