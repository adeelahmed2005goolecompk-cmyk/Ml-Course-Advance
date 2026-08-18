# Theory about this code:

# Python lists are used to store multiple values in a single variable.
# This assignment covers creating, accessing, updating, adding, and removing list items.
# It also demonstrates list slicing, loops, list comprehension, sorting, copying, and joining
# lists. Built-in functions such as max(), min(), sum(), and len() are used for calculations.
# The program also includes practical exercises for numbers, students, marks, and random
# data. Finally, a menu-driven program demonstrates real-world list operations interactively.







"""
Python Lists – Practical Assignment
Subject: Python Programming
Topic: Python Lists
"""

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("╔" + "═" * 68 + "╗")
print("║" + " " * 15 + "PYTHON LISTS - PRACTICAL ASSIGNMENT" + " " * 16 + "║")
print("╚" + "═" * 68 + "╝")

# ==============================================
# PART A – BASIC QUESTIONS
# ==============================================
print("\n" + "█" * 70)
print("█  PART A – BASIC QUESTIONS")
print("█" * 70)

# Q1
print("\n● Create a list of fruits")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(f"  ➜ {fruits}")

# Q2
print("\n● List of five integers")
numbers = [10, 20, 30, 40, 50]
print(f"  ➜ List: {numbers}")
print(f"  ➜ First: {numbers[0]}, Last: {numbers[4]}, Third: {numbers[2]}")

# Q3
print("\n● Negative indexing")
numbers = [10, 20, 30, 40, 50]
print(f"  ➜ List: {numbers}")
print(f"  ➜ Last: {numbers[-1]}, Second last: {numbers[-2]}")

# ==============================================
# PART B – ACCESS LIST ITEMS
# ==============================================
print("\n" + "█" * 70)
print("█  PART B – ACCESS LIST ITEMS")
print("█" * 70)

# Q4
print("\n● Access specific elements")
colors = ["Red", "Green", "Blue", "Yellow", "Black"]
print(f"  ➜ Colors: {colors}")
print(f"  ➜ First: {colors[0]}, Third: {colors[2]}, Last: {colors[-1]}")

# Q5
print("\n● Slicing from index 1 to 3")
colors = ["Red", "Green", "Blue", "Yellow", "Black"]
print(f"  ➜ {colors[1:4]}")

# Q6
print("\n● First four elements")
colors = ["Red", "Green", "Blue", "Yellow", "Black"]
print(f"  ➜ {colors[:4]}")

# ==============================================
# PART C – CHANGE LIST ITEMS
# ==============================================
print("\n" + "█" * 70)
print("█  PART C – CHANGE LIST ITEMS")
print("█" * 70)

# Q7
print("\n● Replace Dog with Rabbit")
animals = ["Cat", "Dog", "Lion", "Tiger"]
print(f"  ➜ Original: {animals}")
animals[1] = "Rabbit"
print(f"  ➜ Updated:  {animals}")

# Q8
print("\n● Replace last two items")
animals = ["Cat", "Dog", "Lion", "Tiger"]
print(f"  ➜ Original: {animals}")
animals[-2:] = ["Elephant", "Horse"]
print(f"  ➜ Updated:  {animals}")

# Q9
print("\n● Change items from index 1 to 3")
animals = ["Cat", "Dog", "Lion", "Tiger", "Bear"]
print(f"  ➜ Original: {animals}")
animals[1:4] = ["Orange", "Purple", "Pink"]
print(f"  ➜ Updated:  {animals}")

# ==============================================
# PART D – ADD LIST ITEMS
# ==============================================
print("\n" + "█" * 70)
print("█  PART D – ADD LIST ITEMS")
print("█" * 70)

# Q10
print("\n● Add items using append(), extend(), insert()")
numbers = [10, 20, 30]
print(f"  ➜ Original:     {numbers}")
numbers.append(40)
print(f"  ➜ After append: {numbers}")
numbers.extend([50, 60])
print(f"  ➜ After extend: {numbers}")
numbers.insert(0, 5)
print(f"  ➜ Final:        {numbers}")

# Q11
print("\n● Add five student names")
students = []
students.append("Ali")
students.append("Ahmed")
students.append("Sara")
students.append("Ayesha")
students.append("Bilal")
print(f"  ➜ {students}")

# ==============================================
# PART E – REMOVE LIST ITEMS
# ==============================================
print("\n" + "█" * 70)
print("█  PART E – REMOVE LIST ITEMS")
print("█" * 70)

# Q12
print("\n● Remove items from cities")
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]
print(f"  ➜ Original: {cities}")
cities.remove("Islamabad")
print(f"  ➜ After remove: {cities}")
cities.pop()
print(f"  ➜ After pop: {cities}")
del cities[0]
print(f"  ➜ After del: {cities}")
cities.clear()
print(f"  ➜ After clear: {cities}")

# Q13
print("\n● Remove number 5")
numbers = list(range(1, 11))
print(f"  ➜ Original: {numbers}")
numbers.remove(5)
print(f"  ➜ Updated:  {numbers}")

# ==============================================
# PART F – LOOP THROUGH LISTS
# ==============================================
print("\n" + "█" * 70)
print("█  PART F – LOOP THROUGH LISTS")
print("█" * 70)

# Q14
print("\n● Print fruits using for loop")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for fruit in fruits:
    print(f"  ➜ {fruit}")

# Q15
print("\n● Print with indices using enumerate()")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for index, fruit in enumerate(fruits):
    print(f"  ➜ {index}: {fruit}")

# Q16
print("\n● Print even numbers")
numbers = [4, 7, 9, 10, 12, 15, 20]
print(f"  ➜ List: {numbers}")
print("  ➜ Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(f"    • {num}")

# ==============================================
# PART G – LIST COMPREHENSION
# ==============================================
print("\n" + "█" * 70)
print("█  PART G – LIST COMPREHENSION")
print("█" * 70)

# Q17
print("\n● Squares from 1 to 10")
squares = [i**2 for i in range(1, 11)]
print(f"  ➜ {squares}")

# Q18
print("\n● Even numbers from 1 to 20")
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(f"  ➜ {even_numbers}")

# Q19
print("\n● Names starting with A")
names = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
print(f"  ➜ Original: {names}")
names_starting_a = [name for name in names if name.startswith('A')]
print(f"  ➜ Filtered: {names_starting_a}")

# Q20
print("\n● Convert words to uppercase")
words = ["python", "java", "c++", "html"]
print(f"  ➜ Original: {words}")
uppercase_words = [word.upper() for word in words]
print(f"  ➜ Uppercase: {uppercase_words}")

# ==============================================
# PART H – SORT LISTS
# ==============================================
print("\n" + "█" * 70)
print("█  PART H – SORT LISTS")
print("█" * 70)

# Q21
print("\n● Sort ascending")
numbers = [45, 12, 98, 23, 67, 5]
print(f"  ➜ Original:  {numbers}")
numbers.sort()
print(f"  ➜ Ascending: {numbers}")

# Q22
print("\n● Sort descending")
numbers = [45, 12, 98, 23, 67, 5]
print(f"  ➜ Original:   {numbers}")
numbers.sort(reverse=True)
print(f"  ➜ Descending: {numbers}")

# Q23
print("\n● Sort names alphabetically")
names = ["Bilal", "Ahmed", "Sara", "Ali", "Usman"]
print(f"  ➜ Original:     {names}")
names.sort()
print(f"  ➜ Alphabetical: {names}")

# ==============================================
# PART I – COPY LISTS
# ==============================================
print("\n" + "█" * 70)
print("█  PART I – COPY LISTS")
print("█" * 70)

# Q24
print("\n● Create copies")
list1 = [10, 20, 30, 40]
copy1 = list1.copy()
copy2 = list(list1)
print(f"  ➜ Original:     {list1}")
print(f"  ➜ Copy (copy):  {copy1}")
print(f"  ➜ Copy (list):  {copy2}")

# Q25
print("\n● Modify copy - check original")
list1 = [10, 20, 30, 40]
copy_list = list1.copy()
print(f"  ➜ Original: {list1}")
print(f"  ➜ Copy:     {copy_list}")
copy_list[0] = 100
print(f"  ➜ After modifying copy[0] = 100:")
print(f"    Original: {list1}")
print(f"    Copy:     {copy_list}")
print(f"  ➜ Original remains unchanged ✓")

# ==============================================
# PART J – JOIN LISTS
# ==============================================
print("\n" + "█" * 70)
print("█  PART J – JOIN LISTS")
print("█" * 70)

# Q26
print("\n● Join lists using + and extend()")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"  ➜ List1: {list1}")
print(f"  ➜ List2: {list2}")
combined = list1 + list2
print(f"  ➜ Using +: {combined}")
list1.extend(list2)
print(f"  ➜ Using extend(): {list1}")

# Q27
print("\n● Combine student lists")
class_a = ["Ali", "Ahmed", "Sara"]
class_b = ["Bilal", "Ayesha", "Usman"]
print(f"  ➜ Class A: {class_a}")
print(f"  ➜ Class B: {class_b}")
all_students = class_a + class_b
print(f"  ➜ All students: {all_students}")

# ==============================================
# PART K – LIST METHODS
# ==============================================
print("\n" + "█" * 70)
print("█  PART K – LIST METHODS")
print("█" * 70)

# Q28
print("\n● All list methods")
numbers = [10, 20, 30, 20, 40]
print(f"  ➜ Original:    {numbers}")
numbers.append(50)
print(f"  ➜ append(50):   {numbers}")
numbers.insert(2, 25)
print(f"  ➜ insert(2,25): {numbers}")
numbers.remove(20)
print(f"  ➜ remove(20):   {numbers}")
popped = numbers.pop()
print(f"  ➜ pop():        {numbers} (removed: {popped})")
print(f"  ➜ count(20):    {numbers.count(20)}")
print(f"  ➜ index(30):    {numbers.index(30)}")
numbers.sort()
print(f"  ➜ sort():       {numbers}")
numbers.reverse()
print(f"  ➜ reverse():    {numbers}")
copy_numbers = numbers.copy()
print(f"  ➜ copy():       {copy_numbers}")
numbers.clear()
print(f"  ➜ clear():      {numbers}")

# ==============================================
# PART L – PROGRAMMING EXERCISES
# ==============================================
print("\n" + "█" * 70)
print("█  PART L – PROGRAMMING EXERCISES")
print("█" * 70)

# Q29
print("\n● Max, Min, Sum")
numbers = [15, 22, 8, 90, 34, 67]
print(f"  ➜ List: {numbers}")
print(f"  ➜ Max:  {max(numbers)}")
print(f"  ➜ Min:  {min(numbers)}")
print(f"  ➜ Sum:  {sum(numbers)}")

# Q30
print("\n● Average of numbers")
numbers = [15, 22, 8, 90, 34, 67]
average = sum(numbers) / len(numbers)
print(f"  ➜ List:    {numbers}")
print(f"  ➜ Average: {average:.2f}")

# Q31
print("\n● Count even and odd")
numbers = [4, 7, 9, 10, 12, 15, 20, 25, 30, 33]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print(f"  ➜ List:        {numbers}")
print(f"  ➜ Even count:  {even_count}")
print(f"  ➜ Odd count:   {odd_count}")

# Q32
print("\n● Remove duplicates")
numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"  ➜ Original: {numbers}")
unique_numbers = list(dict.fromkeys(numbers))
print(f"  ➜ Unique:   {unique_numbers}")

# Q33
print("\n● User input five numbers")
user_numbers = []
for i in range(5):
    num = float(input(f"  Enter number {i+1}: "))
    user_numbers.append(num)
print(f"\n  ➜ Numbers:  {user_numbers}")
print(f"  ➜ Largest:  {max(user_numbers)}")
print(f"  ➜ Smallest: {min(user_numbers)}")
print(f"  ➜ Sum:      {sum(user_numbers)}")
print(f"  ➜ Average:  {sum(user_numbers)/len(user_numbers):.2f}")

# Q34
print("\n● Random numbers greater than 50")
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"  ➜ All numbers:     {random_numbers}")
greater_than_50 = [num for num in random_numbers if num > 50]
print(f"  ➜ Greater than 50: {greater_than_50}")

# Q35
print("\n● Student marks and grade")
marks = [85, 72, 90, 65, 78, 88, 92, 70]
print(f"  ➜ Marks:      {marks}")
print(f"  ➜ Highest:    {max(marks)}")
print(f"  ➜ Lowest:     {min(marks)}")
avg_marks = sum(marks) / len(marks)
print(f"  ➜ Average:    {avg_marks:.2f}")
if avg_marks >= 90:
    grade = "A+ (Excellent)"
elif avg_marks >= 80:
    grade = "A (Very Good)"
elif avg_marks >= 70:
    grade = "B (Good)"
elif avg_marks >= 60:
    grade = "C (Satisfactory)"
elif avg_marks >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"
print(f"  ➜ Grade:      {grade}")

# ==============================================
# BONUS CHALLENGE – Q36
# ==============================================
print("\n" + "█" * 70)
print("█  BONUS CHALLENGE – MENU DRIVEN PROGRAM")
print("█" * 70)

def menu_driven_program():
    my_list = []
    while True:
        print("\n" + "┌" + "─" * 40 + "┐")
        print("│" + " " * 12 + "LIST OPERATIONS" + " " * 15 + "│")
        print("├" + "─" * 40 + "┤")
        print("│ 1. Add Item        │")
        print("│ 2. Remove Item     │")
        print("│ 3. Search Item     │")
        print("│ 4. Sort List       │")
        print("│ 5. Display List    │")
        print("│ 6. Exit            │")
        print("└" + "─" * 40 + "┘")

        choice = input("\n  Enter choice (1-6): ")

        if choice == '1':
            item = input("  Enter item: ")
            my_list.append(item)
            print(f"  ✓ Added: {item}")
        elif choice == '2':
            if not my_list:
                print("  ⚠ List is empty!")
            else:
                item = input("  Enter item to remove: ")
                if item in my_list:
                    my_list.remove(item)
                    print(f"  ✓ Removed: {item}")
                else:
                    print(f"  ✗ Not found: {item}")
        elif choice == '3':
            if not my_list:
                print("  ⚠ List is empty!")
            else:
                item = input("  Enter item to search: ")
                if item in my_list:
                    print(f"  ✓ Found at index {my_list.index(item)}")
                else:
                    print(f"  ✗ Not found: {item}")
        elif choice == '4':
            if not my_list:
                print("  ⚠ List is empty!")
            else:
                my_list.sort()
                print("  ✓ Sorted successfully!")
        elif choice == '5':
            if not my_list:
                print("  ⚠ List is empty!")
            else:
                print("\n  Current List:")
                for i, item in enumerate(my_list):
                    print(f"    {i}. {item}")
        elif choice == '6':
            print("\n  👋 Goodbye!")
            break
        else:
            print("  ✗ Invalid choice!")
        input("\n  Press Enter...")
        clear_screen()

# Uncomment to run menu program
# menu_driven_program()

print("\n" + "═" * 70)
print("  ✓ ASSIGNMENT COMPLETED")
print("═" * 70)
print("\n  Student Name: ____________________")
print("  Roll No: ____________________")
print("  Date: ____________________\n")