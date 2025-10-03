"""
Title: Python Functions Tutorial
Author: Python-Basics-to-Advanced Contributors
Difficulty: Beginner
Description: Comprehensive guide to defining and using functions in Python with examples
Date: October 2025
"""

# =============================================================================
# 1. DEFINING FUNCTIONS
# =============================================================================

print("=== Python Functions Tutorial ===\n")

def greet(name):
    """
    Greets a person by name.

    Args:
        name (str): The person's name.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

print(greet("Alice"))

# =============================================================================
# 2. FUNCTION PARAMETERS AND DEFAULTS
# =============================================================================

def power(base, exponent=2):
    """
    Calculates the power of a base number.

    Args:
        base (int or float): Base number.
        exponent (int or float): Exponent, default is 2.

    Returns:
        int or float: Result of base raised to exponent.
    """
    return base ** exponent

print(f"5^2 = {power(5)}")
print(f"3^3 = {power(3, 3)}")

# =============================================================================
# 3. RETURNING MULTIPLE VALUES
# =============================================================================

def arithmetic_ops(a, b):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        tuple: Sum, difference, product, and quotient.
    """
    sum_ = a + b
    diff = a - b
    prod = a * b
    quo = a / b if b != 0 else None
    return sum_, diff, prod, quo

s, d, p, q = arithmetic_ops(10, 5)
print(f"Sum: {s}, Difference: {d}, Product: {p}, Quotient: {q}")

# =============================================================================
# 4. LAMBDA (ANONYMOUS) FUNCTIONS
# =============================================================================

add = lambda x, y: x + y
square = lambda x: x * x

print(f"Add 3 + 4 = {add(3, 4)}")
print(f"Square of 6 = {square(6)}")

# =============================================================================
# 5. FUNCTION SCOPE AND LOCAL VARIABLES
# =============================================================================

def demonstrate_scope():
    x = 10  # local variable
    print(f"Inside function, x = {x}")

demonstrate_scope()
# print(x)  # This would raise an error because x is local

print("\n=== End of Functions Tutorial ===")
print("Practice tip: Try creating your own functions and experimenting with parameters and returns!")
