import ast
import re

NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")


def numbers_in_text(text):
    """All numbers that appear in the text, as floats. '5,574' counts as 5574."""
    cleaned = re.sub(r"(?<=\d),(?=\d{3})", "", text)
    return {float(match) for match in NUMBER_PATTERN.findall(cleaned)}


def numbers_in_expression(expression):
    """All numbers written in an arithmetic expression."""
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except SyntaxError:
        raise ValueError("Not a valid arithmetic expression")
    return [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ]


ALLOWED_CONSTANTS = {100.0}  # needed to turn a ratio into a percentage


def unsupported_numbers(expression, text):
    """Numbers used in the expression that do NOT appear in the text."""
    found = numbers_in_text(text) | ALLOWED_CONSTANTS
    return [n for n in numbers_in_expression(expression) if float(n) not in found]