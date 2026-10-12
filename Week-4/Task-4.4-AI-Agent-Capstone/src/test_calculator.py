from calculator import calculate


def close(a, b):
    return abs(a - b) < 1e-9


good = [
    ("0.86 - 0.71", 0.15),
    ("95.5 - 91.6", 3.9),
    ("(0.86 + 0.71) / 2", 0.785),
    ("-3 + 5", 2),
    ("10 / 4", 2.5),
]
bad = [
    "", "   ", "5 / 0", "2 ** 3", "abs(-3)", "x + 1", "1 +",
    "__import__('os').system('echo hi')", "0.86 - ", "True + 1", 123, None,
]

failures = 0
for expr, expected in good:
    try:
        got = calculate(expr)
        ok = close(got, expected)
    except Exception as error:
        got, ok = f"error: {error}", False
    print("PASS" if ok else "FAIL", "|", expr, "->", got)
    failures += not ok

for expr in bad:
    try:
        got = calculate(expr)
        print("FAIL |", repr(expr), "-> accepted:", got)
        failures += 1
    except ValueError as error:
        print("PASS |", repr(expr), "-> rejected:", error)
    except Exception as error:
        print("FAIL |", repr(expr), "-> unexpected error:", error)
        failures += 1

print("\nFailures:", failures)