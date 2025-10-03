# Write a Program in Python to remove punctuations from given string.

import string

string = input("Enter Your String:\n")
punc =   '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""

for i in string:
    if i not in punc: 
        result=result + i

print(result)