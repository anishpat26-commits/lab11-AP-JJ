# https://github.com/anishpat26-commits/lab10-AP-JJ.git
# Partner 1: Anish Patel
# Partner 2: James Jiang
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by 0")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be not be 1 or less than or equal to zero..")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than zero.")
    return math.log(b, a)

def log(a, b):
    if a <= 0:
        raise ValueError("Base cannot be nonpositive")
    elif a == 1:
        raise ValueError("Base cannot be 1")
    elif b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def exp(a, b):
    return a ** b


