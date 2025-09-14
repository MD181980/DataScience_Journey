# Day4_Strings.py
# Author: Durga
# Purpose: Practice string operations in Python

# ----------------------------
# Program 1: String Basics
# ----------------------------
# Take user input and show basic string operations
name = input("Enter your name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length of name:", len(name))

# ----------------------------
# Program 2: Palindrome Check
# ----------------------------
# A word is palindrome if it reads same forwards and backwards
word = input("\nEnter a word to check if it's palindrome: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# ----------------------------
# Program 3: Count Vowels
# ----------------------------
# Count vowels in a given sentence
sentence = input("\nEnter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# ----------------------------
# Program 4: Word Replacement
# ----------------------------
# Replace a word in a sentence
text = "I love programming in Python"
updated_text = text.replace("Python", "Data Science")
print("\nOriginal text:", text)
print("Updated text:", updated_text)

# ----------------------------
# Program 5: String Reversal (Main Assignment)
# ----------------------------
# Reverse a user given string
user_string = input("\nEnter a string to reverse: ")
print("Reversed string:", user_string[::-1])
