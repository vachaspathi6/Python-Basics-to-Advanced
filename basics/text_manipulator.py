import re
import base64

def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def capitalize_words(text):
    return text.title()

def reverse_text(text):
    return text[::-1]

def remove_spaces(text):
    return text.replace(" ", "")

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    return len(text)

def vowel_consonant_count(text):
    vowels = "aeiouAEIOU"
    v = sum(1 for ch in text if ch in vowels)
    c = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
    return v, c

def find_replace(text, find, replace):
    return text.replace(find, replace)

def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_text(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except:
        return "Invalid encrypted text!"

# ---------- Main Program ----------
if __name__ == "__main__":
    text = input("Enter your text: ")
    
    while True:
        print("\n--- TEXT MANIPULATOR MENU ---")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Capitalize Each Word")
        print("4. Reverse Text")
        print("5. Remove Spaces")
        print("6. Remove Punctuation")
        print("7. Word Count")
        print("8. Character Count")
        print("9. Vowel & Consonant Count")
        print("10. Find & Replace")
        print("11. Encrypt Text")
        print("12. Decrypt Text")
        print("13. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            print(to_upper(text))
        elif choice == "2":
            print(to_lower(text))
        elif choice == "3":
            print(capitalize_words(text))
        elif choice == "4":
            print(reverse_text(text))
        elif choice == "5":
            print(remove_spaces(text))
        elif choice == "6":
            print(remove_punctuation(text))
        elif choice == "7":
            print("Word count:", word_count(text))
        elif choice == "8":
            print("Character count:", char_count(text))
        elif choice == "9":
            v, c = vowel_consonant_count(text)
            print("Vowels:", v, "Consonants:", c)
        elif choice == "10":
            f = input("Word to find: ")
            r = input("Replace with: ")
            text = find_replace(text, f, r)
            print("Updated text:", text)
        elif choice == "11":
            text = encrypt_text(text)
            print("Encrypted:", text)
        elif choice == "12":
            text = decrypt_text(text)
            print("Decrypted:", text)
        elif choice == "13":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
