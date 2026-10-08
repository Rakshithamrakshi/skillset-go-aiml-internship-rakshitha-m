def second_largest(numbers):
    unique = list(set(numbers))

    if len(unique) < 2:
        return None

    unique.sort(reverse=True)
    return unique[1]


def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def format_duration(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"