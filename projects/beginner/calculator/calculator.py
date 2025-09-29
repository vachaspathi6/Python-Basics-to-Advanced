"""
Title: Simple Calculator
Author: Python-Basics-to-Advanced
Difficulty: Beginner
Description: A basic calculator that performs arithmetic operations
"""


def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def get_number(prompt: str) -> float:
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operation() -> str:
    """Get a valid operation from user input."""
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in operations:
            return operation
        print("Invalid operation! Please enter +, -, *, or /")


def calculate(num1: float, operation: str, num2: float) -> float:
    """Perform the calculation based on the operation."""
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)


def main():
    """Main calculator function."""
    print("=== Simple Calculator ===")
    print("Welcome! This calculator performs basic arithmetic operations.")

    while True:
        try:
            # Get input from user
            num1 = get_number("Enter first number: ")
            operation = get_operation()
            num2 = get_number("Enter second number: ")

            # Perform calculation
            result = calculate(num1, operation, num2)

            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")

            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_calc != 'y':
                print("Thank you for using the calculator! Goodbye! 👋")
                break

            print("\n" + "="*40)

        except ValueError as e:
            print(f"Error: {e}")
            print("Let's try again!\n")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Let's try again!\n")


if __name__ == "__main__":
    main()
