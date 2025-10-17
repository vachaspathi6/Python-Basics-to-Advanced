
# 11 - What are Strings?

In Python, anything that you enclose between single or double quotation marks is considered a **string**. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

### Example:

```python
name = "Yash"
print("Hello, " + name)
```

**Output:**

```
Hello, Yash
```
---
> **Note:** It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
---

Sometimes, the user might need to put quotation marks in between the strings. For example, consider the sentence: `He said, “I want to eat an apple”.`

1 How will you print this statement in Python?

```python
print('He said, "I am the Best".') #here observe ' "" ' for printing ascii ""
```
Output: 
```
He said, "I am the Best".
```

2 Using Backslash
```py
print("using baclslash \\ ") #Remember above Escape sequences
print("He said, \"I am a King\".")
```
Output:
```
using baclslash \ 
He said, "I am a King".
```

### Multiline Strings
If our string has multiple lines, we can create them like this:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```


### Accessing Characters of a String (Imagine String Array)
In Python, a string is like an array of characters. We can access parts of a string by using its **index**, which starts from 0. Square brackets can be used to access elements of the string:

```python
print(name[0])
print(name[1])
```


### Looping Through the String
We can loop through strings using a `for` loop like this:

```python
for character in name:
    print(character)
```
```
Y
a
s
h
```

The above code prints all the characters in the string `name` one by one!


---

# 12 - String Slicing & Operations on String

## Length of a String

We can find the length of a string using the `len()` function.

**Example:**

```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```

**Output:**

```
Mango is a 5 letter word.
```


## String as an Array

A string is essentially a sequence of characters also called an array. Thus, we can access the elements of this array.
 - In Python string slicing, the general syntax is:
    ```bash
    string[start:stop:step]
    ```
- **start index** – Inclusive
- **stop index** – Exclusive


**Example:**

```python
pie = "ApplePie"
print(pie[:5])
print(pie[6])  # returns character at specified index
```

**Output:**

```
Apple
i
```

---
> **Note:** This method of specifying the start and end index to specify a part of a string is called **slicing**.
---


## Slicing Example

```python
pie = "ApplePie"
print(pie[:5])       # Slicing from Start
print(pie[5:])       # Slicing till End
print(pie[2:6])      # Slicing in between
print(pie[-8:])      # Slicing using negative index
print(pie[-5:-2])    # Negative indexing in a range
print(pie[::2])      # Slicing with step
print(pie[::-1])     # Reversing the string using slicing
print(pie[1:7:2])    # Slicing from index 1 to 6 with step 2
```

**Output:**

```
Apple
Pie
pleP
ApplePie
ple
ApPe
eiPelpA
petr
```



---
## String Slicing & Operations on String

```python
text = "Python"
# Indexes:    0 1 2 3 4 5
# negIndex:  -6-5-4-3-2-1
```


### 12.1 `text[index]`

**Access a single character by index**

```python
print(text[2])   # Output: 't'
```

* Returns the character at index 2 (zero-based).
* Index must be within range.

<br>

### 12.2 `text[start:stop]`

**Slice from start to stop (exclusive)**

```python
print(text[1:4])   # Output: 'yth'
```

* Includes index 1
* Excludes index 4
* Characters at indexes 1, 2, 3

<br>

### 12.3 `text[:stop]`

**Slice from beginning to stop (exclusive)**

```python
print(text[:4])   # Output: 'Pyth'
```

* Starts from index 0
* Ends before index 4

<br>

### 12.4 `text[start:]`

**Slice from start to end**

```python
print(text[2:])   # Output: 'thon'
```

* Starts from index 2
* Goes to the end of the string

<br>

### 12.5 `text[:]`

**Full copy of the string**

```python
print(text[:])   # Output: 'Python'
```

* Equivalent to a full slice / copy

<br>

### 12.6 `text[start:stop:step]`

**Slice with steps**

```python
print(text[::2])     # Output: 'Pto'
```

* Every 2nd character from index 0: `P`, `t`, `o`

```python
print(text[1:5:2])   # Output: 'yh'
```

* From index 1 to 4, every 2nd character: `y`, `h`

<br>

### 12.7 `text[::-1]`

**Reverse the string**

```python
print(text[::-1])   # Output: 'nohtyP'
```

* Step of -1 reverses the string

<br>

### 12.8 `text[-n:]` or `text[:-n]`

**Using negative indices**

```python
print(text[-3:])    # Output: 'hon'
print(text[:-3])    # Output: 'Pyt'
```

* Negative indices count from the end

---

# 13 - String Methods in Python

Python provides a set of built-in methods that we can use to alter and modify strings.



### `upper()`

Converts a string to upper case.

```python
str1 = "AbcDEfghIJ"
print(str1.upper())
# Output: 'ABCDEFGHIJ'
```

<br>

### `lower()`

Converts a string to lower case.

```python
str1 = "AbcDEfghIJ"
print(str1.lower())
# Output: 'abcdefghij'
```

<br>

### `strip()`

Removes any white spaces before and after the string.

```python
str2 = " Silver Spoon "
print(str2.strip())
# Output: 'Silver Spoon'
```
<br>

### `rstrip()` -  **Imp 🚩**

Removes any trailing characters.

```python
str3 = "Hello !!!"
print(str3.rstrip("!"))
# Output: 'Hello'
```

<br>

### `replace()` - -  **Imp 🚩**

Replaces all occurrences of a string with another string.

```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
# Output: 'Silver Moon'
```

<br>

### `split()` -  **Imp 🚩** - used to convert strings to lists / arrays in deveopment and DSA 

Splits the string at the specified instance and returns list items.

```python
str2 = "Silver Spoon"
print(str2.split(" "))
# Output: ['Silver', 'Spoon']
```

<br>

### `capitalize()` - First word only (Not like upper)

Turns only the first character to uppercase.

```python
str1 = "hello"
print(str1.capitalize())
# Output: 'Hello'

str2 = "hello WorlD"
print(str2.capitalize())
# Output: 'Hello world'
```

<br>

### `center()`

Aligns the string to the center.

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
# Output: '            Welcome to the Console!!!'

print(str1.center(50, "."))
# Output: '............Welcome to the Console!!!.............'
```

<br>

### `count()` -  **Imp 🚩**

Returns the number of times the given value has occurred.

```python
str2 = "Abracadabra"
print(str2.count("a"))
# Output: 4
```

<br>

### `endswith()` -  **Imp 🚩** - Used in devlopment to check Links, and cut them as required also in DSA

Checks if the string ends with a given value.

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# Output: True

print(str1.endswith("to", 4, 10))
# Output: True
```

<br>

### `find()` -  **Imp 🚩**

Searches for the first occurrence of the given value.

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
# Output: 10

print(str1.find("Daniel"))
# Output: -1
```

<br>

### `index()` -  **Imp 🚩**

Similar to `find()` but raises an exception if value is absent.

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# Output: 13

print(str1.index("Daniel"))
# Output: ValueError: substring not found
```

<br>

### `isalnum()` -  **Imp 🚩**

Returns True if string contains only A-Z, a-z, 0-9.

```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# Output: True
```

<br>

### `isalpha()` -  **Imp 🚩**

Returns True if string contains only A-Z, a-z.

```python
str1 = "Welcome"
print(str1.isalpha())
# Output: True
```

<br>

### `islower()`

Returns True if all characters are lowercase.

```python
str1 = "hello world"
print(str1.islower())
# Output: True
```

<br>

### `isprintable()`

Returns True if all values are printable.

```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
# Output: True
```

<br>

### `isspace()` -  **Imp 🚩**

Returns True if the string contains only whitespace.

```python
str1 = "        "       # Using Spacebar
print(str1.isspace())

str2 = "\t\t"           # Using Tab
print(str2.isspace())
# Output: True, True
```

<br>

### `istitle()`

Returns True if the first letter of each word is capitalized.

```python
str1 = "World Health Organization" 
print(str1.istitle())
# Output: True

str2 = "To kill a Mocking bird"
print(str2.istitle())
# Output: False
```

<br>

### `isupper()`

Returns True if all characters are uppercase.

```python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
# Output: True
```

<br>

### `startswith()`

Checks if the string starts with a given value.

```python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# Output: True
```

<br>

### `swapcase()`

Changes character casing: upper to lower and vice versa.

```python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# Output: 'pYTHON IS A iNTERPRETED lANGUAGE'
```

<br>

### `title()`

Capitalizes each letter of the words in the string.

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
# Output: "He'S Name Is Dan. Dan Is An Honest Man."
```

---
