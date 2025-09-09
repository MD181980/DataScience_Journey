"""
Day2_ControlStructures.py
--------------------------
This file contains beginner Python programs focusing on control structures:
1. Grade calculator using if-elif-else
2. Multiplication table (1 to 5) using nested loops
3. User input validation (only positive integers)
"""


# 1. Grade calculator using if-elif-else
marks = int(input("Enter your marks (0-100): "))
print("Your grade is:", end=" ")

if 90 <= marks <= 100:
    print("A")
elif 80 <= marks < 90:
    print("B")
elif 70 <= marks < 80:
    print("C")
elif 60 <= marks < 70:
    print("D")
elif 0 <= marks < 60:
    print("F")
else:
    print("Invalid marks entered!")  # handles values outside 0-100


# 2. Multiplication table (1 to 5) using nested loops
print("\nMultiplication Table (1 to 5):")
for i in range(1, 6):        # outer loop → rows
    for x in range(1, 6):    # inner loop → columns
        print(i * x, end="\t")
    print()


# 3. User input validation for positive integers
while True:
    i = int(input("Enter a positive number: "))
    if i < 0:
        print("❌ Only positive numbers are accepted, try again!")
        continue
    else:
        print("✅ You entered:", i)
        break
