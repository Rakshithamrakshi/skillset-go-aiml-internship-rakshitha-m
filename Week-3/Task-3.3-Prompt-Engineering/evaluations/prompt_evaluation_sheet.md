# Prompt Evaluation Sheet (Task 3.3)

Model: ChatGPT (exact model version not recorded)
Date: 07 Oct 2026
Method: fixed test inputs, expected answers and scoring rules written before running; one change per version; a new chat for every run; one run per input.
All test texts are invented. No personal data and nothing from the SMS dataset.

## Score summary

| Category | V1 | V2 | V3 | Max | Final version |
|----------|----|----|----|-----|---------------|
| Reasoning | 10 | 15 | n/a | 15 | V2 |
| Extraction | 25 | 29 | 30 | 30 | V3 |
| Summarization | 6 | 9 | 11 | 12 | V3 |
| Coding | 19 | 22 | n/a | 22 | V2 |

## Full evaluation sheet

| Category | Version | Prompt | Expected Output | Actual Output | Problems | Improvement |
|----------|---------|--------|-----------------|---------------|----------|-------------|
| Reasoning | V1 | `Solve this problem: [PROBLEM]` | R1 3, R2 31, R3 2:55 PM, R4 480, R5 4 minutes, each ending with a clean `Answer:` line | All 5 answers correct. No reply ended with a line starting with "Answer:". Score 10/15 | Last lines were a check line, an emoji line or "Final Answer" | Added a last-line format instruction |
| Reasoning | V2 | V1 prompt + `End your reply with a final line in exactly this form, with no bold, no emoji, and nothing after it: Answer: <final answer>` | Same as V1 | All 5 correct, all 5 ended with a clean `Answer:` line. Score 15/15 | None found in this single run | Kept as final prompt |
| Extraction | V1 | `Extract the order details from this email: [EMAIL]` | Fields order_id, customer_name, item, quantity, delivery_city; E3 order_id null; E5 quantity 1 | Field values correct, but replies were bullet lists with varying labels. Score 25/30 | No JSON; extra fields in E4 and E5; E3 said "Not provided" instead of null | Asked for JSON with exact keys and nothing else |
| Extraction | V2 | V1 prompt + `return only a JSON object with exactly these keys: order_id, customer_name, item, quantity, delivery_city. Do not write anything outside the JSON.` | Same as V1 | Clean JSON in all 5; 4 of 5 fully correct. Score 29/30 | E5: "a green backpack" gave quantity null instead of 1 | Added a rule for "a" or "an" |
| Extraction | V3 | V2 prompt + `If a quantity is written as "a" or "an", use 1.` | Same as V1 | All 5 correct, clean JSON. Score 30/30 | None found in this single run | Kept as final prompt |
| Summarization | V1 | `Summarize this text: [TEXT]` | Exactly 3 short bullets covering the key points, no extra text | Good content but 1 to 3 paragraphs. Score 6/12 | No bullets; several sentences; S2 missed the station-removal rule | Asked for exactly 3 bullets and nothing else |
| Summarization | V2 | `Summarize this text in exactly 3 bullet points. Write only the 3 bullet points, with no title, introduction or closing line.` | Same as V1 | Exactly 3 bullets in all texts. Score 9/12 | Bullets too long (about 26 to 33 words) | Added a one-sentence, 25-word limit |
| Summarization | V3 | V2 prompt + `Each bullet must be one sentence of at most 25 words.` | Same as V1 | Exactly 3 bullets, longest 21 words. Score 11/12 | S1 left out the possible Saturday opening next year | Kept as final prompt; limitation recorded |
| Coding | V1 | `Write a Python function for this spec: [SPEC]` | Correct function passing all 19 unit tests, one code block, no print/input | All 19 tests passed. Each reply added a second "Example" code block. Score 19/22 | Extra example block in all 3 replies | Added a one-code-block, no-examples instruction |
| Coding | V2 | V1 prompt + `Reply with exactly one Python code block containing only the function. Do not include examples, print() calls, input() calls, or any text outside the code block.` | Same as V1 | All 19 tests passed, one code block per reply. Score 22/22 | None found in this single run | Kept as final prompt |

## Final prompts

**Reasoning (V2)**
```
Solve this problem: [PROBLEM]

End your reply with a final line in exactly this form, with no bold, no emoji, and nothing after it:
Answer: <final answer>
```

**Extraction (V3)**
```
Extract the order details from this email and return only a JSON object with exactly these keys: order_id, customer_name, item, quantity, delivery_city. Do not write anything outside the JSON. If a quantity is written as "a" or "an", use 1.

Email:
[EMAIL]
```

**Summarization (V3)**
```
Summarize this text in exactly 3 bullet points. Write only the 3 bullet points, with no title, introduction or closing line. Each bullet must be one sentence of at most 25 words.

Text:
[TEXT]
```

**Coding (V2)**
```
Write a Python function for this spec: [SPEC]

Reply with exactly one Python code block containing only the function. Do not include examples, print() calls, input() calls, or any text outside the code block.
```

## Honest limitations

- One model (ChatGPT) and one run per input. The final prompts were not repeated, so consistency across runs is not verified.
- Small, invented test sets (5 problems, 5 emails, 3 texts, 3 functions).
- Most failures were format failures. The plain prompts already gave correct reasoning, extraction values and code.
- The Extraction V3 rule was written after seeing the E5 failure, so E5 is no longer an unseen test.
- Summarization word counts and the "Under 100 words" checks for Reasoning were done by hand or by eye, not with a tool.
- The coding tests could not tell V1 from V2, because both passed all 19 tests.