# Task 3.3: Prompt Engineering Portfolio

Week 3 of the Skill Set Go EduTech AI/ML internship.

## Goal

Design, test and improve LLM prompts for four categories: reasoning, extraction, summarization and coding. For each category I wrote the test inputs, the expected answers and the scoring rules **before** running anything, then improved the prompt one change at a time and scored every version the same way.

## Method

1. Fixed test inputs for each category (all invented, no personal data, nothing from the SMS dataset).
2. Expected answers and scoring rules written before the first run.
3. Version 1 is a plain baseline. Each later version changes exactly one thing.
4. A new chat for every run. Model: ChatGPT (exact model version not recorded). Date: 07 Oct 2026.
5. Real outputs saved in `results/`, scorecards added after each run.

## Results summary

| Category | V1 | V2 | V3 | Max | Final version |
|----------|----|----|----|-----|---------------|
| Reasoning (word problems with traps) | 10 | 15 | n/a | 15 | V2 |
| Extraction (order emails to JSON) | 25 | 29 | 30 | 30 | V3 |
| Summarization (300 words to 3 bullets) | 6 | 9 | 11 | 12 | V3 |
| Coding (function from a spec, 19 unit tests) | 19 | 22 | n/a | 22 | V2 |

## What I learned

- In most cases the plain prompt already gave correct content. The first failures were about **format** (no clean answer line, no JSON, no bullets, extra example code).
- Each added instruction fixed one specific, observed failure.
- Extraction showed a real content failure: "a green backpack" gave quantity null until I added a rule.
- A tight length limit made the summarizer drop one key point.
- Writing scoring rules first made the comparison between versions fair.

## Limitations

- One model (ChatGPT) and one run per input. Final prompts were not repeated, so consistency across runs is not verified.
- Small, invented test sets (5 problems, 5 emails, 3 texts, 3 functions).
- The Extraction V3 rule was written after seeing the E5 failure, so E5 is no longer an unseen test.
- Word counts (summaries) and the "under 100 words" checks (reasoning) were done by hand or by eye.
- The coding tests could not tell V1 from V2, because both passed all 19 tests.

## Folder structure

```
Task-3.3-Prompt-Engineering/
├── README.md
├── prompts/        fixed test inputs and expected answers (+ run_coding_tests.py)
├── results/        real outputs and scorecards for every run
├── evaluations/    one evaluation file per category + prompt_evaluation_sheet.md
└── screenshots/    evidence screenshots
```

## Key files

- `evaluations/prompt_evaluation_sheet.md`: combined sheet (Category, Version, Prompt, Expected Output, Actual Output, Problems, Improvement) and the final prompts
- `evaluations/reasoning_evaluation.md`, `extraction_evaluation.md`, `summarization_evaluation.md`, `coding_evaluation.md`
- `prompts/run_coding_tests.py`: the 19 unit tests I wrote for the coding category

## How to re-run the coding tests

From the repository root:

```
python Week-3\Task-3.3-Prompt-Engineering\prompts\run_coding_tests.py Week-3\Task-3.3-Prompt-Engineering\results\coding_v2_code.py
```