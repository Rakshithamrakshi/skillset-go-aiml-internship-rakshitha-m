from number_check import unsupported_numbers

TEXT = (
    "Keras recall 0.86 and precision 0.88. Baseline recall 0.71 and precision 0.99. "
    "Test accuracy: ~91.6% and train accuracy ~95.5%. "
    "The dataset has 5,574 messages (4,827 ham, 747 spam)."
)

# (expression, text, expected list of unsupported numbers)
cases = [
    ("0.86 - 0.71", TEXT, []),
    ("95.5 - 91.6", TEXT, []),
    ("0.86 - 0.70", TEXT, [0.7]),
    ("0.86 - 0.71 + 5", TEXT, [5]),
    ("5574 - 4827", TEXT, []),
    ("0.860 - 0.71", TEXT, []),
    ("(0.86 + 0.71) / 2", TEXT, [2]),
    ("-3 + 5", "no numbers here", [3, 5]),
    ("0.86 - 0.71", "", [0.86, 0.71]),
    ("(0.86 - 0.71) / 0.71 * 100", TEXT, []),
    ("0.86 * 1000", TEXT, [1000]),
]

failures = 0
for expression, text, expected in cases:
    got = unsupported_numbers(expression, text)
    ok = sorted(got) == sorted(expected)
    print("PASS" if ok else "FAIL", "|", expression, "-> unsupported:", got, "| expected:", expected)
    failures += not ok

try:
    unsupported_numbers("1 +", TEXT)
    print("FAIL | '1 +' was accepted")
    failures += 1
except ValueError as error:
    print("PASS | '1 +' -> rejected:", error)

print("\nFailures:", failures)