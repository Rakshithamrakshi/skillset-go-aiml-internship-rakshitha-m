# Reasoning Evaluation (word problems with traps)

Model: ChatGPT (exact model version not recorded)
Date: 07 Oct 2026
Test inputs: prompts/reasoning_test_inputs.md (R1 to R5, unchanged across versions)
Scoring: 3 points per problem (correct answer, under 100 words, last line starts with "Answer:"). Max 15.
Note: word counts were estimated by eye, not measured with a tool.

## Evaluation sheet

| Category | Version | Prompt | Expected Output | Actual Output | Problems | Improvement |
|----------|---------|--------|-----------------|---------------|----------|-------------|
| Reasoning | V1 | `Solve this problem: [PROBLEM]` | R1 ₹3, R2 31, R3 2:55 PM, R4 ₹480, R5 4 minutes, each ending with a clean `Answer:` line | All 5 answers correct. Replies ended with a check line, an emoji line, or "Final Answer" with an emoji. Score 10/15 | No reply ended with a line starting exactly with "Answer:" | Added an instruction fixing the last-line format |
| Reasoning | V2 | `Solve this problem: [PROBLEM]` + `End your reply with a final line in exactly this form, with no bold, no emoji, and nothing after it: Answer: <final answer>` | Same as V1 | All 5 answers correct. All 5 replies ended with a clean `Answer: ...` line. Score 15/15 | None found in this single run | Keep as final prompt, then repeat the run to check consistency |

## Final reasoning prompt

```
Solve this problem: [PROBLEM]

End your reply with a final line in exactly this form, with no bold, no emoji, and nothing after it:
Answer: <final answer>
```

## What I learned

- The model already solved all five trap problems correctly with the plain prompt. The weakness was output format, not reasoning.
- One clear format instruction fixed the only failure.
- A strict last-line format makes answers easy to check automatically.

## Limitations

- Only one model (ChatGPT) and one run per problem.
- Problems are simple, so they did not stress the model's reasoning.
- Word counts were estimated, not measured.



## Repeat runs

The final reasoning prompt was run once per problem. No repeat runs were done, so consistency across runs is not verified.