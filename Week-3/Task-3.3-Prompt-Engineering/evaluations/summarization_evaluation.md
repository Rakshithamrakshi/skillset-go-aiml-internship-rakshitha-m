# Summarization Evaluation (about 300 words into 3 bullets)

Model: ChatGPT (exact model version not recorded)
Date: 07 Oct 2026
Test inputs: prompts/summarization_test_inputs.md (S1 to S3, unchanged across versions)
Scoring: 4 points per text (exactly 3 bullets, one sentence of at most 25 words each, key points covered, no wrong facts). Max 12.
Note: word counts were done by hand, not with a tool.

## Evaluation sheet

| Category | Version | Prompt | Expected Output | Actual Output | Problems | Improvement |
|----------|---------|--------|-----------------|---------------|----------|-------------|
| Summarization | V1 | `Summarize this text: [TEXT]` | Exactly 3 short bullets covering the key points, no extra text | Good content, but 1 to 3 paragraphs instead of bullets. Score 6/12 | No bullets; several sentences; S2 missed the station-removal rule | Asked for exactly 3 bullets and nothing else |
| Summarization | V2 | `Summarize this text in exactly 3 bullet points. Write only the 3 bullet points, with no title, introduction or closing line.` + text | Same as V1 | Exactly 3 bullets in all texts, no extra text. Score 9/12 | Bullets too long (about 26 to 33 words) and often joined two ideas with a semicolon | Added a one-sentence, 25-word limit |
| Summarization | V3 | V2 prompt + `Each bullet must be one sentence of at most 25 words.` | Same as V1 | Exactly 3 bullets, longest 21 words. Score 11/12 | S1 left out the possible Saturday opening next year | Keep as final prompt; limitation recorded |

## Final summarization prompt

```
Summarize this text in exactly 3 bullet points. Write only the 3 bullet points, with no title, introduction or closing line. Each bullet must be one sentence of at most 25 words.

Text:
[TEXT]
```

## What I learned

- The plain prompt gave a good summary in the wrong format. Each format rule (bullet count, then length) fixed one specific failure.
- A tight length limit makes the model drop details, so shorter summaries lose some key points.
- Rules written in advance made it possible to score each version the same way.

## Limitations

- Only one model (ChatGPT) and one run per text.
- Only 3 invented texts of about 300 words.
- Rule 3 was written loosely: S1 has only 5 key ideas, so the "at least 5" threshold was stricter for it than for the other texts.
- Word counts were done by hand.
- No repeat runs were done, so consistency across runs is not verified.