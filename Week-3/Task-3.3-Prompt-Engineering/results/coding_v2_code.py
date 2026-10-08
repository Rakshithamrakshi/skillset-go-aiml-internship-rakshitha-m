def second_largest(numbers):
    distinct = set(numbers)
    if len(distinct) < 2:
        return None
    return sorted(distinct)[-2]


def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def format_duration(seconds):
    if seconds < 0:
        raise ValueError
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"