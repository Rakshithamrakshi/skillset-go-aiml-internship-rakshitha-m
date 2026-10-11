# Task 4.3 - Evaluation Questions (written before the runs)

Expected answers come from my own project files. Rows marked FILL are for me
to complete by searching the files in Task-4.1 knowledge_base (Ctrl + Shift + F).

| ID | Type | Question | Expected answer | Expected path |
|---|---|---|---|---|
| Q1 | Normal | What test accuracy did the CNN get? | About 91.6% (root README: 91.64%) | validate_input, retrieve, generate |
| Q2 | Multi-part | What were the spam classifier recall and precision, and how did the baseline compare? | Keras recall 0.86, precision 0.88; baseline recall 0.71, precision 0.99 | validate_input, retrieve, generate |
| Q3 | Multi-part | Which optimizer and batch size were used in the final hyperparameter configuration? | Adam, batch size 32 (learning rate 0.001, 30 epochs) | validate_input, retrieve, generate |
| Q4 | List | Which problems were found when auditing the Flask to-do app? | Debug mode on; list-position task ids; crash on wrong-type JSON; damaged file overwritten | validate_input, retrieve, generate |
| Q5 | Specific numbers | What did the final prompt versions score for reasoning and coding? | Reasoning 15/15, coding 22/22 | validate_input, retrieve, generate |
| Q6 | Out of scope | Who won the cricket world cup? | "I don't know based on the provided documents." | validate_input, retrieve, no_answer |
| Q7 | Near-miss | What accuracy did the CNN get on CIFAR-10? | A refusal (the CNN used Fashion-MNIST, not CIFAR-10) | validate_input, retrieve, generate |
| Q8 | Invalid | ab | Asks for at least 3 characters | validate_input, invalid_reply |
| Q9 | Missing info | What is the Offer Letter ID? | States that no ID value is provided (the field is blank in the documents), without making one up | validate_input, retrieve, generate (not predicted for sure) |
| Q10 | Ambiguous | How did it perform? | Should not pick one project and quote numbers as if the question were clear. A good answer says it is unclear what "it" refers to, or that it can't tell. | validate_input, retrieve, then generate or no_answer (not predicted) |
| Q11 | Specific number | What test loss did the 60-epoch run achieve? | 0.2807 (a little lower than the final configuration) | not predicted |
| Q12 | Count | How many controlled hyperparameter experiments were run? | 13 | not predicted |

## How each run will be judged (after reading the trace)
| Quality | Question I ask |
|---|---|
| Correctness | Does the answer match the expected answer? |
| Completeness | Are all parts of the question answered? |
| Groundedness | Is every claim in the answer supported by a retrieved chunk? |
| Failure type | None, retrieval failure (right chunk missing), or generation failure (right chunk present, wrong answer) |