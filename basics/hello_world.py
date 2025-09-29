"""
Title: Hello World Examples
Author: Python-Basics-to-Advanced
Difficulty: Beginner
Description: Various ways to print "Hello, World!" in Python
"""

# Basic Hello World
print("Hello, World!")

# Hello World with variables
message = "Hello, World!"
print(message)

# Hello World with user input
name = input("What's your name? ")
print(f"Hello, {name}!")


# Hello World with functions
def greet(name="World"):
    """
    Greets a person with a personalized message.

    Args:
        name (str): Name of the person to greet. Defaults to "World".
    """
    return f"Hello, {name}!"


# Test the function
print(greet())
print(greet("Python"))

# Multiple language greetings
greetings = {
    "english": "Hello, World!",
    "spanish": "¡Hola, Mundo!",
    "french": "Bonjour, le Monde!",
    "german": "Hallo, Welt!",
    "italian": "Ciao, Mondo!"
}

print("\n--- Greetings in Different Languages ---")
for language, greeting in greetings.items():
    print(f"{language.title()}: {greeting}")

# Interactive greeting
print("\n--- Interactive Greeting ---")
language = input("Choose a language (english/spanish/french/german/italian): ").lower()
if language in greetings:
    print(greetings[language])
else:
    print("Language not supported, here's English: Hello, World!")
