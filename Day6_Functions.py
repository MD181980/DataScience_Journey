# Day6_Functions.py
# Author: Durga
# Purpose: Practice Python functions with real-world examples

#1️⃣ Greeting Function 
def greet(name):
  print(f'hello, {name} wellcom to python') #print data

greet('durga')

#Calculator (Reusable Function)
# Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Main Program
print("Welcome to Calculator!")

# Take input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for operation
print("Select operation: +, -, *, /")
operation = input("Enter operation: ")

# Perform operation
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation!"

# Display result
print(f"Result: {result}")

#Factorial Function

def fact(num):
    if num<0:
        return print("not defind")
    elif num==0 or num==1:
        return 1
    else:
        return num*fact(num-1) # calculate factorial

num=int (input('enter a number to find factorial')) # take in put
f=fact(num) #call function
print(f"factorial of {num} is {f} ")

# Banking System (Main Assignment)

balance = 0.0  # global variable

def check_balance():   # shows current balance
    print(f"Balance: {balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"{amount} deposited successfully. ")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance! Transaction failed.")
    else:
        balance -= amount
        print(f"{amount} withdrawn successfully.")


print("Welcome to the Banking System\n")

while True:
    print("1. Check Balance\n2. Deposit Amount\n3. Withdraw Amount\n4. Exit\n")
    op = int(input("Choose option for banking: "))

    if op == 1:
        check_balance()
    elif op == 2:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif op == 3:
        if balance <= 0:
            print("Balance is zero. Please deposit money first.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
    elif op == 4:
        print("Exiting banking system. Thank you!")
        break
    else:
        print("Invalid input, try again.")

    
        

        
        
