# Day3_Lists_Tuples.py
# Author: Durga
# Purpose: Practice lists and tuples in Python





#1️⃣ Favorite Movies List



movies=['jayam','hello','kali','kalki','varsham'] #Create a list of your 5 favorite movies.
print("My Favorite Movies are: ")
for movie in movies:                   #Print all movies one by one using a for loop
    print(movie)


#2️⃣ Find Largest & Smallest Number
#Create a list of numbers.

numbers=[2,3,4,22,33,1,33,7,8,67,66,98,234,0,-4,-3]

#Print the largest and smallest number using max() and min().

print(f"\n\n\nthe largest number is { max(numbers)}\n The smallest number is  {min(numbers)}\n\n")



"""3️⃣ Average Marks

Ask the user to enter 5 marks.

Store them in a list.

Calculate and print the average marks."""



marks = list(map(int,input ("enter 5 subjects marks by saparated space ").split()))

#calculate average using sum and len functions
average=sum(marks)/(len(marks))

print(f'Average marks is : {average}\n\n\n')




"""4️⃣ Weekdays Tuple

Create a tuple of weekdays: ("Monday", "Tuesday", ..., "Sunday").

Print only the weekend days."""


# Tuple of weekdays
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


# Accessing weekend days using indexing
print("Weekend days are:", weekdays[5], "and", weekdays[6])




'''5️⃣ Student List Management (Main Assignment)

Create a list of student names.

Add a new student at the end.

Insert a student at position 2.

Remove the last student.

Print the final list.'''


students=['raju','ravi','ammu','gopi']  #create student list
students.insert(2,'durga')  #insret student 
students.pop(-1)
print("\n\nlist of students :",students)






