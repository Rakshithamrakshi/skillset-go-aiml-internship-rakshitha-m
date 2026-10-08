# Coding Evaluation (write a function from a spec, tested with my own unit tests)

Model: ChatGPT (exact model version not recorded)
Date: 07 Oct 2026
Test inputs: prompts/coding_test_inputs.md (C1 to C3) and prompts/run_coding_tests.py (19 unit tests, unchanged across versions)
Scoring: 19 test points + 3 format points (one code block, no print/input per function). Max 22.

## Evaluation sheet

| Category | Version | Prompt | Expected Output | Actual Output | Problems | Improvement |
|----------|---------|--------|-----------------|---------------|----------|-------------|
| Coding | V1 | `Write a Python function for this spec: [SPEC]` | A correct function passing all unit tests, in one code block with no print/input | All 19 tests passed. Each reply added a second "Example" code block. Score 19/22 | Extra example block with print() or example calls in all 3 replies | Added an instruction: exactly one code block, only the function, no examples, print or input |
| Coding | V2 | V1 prompt + `Reply with exactly one Python code block containing only the function. Do not include examples, print() calls, input() calls, or any text outside the code block.` | Same as V1 | All 19 tests passed, one code block per reply. Score 22/22 | None found in this single run | Keep as final prompt |

## Final coding prompt

```
Write a Python function for this spec: [SPEC]

Reply with exactly one Python code block containing only the function. Do not include examples, print() calls, input() calls, or any text outside the code block.
```

## What I learned

- The plain prompt already produced correct code, so the weakness was the reply format, not correctness.
- Without an instruction, the model adds example code, which breaks a file if pasted directly.
- Running my own unit tests gave an objective pass/fail result instead of judging by eye.

## Limitations

- Only one model (ChatGPT) and one run per spec.
- Only 3 small functions. V1 and V2 both passed all 19 tests, so the tests could not tell the versions apart; only the format rule did.
- The tests were written by me and may miss edge cases (for example, non-integer input or very large lists).
- No repeat runs were done, so consistency across runs is not verified.