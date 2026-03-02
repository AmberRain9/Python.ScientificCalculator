# simple_calculator.py
import math
import calculator

# Basic arithmetic
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Advanced operations
def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def power(x, y):
    return x ** y

def inverse(x):
    if x == 0:
        raise ZeroDivisionError("Cannot take inverse of zero")
    return 1 / x

def invert_sign(x):
    return -x