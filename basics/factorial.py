#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
factorial.py
------------
This script calculates the factorial of a non-negative integer using a recursive function.

Usage:
    $ python factorial.py
    Enter a number: 5
    Factorial of 5 is 120

Author: Your Name
Python Version: 3.6+
"""

from typing import Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: factorial(0) = 1
    if n == 0:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


def main() -> None:
    """
    Main function to take user input and display the factorial result.
    """
    try:
        # Take user input
        number_str: str = input("Enter a number: ")
        number: int = int(number_str)

        # Compute factorial
        result: int = factorial(number)

        # Display the result
        print(f"Factorial of {number} is {result}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
