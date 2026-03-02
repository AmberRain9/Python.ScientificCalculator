# operations.py

from Errors import CalculatorError
import math

def add(current, value):
    return current + value

def subtract(current, value):
    return current - value

def multiply(current, value):
    return current * value

def divide(current, value):
    if value == 0:
        raise CalculatorError("Division by zero")
    return current / value

def square(current):
    return current ** 2

def square_root(current):
    if current < 0:
        raise CalculatorError("Square root of negative number")
    return math.sqrt(current)

def power(current, exponent):
    return current ** exponent

def inverse(current):
    if current == 0:
        raise CalculatorError("Inverse of zero")
    return 1 / current

def invert_sign(current):
    return -current 