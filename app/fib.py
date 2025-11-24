"""Fibonacci implementation (initially contains a deliberate bug)."""

def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-based).

    This implementation has an intentional bug: it returns the wrong
    value due to returning the wrong variable (off-by-one).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    # BUG: returning `b` gives fib(n+1) instead of fib(n)
    return b
