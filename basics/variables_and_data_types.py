"""
Title: Python Variables and Data Types Tutorial
Author: Python-Basics-to-Advanced Contributors
Difficulty: Beginner
Description: Comprehensive guide to Python variables and data types with practical examples
Date: October 2025
"""

# =============================================================================
# 1. VARIABLES IN PYTHON
# =============================================================================

print("=== Python Variables and Data Types Tutorial ===\n")

# Variables are containers for storing data
# In Python, you don't need to declare variable types explicitly
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}\n")

# =============================================================================
# 2. NUMERIC DATA TYPES
# =============================================================================

print("--- Numeric Data Types ---")

# Integers (int)
students_count = 30
temperature = -5
year = 2025

# Floating-point numbers (float)
pi = 3.14159
price = 99.99
gpa = 3.85

# Complex numbers (complex)
complex_num = 3 + 4j

print(f"Integer: {students_count} (type: {type(students_count).__name__})")
print(f"Float: {pi} (type: {type(pi).__name__})")
print(f"Complex: {complex_num} (type: {type(complex_num).__name__})\n")

# Numeric operations
a, b = 10, 3
print("Numeric Operations:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}\n")

# =============================================================================
# 3. STRING DATA TYPE
# =============================================================================

print("--- String Data Type ---")

# Different ways to create strings
single_quote = 'Hello, World!'
double_quote = "Python Programming"
triple_quote = """This is a 
multi-line
string"""

print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Triple quotes: {triple_quote}\n")

# String operations
text = "Python Programming"
print("String Operations:")
print(f"Original: {text}")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Substring: {text[0:6]}\n")

# String formatting
name = "Bob"
score = 95.5
print("String Formatting:")
print(f"F-string: Hello, {name}! Your score is {score}%")
print("Format method: Hello, {}! Your score is {:.1f}%".format(name, score))
print("Percent formatting: Hello, %s! Your score is %.1f%%" % (name, score))
print()

# =============================================================================
# 4. BOOLEAN DATA TYPE
# =============================================================================

print("--- Boolean Data Type ---")

# Boolean values
is_sunny = True
is_raining = False

print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")

# Boolean operations
print("\nBoolean Operations:")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# Comparison operations (return boolean)
x, y = 5, 10
print(f"\nComparisons:")
print(f"{x} > {y} = {x > y}")
print(f"{x} < {y} = {x < y}")
print(f"{x} == {y} = {x == y}")
print(f"{x} != {y} = {x != y}")
print(f"{x} >= {y} = {x >= y}")
print(f"{x} <= {y} = {x <= y}\n")

# =============================================================================
# 5. LIST DATA TYPE
# =============================================================================

print("--- List Data Type ---")

# Lists are ordered, mutable collections
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["Python", 3.14, True, 42]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")

# List operations
print("\nList Operations:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Length: {len(fruits)}")

fruits.append("mango")
print(f"After append: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

fruits.insert(1, "strawberry")
print(f"After insert: {fruits}\n")

# =============================================================================
# 6. TUPLE DATA TYPE
# =============================================================================

print("--- Tuple Data Type ---")

# Tuples are ordered, immutable collections
coordinates = (10, 20)
colors = ("red", "green", "blue")
person = ("John", 30, "Engineer")

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Person: {person}")

# Tuple operations
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Number of colors: {len(colors)}")

# Tuple unpacking
name, age, profession = person
print(f"Unpacked - Name: {name}, Age: {age}, Profession: {profession}\n")

# =============================================================================
# 7. DICTIONARY DATA TYPE
# =============================================================================

print("--- Dictionary Data Type ---")

# Dictionaries are unordered, mutable key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# Dictionary operations
student["email"] = "alice@email.com"
print(f"After adding email: {student}")

student["age"] = 21
print(f"After updating age: {student}")

del student["grade"]
print(f"After removing grade: {student}")

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}\n")

# =============================================================================
# 8. SET DATA TYPE
# =============================================================================

print("--- Set Data Type ---")

# Sets are unordered collections of unique elements
unique_numbers = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange", "apple"}  # duplicates removed

print(f"Unique numbers: {unique_numbers}")
print(f"Fruits set: {fruits_set}")  # Note: no duplicate "apple"

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}\n")

# =============================================================================
# 9. TYPE CHECKING AND CONVERSION
# =============================================================================

print("--- Type Checking and Conversion ---")

# Type checking
value = 42
print(f"Value: {value}")
print(f"Type: {type(value)}")
print(f"Is integer: {isinstance(value, int)}")
print(f"Is string: {isinstance(value, str)}")

# Type conversion
num_str = "123"
str_to_int = int(num_str)
str_to_float = float(num_str)

print(f"\nType Conversions:")
print(f"String '123' to int: {str_to_int} (type: {type(str_to_int).__name__})")
print(f"String '123' to float: {str_to_float} (type: {type(str_to_float).__name__})")

int_to_str = str(456)
float_to_int = int(3.14)
list_to_tuple = tuple([1, 2, 3])

print(f"Int 456 to string: '{int_to_str}' (type: {type(int_to_str).__name__})")
print(f"Float 3.14 to int: {float_to_int} (type: {type(float_to_int).__name__})")
print(f"List to tuple: {list_to_tuple} (type: {type(list_to_tuple).__name__})\n")

# =============================================================================
# 10. PRACTICAL EXAMPLES
# =============================================================================

print("--- Practical Examples ---")

# Example 1: Student grade calculator
print("Example 1: Student Grade Calculator")
student_name = "Emma"
math_score = 85
science_score = 92
english_score = 78

average_score = (math_score + science_score + english_score) / 3
grade = "A" if average_score >= 90 else "B" if average_score >= 80 else "C"

print(f"Student: {student_name}")
print(f"Average Score: {average_score:.1f}")
print(f"Grade: {grade}\n")

# Example 2: Shopping cart
print("Example 2: Shopping Cart")
cart = {
    "apples": {"price": 1.50, "quantity": 5},
    "bananas": {"price": 0.80, "quantity": 8},
    "oranges": {"price": 2.00, "quantity": 3}
}

total_cost = 0
for item, details in cart.items():
    item_total = details["price"] * details["quantity"]
    total_cost += item_total
    print(f"{item.title()}: ${details['price']:.2f} x {details['quantity']} = ${item_total:.2f}")

print(f"Total Cost: ${total_cost:.2f}\n")

# Example 3: Text analysis
print("Example 3: Text Analysis")
text = "Python is a powerful and versatile programming language"
words = text.split()
word_count = len(words)
char_count = len(text)
unique_words = set(word.lower() for word in words)

print(f"Text: {text}")
print(f"Word count: {word_count}")
print(f"Character count: {char_count}")
print(f"Unique words: {len(unique_words)}")
print(f"Words: {words}")

print("\n=== End of Tutorial ===")
print("Practice tip: Try modifying the values and see how the results change!")

# =============================================================================
# 11. SUMMARY TABLE OF PYTHON DATA TYPES
# =============================================================================

print("--- Summary of Python Data Types ---\n")

data_types_summary = [
    ("int", "Whole numbers (e.g., 5, -10, 2025)"),
    ("float", "Decimal numbers (e.g., 3.14, -2.5)"),
    ("complex", "Numbers with real and imaginary parts (e.g., 2 + 3j)"),
    ("str", "Sequence of characters (e.g., 'Hello')"),
    ("bool", "Boolean values True or False"),
    ("list", "Ordered, mutable collection (e.g., [1, 2, 3])"),
    ("tuple", "Ordered, immutable collection (e.g., (1, 2, 3))"),
    ("dict", "Key-value pairs (e.g., {'name': 'Alice', 'age': 25})"),
    ("set", "Unordered collection of unique elements (e.g., {1, 2, 3})"),
]

print(f"{'Data Type':<10} | Description")
print("-" * 50)
for dtype, desc in data_types_summary:
    print(f"{dtype:<10} | {desc}")

print("\n💡 Tip: Use the 'type()' function to check any variable’s data type!")
print("\n=== End of Extended Tutorial ===")
