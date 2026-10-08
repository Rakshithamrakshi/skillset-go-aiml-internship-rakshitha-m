"""Runs fixed unit tests against a Python file containing the AI-written functions."""
import importlib.util
import sys

TESTS = [
    ("C1", "second_largest", [5, 3, 9, 1], 5),
    ("C1", "second_largest", [4, 4, 4], None),
    ("C1", "second_largest", [7, 7, 5], 5),
    ("C1", "second_largest", [-1, -5, -3], -3),
    ("C1", "second_largest", [], None),
    ("C1", "second_largest", [2], None),
    ("C2", "is_palindrome", "Madam", True),
    ("C2", "is_palindrome", "A man, a plan, a canal: Panama", True),
    ("C2", "is_palindrome", "hello", False),
    ("C2", "is_palindrome", "", True),
    ("C2", "is_palindrome", "No lemon, no melon", True),
    ("C2", "is_palindrome", "12321", True),
    ("C3", "format_duration", 0, "0:00:00"),
    ("C3", "format_duration", 59, "0:00:59"),
    ("C3", "format_duration", 3600, "1:00:00"),
    ("C3", "format_duration", 3661, "1:01:01"),
    ("C3", "format_duration", 86399, "23:59:59"),
    ("C3", "format_duration", 90000, "25:00:00"),
    ("C3", "format_duration", -1, ValueError),
]


def load_module(path):
    spec = importlib.util.spec_from_file_location("candidate", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if len(sys.argv) != 2:
        print("Usage: python run_coding_tests.py <path_to_code_file>")
        return
    module = load_module(sys.argv[1])
    totals = {}
    for case_id, func_name, argument, expected in TESTS:
        passed_total = totals.setdefault(case_id, [0, 0])
        passed_total[1] += 1
        try:
            func = getattr(module, func_name)
            if expected is ValueError:
                try:
                    func(argument)
                    ok = False
                except ValueError:
                    ok = True
            else:
                ok = func(argument) == expected
        except Exception as error:
            ok = False
            print(f"  error in {func_name}({argument!r}): {type(error).__name__}")
        if ok:
            passed_total[0] += 1
        print(f"{'PASS' if ok else 'FAIL'}  {case_id} {func_name}({argument!r})")
    print()
    for case_id, (passed, total) in totals.items():
        print(f"{case_id}: {passed}/{total}")
    print(f"TOTAL: {sum(p for p, _ in totals.values())}/{sum(t for _, t in totals.values())}")


main()