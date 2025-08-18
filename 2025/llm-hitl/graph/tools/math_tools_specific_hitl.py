from langgraph.types import interrupt

def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    hitl_response= interrupt(
        f"About to run multiply of {a} and {b}, please confirm with [OK] to run"
    )
    if hitl_response.lower().strip() == 'ok' : return a * b
    else : return f"Human Response to {hitl_response}"

def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Divide a by b.

    Args:
        a: first int
        b: second int
    """
    return a / b

math_tools = [add, multiply, divide]