"""
Title: Python Control Structures Tutorial
Author: Python-Basics-to-Advanced Contributors
Difficulty: Beginner
Description: Detailed guide to if-else, loops, break, continue, and control flow in Python
Date: October 2025
"""

print("=== Python Control Structures Tutorial ===\n")

# =============================================================================
# 1. CONDITIONAL STATEMENTS
# =============================================================================

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# =============================================================================
# 2. FOR LOOP
# =============================================================================

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# =============================================================================
# 3. WHILE LOOP
# =============================================================================

print("\nCounting down from 5 to 1:")
count = 5
while count > 0:
    print(count)
    count -= 1

# =============================================================================
# 4. BREAK STATEMENT
# =============================================================================

print("\nFinding the first number divisible by 3 between 10 and 20:")
for num in range(10, 21):
    if num % 3 == 0:
        print(f"Found: {num}")
        break

# =============================================================================
# 5. CONTINUE STATEMENT
# =============================================================================

print("\nPrinting numbers between 1 and 10 skipping multiples of 3:")
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)

print("\n=== End of Control Structures Tutorial ===")
print("Practice tip: Modify the range and conditions to see different outputs and behaviors.")
