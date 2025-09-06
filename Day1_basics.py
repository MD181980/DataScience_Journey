# Day1_Basics.py
# Author: Durga
# Purpose: Basic Python practice (Variables, Input/Output, Arithmetic)

import math

# --- Example 1: Store personal details ---
name = "Durga"
age = 20
college = "Swarnandhra College of Engineering and Technology"

print("My Name:", name)
print("My Age:", age)
print("My College:", college)

# --- Example 2: Arithmetic operations ---
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

# --- Example 3: Area and Circumference of a Circle ---
radius = float(input("Enter circle radius: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius

print("Area of Circle:", area)
print("Circumference of Circle:", circumference)

# --- Assignment: Temperature Conversion ---
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Celsius to Fahrenheit:", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Fahrenheit to Celsius:", celsius)
