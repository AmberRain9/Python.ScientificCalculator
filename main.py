# main.py
import math

# Basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Advanced operations
def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Error: Negative number"
    return math.sqrt(x)

def power(x, y):
    return x ** y

def inverse(x):
    if x == 0:
        return "Error: Cannot invert zero"
    return 1 / x

def invert_sign(x):
    return -x

# Interactive loop
def main():
    print("Simple Calculator")
    print("Available operations: add, sub, mul, div, square, sqrt, pow, inv, neg, q to quit\n")
    
    while True:
        op = input("Operation? ").strip().lower()
        if op == 'q':
            break
        
        if op in ['add', 'sub', 'mul', 'div', 'pow']:
            x = float(input("First number: "))
            y = float(input("Second number: "))
            if op == 'add':
                print("Result:", add(x, y))
            elif op == 'sub':
                print("Result:", subtract(x, y))
            elif op == 'mul':
                print("Result:", multiply(x, y))
            elif op == 'div':
                print("Result:", divide(x, y))
            elif op == 'pow':
                print("Result:", power(x, y))
        
        elif op in ['square', 'sqrt', 'inv', 'neg']:
            x = float(input("Number: "))
            if op == 'square':
                print("Result:", square(x))
            elif op == 'sqrt':
                print("Result:", square_root(x))
            elif op == 'inv':
                print("Result:", inverse(x))
            elif op == 'neg':
                print("Result:", invert_sign(x))
        else:
            print("Invalid operation. Try again.")

    print("Goodbye!")

if __name__ == '__main__':
    main()