# Task 4.4 - Test Log

Expected results were written before the runs. "Actual" columns are filled
from my own terminal output.

| ID | Type | Question | Expected path | Expected answer | Actual path | Actual answer | Result |
|---|---|---|---|---|---|---|---|
| T1 | Normal | What test accuracy did the CNN get? | validate_input, retrieve, plan_calculation, generate | About 91.6% | validate_input, retrieve, plan_calculation, generate | About 91.6% | Pass |
| T2 | Retrieval | What were the spam classifier recall and precision for Keras and the baseline? | validate_input, retrieve, plan_calculation, generate | Keras 0.86/0.88; baseline 0.71/0.99 | validate_input, retrieve, plan_calculation, generate | Keras recall 0.86, precision 0.88; baseline recall 0.71, precision 0.99 | Pass |
| T3 | Tool use | By how many points did the Keras spam recall exceed the baseline recall? | ..., plan_calculation, calculate, generate | 0.15 (0.86 - 0.71) | ..., calculate, generate | 0.15, expression 0.86 - 0.71 | Pass on the number; unit wording unclear; baseline is the 4,136-train model (F6) |
| T4 | Multi-step | How many points higher was the CNN training accuracy than its test accuracy? | ..., calculate, generate | About 3.9 (files give approximate values) | ..., calculate, generate | 3.9 (expression 95.5 - 91.6), stated without "about" | Pass on the number; precision overstated |
| T5 | Ambiguous | How did it perform? | validate_input, retrieve, no_answer | A decline (decision pending) | validate_input, retrieve, no_answer | "I don't know..." (scores 1.479-1.497) | Pass as a safe decline; it does not ask what "it" means |
| T6 | Missing info | What is the Offer Letter ID? | validate_input, retrieve, no_answer | A decline | validate_input, retrieve, no_answer | "I don't know..." | Pass as a decline; the right chunk (rank 1, 1.414) is dropped by the 1.2 limit, as in Task 4.3 |
| T7 | Out of scope | Who won the cricket world cup? | validate_input, retrieve, no_answer | A decline | validate_input, retrieve, no_answer | "I don't know..." | Pass |
| T8 | Invalid | ab | validate_input, invalid_reply | Asks for 3+ characters | validate_input, invalid_reply | Asks for 3+ characters | Pass |
| T9 | Tool safety | What is 5 divided by 0 using the numbers in the docs? | not predicted | Does not crash | validate_input, retrieve, no_answer | "I don't know" | Stopped at the retrieval gate; the tool was not reached. Tool safety is covered by test_agent_branches.py (stand-in model) |
| T10 | Strictness | How much higher was the Keras spam F1 than the baseline F1, as a percentage of the baseline? | not predicted | About 5.55% (precise values); about 4.8% from the rounded 0.87 and 0.83 | After the fix: validate_input, retrieve, plan_calculation, calculate, generate. Before the fix: ..., calculate, cannot_verify | After: "approximately 5.55% higher" (expression (0.8726 - 0.8267) / 0.8267 * 100, result 5.552195) | Fail before the fix; Pass after on the arithmetic, but the baseline is not like-for-like (F6) |


## Failures and fixes

### F1 - T10 false decline (fixed)
- What happened: a percentage question ended at cannot_verify even though it is answerable.
- Why: the number check required every number in the expression to appear in the retrieved text, and 100 (needed for a percentage) never does. Error shown: numbers not found in the documents: [100].
- Fix: `number_check.py` now allows the constant 100 and nothing else; two new unit cases were added.
- Re-test: the same question now runs through calculate and generate, result 5.552195 (my own check: 5.552).
- Limitation remaining: any other constant (for example 2 for an average) is still blocked, and 100 is now allowed anywhere in an expression.

### F2 - T3 unit wording (not fixed)
- What happened: the Keras recall minus the baseline recall was reported as "0.15 points".
- Why: the recall values are fractions (0.86 and 0.71), so the gap is 15 percentage points. The model repeated "points" from the question. Cause not investigated further.
- Limitation remaining: yes.

### F3 - T6 Offer Letter ID (not fixed)
- What happened: a bare "I don't know".
- Why: the chunk with the blank Offer Letter ID ranked first but scored 1.414, above the 1.2 limit, so it was dropped before the model saw it (same finding as Task 4.3, Q9).
- Limitation remaining: yes.

### F4 - T4 approximate values (not fixed)
- What happened: the answer states 3.9 without "about", but the CNN file gives approximate values (~95.5 and ~91.6).
- Limitation remaining: yes.

### F5 - T5 ambiguous question (design decision pending)
- What happened: a safe decline that does not ask what "it" means.
- Limitation remaining: yes; a clarifying question would add complexity.

### F6 - Baseline choice in T3 and T10 (not fixed)
- What happened: both answers compared Keras with the TF-IDF model trained on 4,136 messages.
- Why: the spam file lists two TF-IDF baselines (4,136 and 3,515 train) and calls the 3,515 one the like-for-like comparison with Keras. My expected answers used the 4,136 row, because the root README does, and the system did the same.
- Numbers (my own arithmetic from the table, not tool runs): recall gap 0.153 vs 0.160; F1 gap 5.55% vs about 6.23%.
- Limitation remaining: yes. An answer should say which baseline it used.