
# calculator/operation.py
# This module contains basic arithmetic operations for the command line calculator.

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y    

def divide(x, y):
    """Return the quotient of x and y. Raises ZeroDivisionError if y is zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y