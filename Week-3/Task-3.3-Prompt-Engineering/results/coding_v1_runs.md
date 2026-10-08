# Coding V1 Runs

Model: ChatGPT
Date: 07 Oct 2026
Prompt used: Write a Python function for this spec: [SPEC]

## C1
Full reply:
```python
def second_largest(numbers):
    unique = list(set(numbers))

    if len(unique) < 2:
        return None

    unique.sort(reverse=True)
    return unique[1]
```

**Example:**

```python
print(second_largest([10, 5, 8, 10, 3]))
# 8

print(second_largest([7, 7, 7]))
# None
```



## C2
Full reply:
```python
def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
```

Examples:

```python
print(is_palindrome("Madam"))                 # True
print(is_palindrome("A man, a plan, a canal")) # True
print(is_palindrome("Hello"))                 # False
print(is_palindrome(""))                      # True
print(is_palindrome("!!!"))                   # True
```


## C3
Full reply:
```python
def format_duration(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"
```

Examples:

```python
format_duration(0)       # "0:00:00"
format_duration(3661)    # "1:01:01"
format_duration(90000)   # "25:00:00"
format_duration(-10)     # raises ValueError
```


## V1 Scorecard

Model: ChatGPT
Date: 07 Oct 2026
Test run: python run_coding_tests.py coding_v1_code.py (output seen in terminal: TOTAL 19/19)

| ID | Tests passed | Format rule (one code block, no print/input) | Score |
|----|--------------|-----------------------------------------------|-------|
| C1 | 6/6 | N (second block with print calls) | 6/7 |
| C2 | 6/6 | N (second block with print calls) | 6/7 |
| C3 | 7/7 | N (second block with example calls) | 6/7 |

**V1 total score: 19 / 22**

Problems found:
- All three functions passed every test.
- Every reply added an extra "Example" code block, which breaks the format rule.