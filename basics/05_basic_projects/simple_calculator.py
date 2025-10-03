"""
Title: Simple Calculator
Author: Python-Basics-to-Advanced
Difficulty: Beginner
Description: Basic calculator supporting +, -, *, / operations with input validation
"""

def calculator():
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print(f"Result: {a + b}")
    elif op == '-':
        print(f"Result: {a - b}")
    elif op == '*':
        print(f"Result: {a * b}")
    elif op == '/':
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print(f"Result: {a / b}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
