# Coding Test Inputs (fixed for all prompt versions)

Category: Coding (write a function from a spec, tested with my own unit tests)
All specs are invented for this exercise. No personal data.

## Specs

**C1.** Function name: `second_largest`. Input: a list of numbers. Output: the second largest distinct value. If the list has fewer than 2 distinct values, return None.

**C2.** Function name: `is_palindrome`. Input: a string. Output: True if the string reads the same forwards and backwards, ignoring upper/lower case and every character that is not a letter or digit. An empty string, or one with no letters or digits, returns True.

**C3.** Function name: `format_duration`. Input: a whole number of seconds that is 0 or more. Output: a string in the form H:MM:SS. Hours are not limited to 2 digits (25 hours gives "25:00:00"). Minutes and seconds always have 2 digits. If the input is negative, raise ValueError.

## Tests (written BEFORE running any prompt)

The tests are in `prompts/run_coding_tests.py`: 6 tests for C1, 6 for C2, 7 for C3 (19 in total).

## Scoring criteria (written before running)

- Test points: 1 point per passed test, so 19 at most.
- Format rule: for each function, the reply is one Python code block using the exact function name and containing no print() or input() calls. 1 point each, so 3 at most.
- Maximum per full run: 22 points.

## Run log

- Model name: ChatGPT
- Date: 07 Oct 2026