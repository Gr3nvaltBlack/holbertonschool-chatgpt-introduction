#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a number using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Convert the first command-line argument to an integer and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)

