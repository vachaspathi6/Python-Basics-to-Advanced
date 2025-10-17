# Python String Practice Programs

## 1. Reverse a String
```python
s = input("Enter a string: ")
print("Reversed string:", s[::-1])
```

## 2. Check Palindrome String
```python
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

## 3. Count Vowels and Consonants
```python
s = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for c in s if c in vowels)
consonant_count = sum(1 for c in s if c.isalpha() and c not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
```

## 4. Find Frequency of Each Character
```python
s = input("Enter a string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(freq)
```

## 5. Remove All Punctuations
```python
import string
s = input("Enter a string: ")
cleaned = ''.join(c for c in s if c not in string.punctuation)
print("Without punctuation:", cleaned)
```

## 6. Convert String to Uppercase and Lowercase
```python
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
```

## 7. Replace Spaces with Hyphens
```python
s = input("Enter a string: ")
print("Modified string:", s.replace(' ', '-'))
```

## 8. Count Words in a Sentence
```python
s = input("Enter a sentence: ")
print("Word count:", len(s.split()))
```

## 9. Find Longest Word in a Sentence
```python
s = input("Enter a sentence: ").split()
longest = max(s, key=len)
print("Longest word:", longest)
```

## 10. Check if String Contains Only Digits
```python
s = input("Enter a string: ")
print("Contains only digits:", s.isdigit())
```

## 11. Swap Case of Each Character
```python
s = input("Enter a string: ")
print("Swapped case:", s.swapcase())
```

## 12. Remove Duplicate Characters
```python
s = input("Enter a string: ")
result = ''.join(sorted(set(s), key=s.index))
print("Without duplicates:", result)
```

## 13. Count Occurrence of a Substring
```python
s = input("Enter main string: ")
sub = input("Enter substring: ")
print("Occurrences:", s.count(sub))
```

## 14. Check Anagram Strings
```python
s1 = input("Enter first string: ").replace(' ', '').lower()
s2 = input("Enter second string: ").replace(' ', '').lower()
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
```

## 15. Print All Substrings
```python
s = input("Enter a string: ")
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
```

## 16. Remove All Digits from a String
```python
s = input("Enter a string: ")
cleaned = ''.join(c for c in s if not c.isdigit())
print("Without digits:", cleaned)
```

## 17. Capitalize First Letter of Each Word
```python
s = input("Enter a sentence: ")
print("Capitalized:", s.title())
```

## 18. Check String Starts and Ends With Same Character
```python
s = input("Enter a string: ")
if s[0] == s[-1]:
    print("Starts and ends with same character")
else:
    print("Different start and end characters")
```

## 19. Count Uppercase and Lowercase Letters
```python
s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)
```

## 20. Find Common Characters Between Two Strings
```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
common = set(s1) & set(s2)
print("Common characters:", ''.join(common))
```
