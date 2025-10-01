# Day7_FileHandling.py
# Author: Durga
# Purpose: Practice file handling with text, log, and JSON files in Python

import json

# ------------------------------
# Program 1: Write & Read a Text File
# ------------------------------
with open("notes.txt", "w") as file:
    file.write("Learning Python is fun!\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print("Program 1 Output: ")
    print(content)
    print("-" * 50)

# ------------------------------
# Program 2: Word Counter from File
# ------------------------------
filename = input("Enter filename to count words: ")
try:
    with open(filename, "r") as file:
        data = file.read()
        words = data.split()
        print(f"Program 2 Output: Total words in '{filename}': {len(words)}")
except FileNotFoundError:
    print(f"File '{filename}' not found!")
print("-" * 50)

# ------------------------------
# Program 3: Append Data to File
# ------------------------------
with open("log.txt", "a") as file:
    file.write("Program executed successfully\n")

with open("log.txt", "r") as file:
    print("Program 3 Output: Current log.txt content:")
    print(file.read())
print("-" * 50)

# ------------------------------
# Program 4: Save & Load Student Marks
# ------------------------------
students = [
    {"name": "Durga", "marks": 85},
    {"name": "Arya", "marks": 90},
    {"name": "Radha", "marks": 78}
]

# Write student marks to file
with open("marks.txt", "w") as file:
    for student in students:
        file.write(f"{student['name']}, {student['marks']}\n")

# Read and display neatly
print("Program 4 Output: Student Marks")
with open("marks.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(", ")
        print(f"Name: {name}, Marks: {marks}")
print("-" * 50)

# ------------------------------
# Program 5: JSON File Handling
# ------------------------------
student = {
    "name": "Durga",
    "age": 20,
    "skills": ["Python", "Data Science"],
    "isGraduated": False
}

# Save to JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read from JSON file
with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print("Program 5 Output: Loaded JSON Data")
    print(f"Name: {loaded_student['name']}")
    print(f"Age: {loaded_student['age']}")
    print(f"Skills: {', '.join(loaded_student['skills'])}")
    print(f"Graduated: {loaded_student['isGraduated']}")
print("-" * 50)
