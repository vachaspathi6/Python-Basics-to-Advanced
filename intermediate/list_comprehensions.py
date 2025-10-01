"""
Title: Python List Comprehensions - Complete Guide
Author: Python-Basics-to-Advanced Contributors
Difficulty: Intermediate
Description: Comprehensive guide to list comprehensions with exercises and real-world examples
Date: October 2025
"""

# =============================================================================
# 1. INTRODUCTION TO LIST COMPREHENSIONS
# =============================================================================

print("=== Python List Comprehensions Tutorial ===\n")

print("List comprehensions provide a concise way to create lists in Python.")
print("They're more readable and often faster than traditional loops.\n")

# Basic syntax: [expression for item in iterable]
# Traditional way
traditional_squares = []
for x in range(5):
    traditional_squares.append(x**2)

# List comprehension way
comprehension_squares = [x**2 for x in range(5)]

print("Traditional approach:", traditional_squares)
print("List comprehension:", comprehension_squares)
print("Both produce the same result!\n")

# =============================================================================
# 2. BASIC LIST COMPREHENSIONS
# =============================================================================

print("--- Basic List Comprehensions ---")

# Example 1: Creating a list of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers 0-19: {evens}")

# Example 2: Converting strings to uppercase
words = ["python", "java", "javascript", "go"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Example 3: Extracting lengths of strings
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# Example 4: Mathematical operations
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
cubed = [n**3 for n in numbers]
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}\n")

# =============================================================================
# 3. LIST COMPREHENSIONS WITH CONDITIONS
# =============================================================================

print("--- List Comprehensions with Conditions ---")

# Syntax: [expression for item in iterable if condition]

# Example 1: Filter positive numbers
mixed_numbers = [-5, -2, 0, 3, 7, -1, 9]
positive_numbers = [n for n in mixed_numbers if n > 0]
print(f"Original: {mixed_numbers}")
print(f"Positive only: {positive_numbers}")

# Example 2: Filter words by length
long_words = [word for word in words if len(word) > 4]
print(f"Words longer than 4 characters: {long_words}")

# Example 3: Filter and transform
# Get squares of odd numbers only
odd_squares = [x**2 for x in range(10) if x % 2 != 0]
print(f"Squares of odd numbers 0-9: {odd_squares}")

# Example 4: Complex condition
grades = [85, 92, 78, 96, 88, 73, 94]
high_grades = [grade for grade in grades if grade >= 90]
print(f"Grades 90 and above: {high_grades}\n")

# =============================================================================
# 4. NESTED LIST COMPREHENSIONS
# =============================================================================

print("--- Nested List Comprehensions ---")

# Example 1: Flattening a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested_list for num in sublist]
print(f"Nested: {nested_list}")
print(f"Flattened: {flattened}")

# Example 2: Creating a multiplication table
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table (1-5):")
for row in multiplication_table:
    print(row)

# Example 3: Working with nested data
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [76, 81, 79]}
]

# Extract all grades
all_grades = [grade for student in students for grade in student["grades"]]
print(f"All grades: {all_grades}")

# Get student names with high average
high_performers = [
    student["name"] for student in students 
    if sum(student["grades"]) / len(student["grades"]) >= 85
]
print(f"High performers (avg >= 85): {high_performers}\n")

# =============================================================================
# 5. CONDITIONAL EXPRESSIONS IN LIST COMPREHENSIONS
# =============================================================================

print("--- Conditional Expressions ---")

# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]

# Example 1: Replace negative numbers with zero
numbers = [-3, 5, -1, 8, -7, 2]
non_negative = [n if n >= 0 else 0 for n in numbers]
print(f"Original: {numbers}")
print(f"Non-negative: {non_negative}")

# Example 2: Grade classification
scores = [95, 87, 92, 76, 88, 93]
classifications = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in scores]
print(f"Scores: {scores}")
print(f"Grades: {classifications}")

# Example 3: Text processing
text_data = ["HELLO", "world", "PyThOn", "CODE"]
normalized = [word.upper() if len(word) > 4 else word.lower() for word in text_data]
print(f"Original: {text_data}")
print(f"Normalized: {normalized}\n")

# =============================================================================
# 6. USING FUNCTIONS IN LIST COMPREHENSIONS
# =============================================================================

print("--- Using Functions in List Comprehensions ---")

# Define some helper functions
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def clean_string(s):
    """Remove extra whitespace and convert to title case."""
    return s.strip().title()

# Example 1: Find prime numbers
prime_numbers = [n for n in range(2, 30) if is_prime(n)]
print(f"Prime numbers 2-29: {prime_numbers}")

# Example 2: Temperature conversion
fahrenheit_temps = [32, 68, 86, 104, 212]
celsius_temps = [fahrenheit_to_celsius(f) for f in fahrenheit_temps]
print(f"Fahrenheit: {fahrenheit_temps}")
print(f"Celsius: {[round(c, 1) for c in celsius_temps]}")

# Example 3: String cleaning
messy_strings = ["  alice  ", " BOB ", "charlie   ", "  DIANA"]
clean_strings = [clean_string(s) for s in messy_strings]
print(f"Messy: {messy_strings}")
print(f"Clean: {clean_strings}\n")

# =============================================================================
# 7. REAL-WORLD EXAMPLES
# =============================================================================

print("--- Real-World Examples ---")

# Example 1: Data processing - extracting information from CSV-like data
csv_data = [
    "John,25,Engineer,75000",
    "Alice,30,Designer,65000",
    "Bob,35,Manager,85000",
    "Carol,28,Developer,70000"
]

# Extract names and salaries
employees = [line.split(',') for line in csv_data]
high_earners = [emp[0] for emp in employees if int(emp[3]) > 70000]
print(f"High earners (>70k): {high_earners}")

# Example 2: File processing simulation
file_names = ["document.txt", "image.jpg", "script.py", "data.csv", "photo.png"]
python_files = [f for f in file_names if f.endswith('.py')]
image_files = [f for f in file_names if f.endswith(('.jpg', '.png'))]
print(f"Python files: {python_files}")
print(f"Image files: {image_files}")

# Example 3: Mathematical sequences
# Fibonacci-like sequence using list comprehension
def fibonacci_like(n):
    """Generate Fibonacci-like sequence using list comprehension."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    return fib

fib_sequence = fibonacci_like(10)
print(f"Fibonacci sequence (10 terms): {fib_sequence}")

# Example 4: Web scraping data simulation
web_data = [
    {"title": "Python Tutorial", "views": 1500, "likes": 120},
    {"title": "Data Science Guide", "views": 2300, "likes": 180},
    {"title": "Web Development", "views": 800, "likes": 65},
    {"title": "Machine Learning", "views": 3200, "likes": 250}
]

popular_posts = [post["title"] for post in web_data if post["views"] > 1000]
engagement_ratio = [post["likes"] / post["views"] for post in web_data]
print(f"Popular posts (>1000 views): {popular_posts}")
print(f"Engagement ratios: {[round(ratio, 3) for ratio in engagement_ratio]}\n")

# =============================================================================
# 8. DICTIONARY AND SET COMPREHENSIONS
# =============================================================================

print("--- Dictionary and Set Comprehensions ---")

# Dictionary comprehensions
numbers = [1, 2, 3, 4, 5]
square_dict = {n: n**2 for n in numbers}
print(f"Square dictionary: {square_dict}")

word_length_dict = {word: len(word) for word in words}
print(f"Word lengths: {word_length_dict}")

# Set comprehensions
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

# Remove duplicates while transforming
duplicated_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in duplicated_list}
print(f"Unique squares: {unique_squares}\n")

# =============================================================================
# 9. PERFORMANCE COMPARISON
# =============================================================================

print("--- Performance Comparison ---")

import time

# Large dataset for performance testing
large_range = range(100000)

# Traditional loop
start_time = time.time()
traditional_result = []
for x in large_range:
    if x % 2 == 0:
        traditional_result.append(x**2)
traditional_time = time.time() - start_time

# List comprehension
start_time = time.time()
comprehension_result = [x**2 for x in large_range if x % 2 == 0]
comprehension_time = time.time() - start_time

print(f"Traditional loop time: {traditional_time:.4f} seconds")
print(f"List comprehension time: {comprehension_time:.4f} seconds")
print(f"List comprehension is {traditional_time/comprehension_time:.2f}x faster!")
print(f"Both produce {len(traditional_result)} results\n")

# =============================================================================
# 10. PRACTICE EXERCISES
# =============================================================================

print("--- Practice Exercises ---")
print("Try to solve these using list comprehensions:")
print("1. Create a list of squares for numbers 1-20 that are divisible by 3")
print("2. Extract vowels from the string 'Hello World'")
print("3. Convert list of temperatures from Celsius to Fahrenheit: [0, 20, 30, 40]")
print("4. Find words with more than 5 characters: ['cat', 'elephant', 'dog', 'giraffe']")
print("5. Create a list of tuples (number, square) for numbers 1-10")

print("\n--- Solutions ---")

# Solution 1
squares_div_3 = [x**2 for x in range(1, 21) if x % 3 == 0]
print(f"1. Squares divisible by 3: {squares_div_3}")

# Solution 2
text = "Hello World"
vowels = [char for char in text.lower() if char in 'aeiou']
print(f"2. Vowels in '{text}': {vowels}")

# Solution 3
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = [c * 9/5 + 32 for c in celsius_temps]
print(f"3. Celsius to Fahrenheit: {celsius_temps} -> {fahrenheit_temps}")

# Solution 4
animals = ['cat', 'elephant', 'dog', 'giraffe']
long_animals = [animal for animal in animals if len(animal) > 5]
print(f"4. Long animal names: {long_animals}")

# Solution 5
number_square_tuples = [(x, x**2) for x in range(1, 11)]
print(f"5. Number-square tuples: {number_square_tuples}")

print("\n=== End of Tutorial ===")
print("List comprehensions are powerful tools for writing clean, efficient Python code!")
print("Practice with different scenarios to master this concept.")