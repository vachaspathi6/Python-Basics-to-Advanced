"""
Title: Python Practice Exercises - Loops, Functions, and Data Structures
Author: Python-Basics-to-Advanced Contributors
Difficulty: Beginner to Intermediate
Description: Comprehensive collection of Python exercises with detailed solutions
Date: October 2025

This file contains practice exercises covering:
1. Basic loops and control structures
2. Functions and parameters
3. Lists and list operations
4. Dictionaries and sets
5. String manipulation
6. File operations
7. Object-oriented programming basics
"""

print("=== Python Practice Exercises ===\n")
print("Work through these exercises to strengthen your Python skills!")
print("Try to solve each problem before looking at the solution.\n")

# =============================================================================
# 1. LOOP EXERCISES
# =============================================================================

print("🔄 LOOP EXERCISES")
print("-" * 50)

# Exercise 1.1: Number Patterns
print("\nExercise 1.1: Print a right triangle pattern")
print("Expected output:")
print("*")
print("**")
print("***")
print("****")
print("*****")

print("\n💡 Solution 1.1:")
def print_triangle(height):
    """Print a right triangle pattern of given height."""
    for i in range(1, height + 1):
        print("*" * i)

print_triangle(5)

# Exercise 1.2: FizzBuzz
print("\n" + "="*50)
print("Exercise 1.2: FizzBuzz")
print("Print numbers 1-30, but:")
print("- Replace multiples of 3 with 'Fizz'")
print("- Replace multiples of 5 with 'Buzz'")
print("- Replace multiples of both with 'FizzBuzz'")

print("\n💡 Solution 1.2:")
def fizzbuzz(n):
    """Classic FizzBuzz implementation."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()  # New line at the end

fizzbuzz(30)

# Exercise 1.3: Sum of Even Numbers
print("\n" + "="*50)
print("Exercise 1.3: Calculate sum of even numbers from 1 to 100")

print("\n💡 Solution 1.3:")
def sum_even_numbers(limit):
    """Calculate sum of even numbers up to limit."""
    total = 0
    for i in range(2, limit + 1, 2):  # Start at 2, step by 2
        total += i
    return total

result = sum_even_numbers(100)
print(f"Sum of even numbers 1-100: {result}")

# Alternative solution using list comprehension
result_alt = sum(i for i in range(1, 101) if i % 2 == 0)
print(f"Alternative solution: {result_alt}")

# Exercise 1.4: Multiplication Table
print("\n" + "="*50)
print("Exercise 1.4: Create a multiplication table (5x5)")

print("\n💡 Solution 1.4:")
def multiplication_table(size):
    """Print a multiplication table."""
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    
    for i in range(1, size + 1):
        print(f"{i:2}: ", end="")
        for j in range(1, size + 1):
            print(f"{i*j:4}", end="")
        print()

multiplication_table(5)

# =============================================================================
# 2. FUNCTION EXERCISES
# =============================================================================

print("\n\n🔧 FUNCTION EXERCISES")
print("-" * 50)

# Exercise 2.1: Prime Number Checker
print("\nExercise 2.1: Create a function to check if a number is prime")

print("\n💡 Solution 2.1:")
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test the function
test_numbers = [2, 3, 4, 17, 25, 29, 100]
for num in test_numbers:
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")

# Exercise 2.2: Factorial Calculator
print("\n" + "="*50)
print("Exercise 2.2: Calculate factorial using recursion and iteration")

print("\n💡 Solution 2.2:")
def factorial_iterative(n):
    """Calculate factorial using iteration."""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test both implementations
for i in range(6):
    iter_result = factorial_iterative(i)
    rec_result = factorial_recursive(i)
    print(f"Factorial of {i}: Iterative={iter_result}, Recursive={rec_result}")

# Exercise 2.3: Password Validator
print("\n" + "="*50)
print("Exercise 2.3: Create a password validator function")
print("Requirements: At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char")

print("\n💡 Solution 2.3:")
def validate_password(password):
    """Validate password strength."""
    import string
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    missing = []
    if not has_upper:
        missing.append("uppercase letter")
    if not has_lower:
        missing.append("lowercase letter")
    if not has_digit:
        missing.append("digit")
    if not has_special:
        missing.append("special character")
    
    if missing:
        return False, f"Password missing: {', '.join(missing)}"
    
    return True, "Password is valid"

# Test passwords
test_passwords = ["weak", "StrongPass1!", "noUpPeR123!", "NOLOWER123!", "NoDigits!"]
for password in test_passwords:
    is_valid, message = validate_password(password)
    print(f"'{password}': {'✅' if is_valid else '❌'} {message}")

# Exercise 2.4: Text Statistics
print("\n" + "="*50)
print("Exercise 2.4: Create a function to analyze text statistics")

print("\n💡 Solution 2.4:")
def text_statistics(text):
    """Analyze text and return statistics."""
    import string
    
    # Basic counts
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Character frequency
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Most common character
    most_common_char = max(char_freq.items(), key=lambda x: x[1]) if char_freq else None
    
    return {
        'characters': char_count,
        'words': word_count,
        'sentences': sentence_count,
        'most_common_char': most_common_char,
        'char_frequency': char_freq
    }

sample_text = "Hello world! This is a sample text for analysis. How interesting!"
stats = text_statistics(sample_text)
print(f"Text: {sample_text}")
print(f"Characters: {stats['characters']}")
print(f"Words: {stats['words']}")
print(f"Sentences: {stats['sentences']}")
if stats['most_common_char']:
    char, count = stats['most_common_char']
    print(f"Most common character: '{char}' (appears {count} times)")

# =============================================================================
# 3. LIST EXERCISES
# =============================================================================

print("\n\n📋 LIST EXERCISES")
print("-" * 50)

# Exercise 3.1: List Operations
print("\nExercise 3.1: Implement various list operations")

print("\n💡 Solution 3.1:")
def list_operations_demo():
    """Demonstrate various list operations."""
    numbers = [1, 5, 3, 9, 2, 8, 4, 7, 6]
    print(f"Original list: {numbers}")
    
    # Find maximum and minimum
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    print(f"Sorted: {sorted_numbers}")
    
    # Reverse the list
    reversed_numbers = list(reversed(numbers))
    print(f"Reversed: {reversed_numbers}")
    
    # Find even and odd numbers
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    print(f"Even numbers: {evens}")
    print(f"Odd numbers: {odds}")
    
    # Calculate sum and average
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")

list_operations_demo()

# Exercise 3.2: Remove Duplicates
print("\n" + "="*50)
print("Exercise 3.2: Remove duplicates from a list while preserving order")

print("\n💡 Solution 3.2:")
def remove_duplicates(lst):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def remove_duplicates_dict(lst):
    """Alternative solution using dict.fromkeys() (Python 3.7+)."""
    return list(dict.fromkeys(lst))

test_list = [1, 2, 3, 2, 4, 3, 5, 1, 6]
print(f"Original: {test_list}")
print(f"Without duplicates (method 1): {remove_duplicates(test_list)}")
print(f"Without duplicates (method 2): {remove_duplicates_dict(test_list)}")

# Exercise 3.3: List Rotation
print("\n" + "="*50)
print("Exercise 3.3: Rotate a list to the left and right")

print("\n💡 Solution 3.3:")
def rotate_left(lst, n):
    """Rotate list to the left by n positions."""
    if not lst:
        return lst
    n = n % len(lst)  # Handle rotations larger than list size
    return lst[n:] + lst[:n]

def rotate_right(lst, n):
    """Rotate list to the right by n positions."""
    if not lst:
        return lst
    n = n % len(lst)  # Handle rotations larger than list size
    return lst[-n:] + lst[:-n]

original = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original: {original}")
print(f"Rotate left by 2: {rotate_left(original, 2)}")
print(f"Rotate right by 2: {rotate_right(original, 2)}")
print(f"Rotate left by 10: {rotate_left(original, 10)}")  # More than list size

# Exercise 3.4: Two Sum Problem
print("\n" + "="*50)
print("Exercise 3.4: Find two numbers in a list that sum to a target")

print("\n💡 Solution 3.4:")
def two_sum(nums, target):
    """Find two numbers that sum to target. Return their indices."""
    # Brute force approach - O(n²)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum_optimized(nums, target):
    """Optimized solution using hash map - O(n)."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

test_nums = [2, 7, 11, 15, 3, 6]
target = 9
print(f"Numbers: {test_nums}")
print(f"Target: {target}")
result1 = two_sum(test_nums, target)
result2 = two_sum_optimized(test_nums, target)
print(f"Brute force result: {result1}")
print(f"Optimized result: {result2}")
if result1:
    print(f"Numbers at indices: {test_nums[result1[0]]} + {test_nums[result1[1]]} = {target}")

# =============================================================================
# 4. DICTIONARY EXERCISES
# =============================================================================

print("\n\n📖 DICTIONARY EXERCISES")
print("-" * 50)

# Exercise 4.1: Word Frequency Counter
print("\nExercise 4.1: Count word frequency in a text")

print("\n💡 Solution 4.1:")
def word_frequency(text):
    """Count frequency of words in text."""
    import string
    
    # Clean the text
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    
    words = clean_text.split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def display_word_frequency(text, top_n=5):
    """Display top N most frequent words."""
    freq = word_frequency(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Text: {text}")
    print(f"Total unique words: {len(freq)}")
    print(f"Top {top_n} most frequent words:")
    for word, count in sorted_words[:top_n]:
        print(f"  '{word}': {count} times")

sample_text = "The quick brown fox jumps over the lazy dog. The dog was really lazy."
display_word_frequency(sample_text)

# Exercise 4.2: Student Grade Manager
print("\n" + "="*50)
print("Exercise 4.2: Manage student grades with dictionaries")

print("\n💡 Solution 4.2:")
class GradeManager:
    """Manage student grades using dictionaries."""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        """Add a new student."""
        if name not in self.students:
            self.students[name] = []
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists")
    
    def add_grade(self, name, grade):
        """Add a grade for a student."""
        if name in self.students:
            if 0 <= grade <= 100:
                self.students[name].append(grade)
                print(f"Added grade {grade} for {name}")
            else:
                print("Grade must be between 0 and 100")
        else:
            print(f"Student {name} not found")
    
    def get_average(self, name):
        """Calculate student's average grade."""
        if name in self.students and self.students[name]:
            return sum(self.students[name]) / len(self.students[name])
        return None
    
    def get_class_statistics(self):
        """Get class-wide statistics."""
        all_grades = []
        for grades in self.students.values():
            all_grades.extend(grades)
        
        if not all_grades:
            return None
        
        return {
            'total_students': len(self.students),
            'total_grades': len(all_grades),
            'class_average': sum(all_grades) / len(all_grades),
            'highest_grade': max(all_grades),
            'lowest_grade': min(all_grades)
        }
    
    def display_all_students(self):
        """Display all students and their grades."""
        for name, grades in self.students.items():
            if grades:
                avg = self.get_average(name)
                print(f"{name}: {grades} (Average: {avg:.1f})")
            else:
                print(f"{name}: No grades recorded")

# Demonstrate the grade manager
gm = GradeManager()
gm.add_student("Alice")
gm.add_student("Bob")
gm.add_student("Charlie")

gm.add_grade("Alice", 85)
gm.add_grade("Alice", 92)
gm.add_grade("Alice", 78)
gm.add_grade("Bob", 90)
gm.add_grade("Bob", 88)
gm.add_grade("Charlie", 95)

print("\nStudent Grades:")
gm.display_all_students()

stats = gm.get_class_statistics()
if stats:
    print(f"\nClass Statistics:")
    print(f"Total students: {stats['total_students']}")
    print(f"Class average: {stats['class_average']:.1f}")
    print(f"Highest grade: {stats['highest_grade']}")
    print(f"Lowest grade: {stats['lowest_grade']}")

# Exercise 4.3: Inventory Management
print("\n" + "="*50)
print("Exercise 4.3: Simple inventory management system")

print("\n💡 Solution 4.3:")
class Inventory:
    """Simple inventory management system."""
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, price):
        """Add an item to inventory."""
        if name in self.items:
            self.items[name]['quantity'] += quantity
            print(f"Added {quantity} {name}(s). New total: {self.items[name]['quantity']}")
        else:
            self.items[name] = {'quantity': quantity, 'price': price}
            print(f"Added new item: {name} (Qty: {quantity}, Price: ${price:.2f})")
    
    def remove_item(self, name, quantity):
        """Remove items from inventory."""
        if name in self.items:
            if self.items[name]['quantity'] >= quantity:
                self.items[name]['quantity'] -= quantity
                print(f"Removed {quantity} {name}(s). Remaining: {self.items[name]['quantity']}")
                
                # Remove item if quantity becomes 0
                if self.items[name]['quantity'] == 0:
                    del self.items[name]
                    print(f"{name} removed from inventory (quantity reached 0)")
            else:
                print(f"Cannot remove {quantity} {name}(s). Only {self.items[name]['quantity']} available")
        else:
            print(f"Item {name} not found in inventory")
    
    def update_price(self, name, new_price):
        """Update item price."""
        if name in self.items:
            old_price = self.items[name]['price']
            self.items[name]['price'] = new_price
            print(f"Updated {name} price: ${old_price:.2f} → ${new_price:.2f}")
        else:
            print(f"Item {name} not found in inventory")
    
    def get_inventory_value(self):
        """Calculate total inventory value."""
        total = sum(item['quantity'] * item['price'] for item in self.items.values())
        return total
    
    def display_inventory(self):
        """Display all items in inventory."""
        if not self.items:
            print("Inventory is empty")
            return
        
        print("\nCurrent Inventory:")
        print("-" * 50)
        for name, details in self.items.items():
            total_value = details['quantity'] * details['price']
            print(f"{name}: {details['quantity']} units @ ${details['price']:.2f} each = ${total_value:.2f}")
        
        total_value = self.get_inventory_value()
        print("-" * 50)
        print(f"Total Inventory Value: ${total_value:.2f}")

# Demonstrate inventory system
inventory = Inventory()
inventory.add_item("Laptop", 10, 999.99)
inventory.add_item("Mouse", 25, 29.99)
inventory.add_item("Keyboard", 15, 79.99)
inventory.add_item("Laptop", 5, 999.99)  # Add more laptops

inventory.display_inventory()

inventory.update_price("Mouse", 24.99)
inventory.remove_item("Keyboard", 5)
inventory.remove_item("Laptop", 20)  # Try to remove more than available

inventory.display_inventory()

# =============================================================================
# 5. CHALLENGE EXERCISES
# =============================================================================

print("\n\n🏆 CHALLENGE EXERCISES")
print("-" * 50)

# Exercise 5.1: Palindrome Checker
print("\nExercise 5.1: Check if a string is a palindrome (reads same forwards and backwards)")

print("\n💡 Solution 5.1:")
def is_palindrome(text):
    """Check if text is a palindrome (case-insensitive, ignoring spaces and punctuation)."""
    import string
    
    # Clean the text: remove punctuation and spaces, convert to lowercase
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if it reads the same forwards and backwards
    return clean_text == clean_text[::-1]

palindrome_tests = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam",
    "Was it a car or a cat I saw?"
]

for test in palindrome_tests:
    result = is_palindrome(test)
    print(f"'{test}' → {'✅ Palindrome' if result else '❌ Not a palindrome'}")

# Exercise 5.2: Anagram Checker
print("\n" + "="*50)
print("Exercise 5.2: Check if two strings are anagrams")

print("\n💡 Solution 5.2:")
def are_anagrams(str1, str2):
    """Check if two strings are anagrams."""
    # Clean and normalize both strings
    clean1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    # Sort characters and compare
    return sorted(clean1) == sorted(clean2)

def are_anagrams_counter(str1, str2):
    """Alternative solution using character counting."""
    from collections import Counter
    
    clean1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    return Counter(clean1) == Counter(clean2)

anagram_tests = [
    ("listen", "silent"),
    ("elbow", "below"),
    ("hello", "world"),
    ("The Eyes", "They See"),
    ("Dormitory", "Dirty Room")
]

for str1, str2 in anagram_tests:
    result1 = are_anagrams(str1, str2)
    result2 = are_anagrams_counter(str1, str2)
    print(f"'{str1}' & '{str2}' → {'✅ Anagrams' if result1 else '❌ Not anagrams'}")

# Exercise 5.3: Fibonacci Generator
print("\n" + "="*50)
print("Exercise 5.3: Generate Fibonacci sequence using different methods")

print("\n💡 Solution 5.3:")
def fibonacci_list(n):
    """Generate first n Fibonacci numbers as a list."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def fibonacci_generator(n):
    """Generate Fibonacci numbers using a generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_nth(n):
    """Calculate the nth Fibonacci number (0-indexed)."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("First 10 Fibonacci numbers (list):", fibonacci_list(10))
print("First 10 Fibonacci numbers (generator):", list(fibonacci_generator(10)))
print("10th Fibonacci number:", fibonacci_nth(10))

# Exercise 5.4: Roman Numeral Converter
print("\n" + "="*50)
print("Exercise 5.4: Convert between integers and Roman numerals")

print("\n💡 Solution 5.4:")
def int_to_roman(num):
    """Convert integer to Roman numeral."""
    if num <= 0 or num > 3999:
        return "Number must be between 1 and 3999"
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    for i in range(len(values)):
        count = num // values[i]
        if count:
            result += symbols[i] * count
            num -= values[i] * count
    
    return result

def roman_to_int(roman):
    """Convert Roman numeral to integer."""
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman.upper()):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Test Roman numeral conversion
test_numbers = [4, 9, 58, 1994, 3999]
for num in test_numbers:
    roman = int_to_roman(num)
    back_to_int = roman_to_int(roman)
    print(f"{num} → {roman} → {back_to_int}")

print("\n=== Congratulations! 🎉 ===")
print("You've completed a comprehensive set of Python exercises!")
print("These problems cover essential programming concepts and data structures.")
print("Keep practicing to master these skills!")

# =============================================================================
# BONUS: MINI PROJECT - HANGMAN GAME
# =============================================================================

print("\n\n🎯 BONUS MINI PROJECT: HANGMAN GAME")
print("-" * 50)

import random

class HangmanGame:
    """Simple Hangman word guessing game."""
    
    def __init__(self):
        self.words = [
            "python", "programming", "computer", "algorithm", "function",
            "variable", "loop", "condition", "string", "integer",
            "dictionary", "list", "tuple", "object", "class"
        ]
        self.word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
    
    def start_new_game(self):
        """Start a new game."""
        self.word = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        print("🎯 Welcome to Hangman!")
        print(f"Guess the {len(self.word)}-letter word!")
        print("You have 6 wrong guesses allowed.\n")
    
    def display_word(self):
        """Display the word with guessed letters revealed."""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def display_hangman(self):
        """Display hangman drawing based on wrong guesses."""
        stages = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
        ]
        return stages[self.wrong_guesses]
    
    def make_guess(self, letter):
        """Process a letter guess."""
        letter = letter.upper()
        
        if letter in self.guessed_letters:
            return "already_guessed"
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            return "correct"
        else:
            self.wrong_guesses += 1
            return "incorrect"
    
    def is_won(self):
        """Check if the game is won."""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_lost(self):
        """Check if the game is lost."""
        return self.wrong_guesses >= self.max_wrong_guesses
    
    def play_demo(self):
        """Play a demonstration game."""
        self.start_new_game()
        
        # Simulate some guesses for demonstration
        demo_guesses = ['P', 'R', 'O', 'G', 'A', 'M', 'I', 'N']
        
        for guess in demo_guesses:
            if self.is_won() or self.is_lost():
                break
            
            print(self.display_hangman())
            print(f"Word: {self.display_word()}")
            print(f"Guessed letters: {' '.join(sorted(self.guessed_letters))}")
            print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
            print(f"\nGuessing letter: {guess}")
            
            result = self.make_guess(guess)
            if result == "correct":
                print(f"✅ Good guess! '{guess}' is in the word.")
            elif result == "incorrect":
                print(f"❌ Sorry, '{guess}' is not in the word.")
            elif result == "already_guessed":
                print(f"⚠️  You already guessed '{guess}'.")
            
            print("-" * 40)
        
        # Final result
        print(self.display_hangman())
        print(f"Word: {self.display_word()}")
        
        if self.is_won():
            print(f"🎉 Congratulations! You guessed '{self.word}' correctly!")
        elif self.is_lost():
            print(f"💀 Game Over! The word was '{self.word}'.")

# Run a demo game
print("\n💡 Hangman Game Demo:")
game = HangmanGame()
game.play_demo()

print("\n" + "="*60)
print("🏁 END OF PYTHON EXERCISES")
print("="*60)
print("Great job working through all these exercises!")
print("Each exercise builds important programming skills:")
print("• Problem decomposition")
print("• Algorithm design")
print("• Data structure usage")
print("• Code organization")
print("• Testing and debugging")
print("\nKeep practicing and building projects to improve your skills! 🚀")