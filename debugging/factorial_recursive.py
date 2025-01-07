#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated. 
             The function assumes that n is a non-negative integer.

    Returns:
    int: The factorial of the given number n. If n is 0, the factorial is 1 by definition.
          For any other positive integer, it returns n * (n-1) * ... * 1.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Get the number from the command line argument and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)

