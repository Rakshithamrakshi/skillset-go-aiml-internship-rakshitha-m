# Coding V2 Runs

Model: ChatGPT
Date: 07 Oct 2026
Change from V1: added "Reply with exactly one Python code block containing only the function. Do not include examples, print() calls, input() calls, or any text outside the code block."

## C1
Full reply:
```python
def second_largest(numbers):
    distinct = set(numbers)
    if len(distinct) < 2:
        return None
    return sorted(distinct)[-2]
```


## C2
Full reply:
```python
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```


## C3
Full reply:
```python
def format_duration(seconds):
    if seconds < 0:
        raise ValueError
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"
```


## V2 Scorecard

Model: ChatGPT
Date: 07 Oct 2026
Test run: python run_coding_tests.py coding_v2_code.py (output seen in terminal: TOTAL 19/19)

| ID | Tests passed | Format rule (one code block, no print/input) | Score |
|----|--------------|-----------------------------------------------|-------|
| C1 | 6/6 | Y | 7/7 |
| C2 | 6/6 | Y | 7/7 |
| C3 | 7/7 | Y | 7/7 |

**V2 total score: 22 / 22**

Problems found: none in this single run.