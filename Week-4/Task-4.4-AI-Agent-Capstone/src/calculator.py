import ast
import math
import operator

# The only operations the tool allows
ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
MAX_LENGTH = 100


def _eval(node):
    """Evaluate a parsed expression, accepting only numbers and + - * /."""
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPS:
        return ALLOWED_OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_eval(node.operand)
    raise ValueError("Only numbers and + - * / are allowed")


def calculate(expression):
    """Return the result of a simple arithmetic expression, or raise ValueError."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Expression must be non-empty text")
    if len(expression) > MAX_LENGTH:
        raise ValueError("Expression is too long")
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except SyntaxError:
        raise ValueError("Not a valid arithmetic expression")
    try:
        result = _eval(tree)
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    if not math.isfinite(result):
        raise ValueError("Result is not a finite number")
    return result