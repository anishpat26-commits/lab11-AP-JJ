# https://github.com/anishpat26-commits/lab10-AP-JJ.git
# Partner 1: Anish Patel
# Partner 2: James Jiang
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by 0")
    return b/a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be not be 1 or less than or equal to zero..")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than zero.")
    return math.log(b, a)

def exp(a, b):
    return a ** b


