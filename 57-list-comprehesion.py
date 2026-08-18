# Theory about this code:

# This code demonstrates Python List Comprehension through a collection of practical examples and exercises.
# It shows how to create lists, calculate squares and cubes, filter numbers, and modify strings using concise syntax.
# Conditional comprehensions are used to find positive numbers, even numbers, divisible numbers, and specific words.
# The code also covers advanced examples such as flattening nested lists, matrix transposition, and creating tuples.
# It compares traditional for loops with list comprehensions and measures their execution time.
# Overall, the program provides a complete practice of list comprehension for writing shorter, cleaner, and efficient Python code.




print("="*70)
print("LIST COMPREHENSION ASSIGNMENT - COMPLETE SOLUTIONS")
print("="*70)

print("\n#############################################################################\n")

print("\n" + "="*50)
print("PART A: BASIC QUESTIONS")
print("="*50)

print("\n#############################################################################\n")

print("\n Numbers from 1 to 10:")
numbers_1_to_10 = [x for x in range(1, 11)]
print(numbers_1_to_10)

print("\n#############################################################################\n")

print("\n Squares of numbers from 1 to 10:")
squares = [x**2 for x in range(1, 11)]
print(squares)

print("\n#############################################################################\n")

print("\n Cubes of numbers from 1 to 10:")
cubes = [x**3 for x in range(1, 11)]
print(cubes)

print("\n#############################################################################\n")

print("\n Even numbers from 1 to 20:")
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

print("\n#############################################################################\n")

print("\n Odd numbers from 1 to 20:")
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print(odd_numbers)

print("\n#############################################################################\n")

print("\n" + "="*50)
print("PART B: CONDITIONAL LIST COMPREHENSION")
print("="*50)

print("\n#############################################################################\n")

print("\n Numbers greater than 20:")
numbers = [5, 12, 25, 30, 18, 45, 10, 60]
greater_than_20 = [x for x in numbers if x > 20]
print(f"Original: {numbers}")
print(f"Greater than 20: {greater_than_20}")

print("\n#############################################################################\n")

print("\n Only positive numbers:")
nums = [-5, 10, -8, 15, 20, -3, 7]
positive_numbers = [x for x in nums if x > 0]
print(f"Original: {nums}")
print(f"Positive numbers: {positive_numbers}")

print("\n#############################################################################\n")


print("\n Words in uppercase:")
words = ["python", "java", "c++", "javascript"]
uppercase_words = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {uppercase_words}")

print("\n#############################################################################\n")

print("\n Length of each word:")
words = ["apple", "banana", "grapes", "kiwi"]
word_lengths = [len(word) for word in words]
print(f"Words: {words}")
print(f"Lengths: {word_lengths}")

print("\n#############################################################################\n")

print("\n Numbers divisible by 3:")
divisible_by_3 = [x for x in range(1, 21) if x % 3 == 0]
print(divisible_by_3)

print("\n#############################################################################\n")

print("\n" + "="*50)
print("PART C: STRING PRACTICE")
print("="*50)

print("\n#############################################################################\n")

print("\n Characters of 'PYTHON':")
word = "PYTHON"
characters = [char for char in word]
print(f"Word: {word}")
print(f"Characters: {characters}")

print("\n#############################################################################\n")

print("\n Remove all vowels from 'Programming':")
word = "Programming"
vowels = 'aeiouAEIOU'
without_vowels = [char for char in word if char not in vowels]
print(f"Original: {word}")
print(f"Without vowels: {''.join(without_vowels)}")

print("\n#############################################################################\n")

print("\n" + "="*50)
print("PART D: MIXED PRACTICE")
print("="*50)

print("\n#############################################################################\n")

print("\n Squares of even numbers from 1 to 20:")
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)

print("\n#############################################################################\n")

print("\n Words with more than 5 letters:")
fruits = ["apple", "banana", "kiwi", "watermelon", "orange", "pear"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(f"Original: {fruits}")
print(f"Words with > 5 letters: {long_fruits}")

print("\n#############################################################################\n")

print("\n Replace negative numbers with 0:")
numbers = [-5, 10, -3, 8, -1, 15]
positive_or_zero = [x if x > 0 else 0 for x in numbers]
print(f"Original: {numbers}")
print(f"Modified: {positive_or_zero}")

print("\n#############################################################################\n")

print("\n" + "="*50)
print("BONUS CHALLENGE")
print("="*50)

print("\n#############################################################################\n")

print("\n Multiplication table of 5:")
table_of_5 = [5 * x for x in range(1, 11)]
print(table_of_5)

print("\n#############################################################################\n")

print("\n Numbers divisible by 5 AND 7 (1 to 50):")
divisible_by_5_and_7 = [x for x in range(1, 51) if x % 5 == 0 and x % 7 == 0]
print(divisible_by_5_and_7)

print("\n#############################################################################\n")

divisible_by_5_or_7 = [x for x in range(1, 51) if x % 5 == 0 or x % 7 == 0]
print(f"Divisible by 5 OR 7: {divisible_by_5_or_7}")

print("\n#############################################################################\n")

print("\n First letter of each word:")
names = ["Ali", "Ahmed", "Sara", "Fatima", "Usman"]
first_letters = [name[0] for name in names]
print(f"Names: {names}")
print(f"First letters: {first_letters}")

print("\n#############################################################################\n")

print("\n" + "="*50)
print("EXTRA PRACTICE EXAMPLES")
print("="*50)

print("\n#############################################################################\n")

print("\n Flatten a nested list:")
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested for num in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

print("\n#############################################################################\n")

print("\n List of (number, square) tuples:")
number_square_pairs = [(x, x**2) for x in range(1, 6)]
print(number_square_pairs)

print("\n#############################################################################\n")

print("\n Matrix Transpose:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original Matrix: {matrix}")
print(f"Transpose: {transpose}")

print("\n#############################################################################\n")

print("\n Words starting with 'S':")
words = ["Sun", "Moon", "Star", "Sky", "Ocean", "Sea"]
words_starting_s = [word for word in words if word.startswith('S')]
print(f"Words: {words}")
print(f"Words starting with 'S': {words_starting_s}")

print("\n#############################################################################\n")

print("\n Common elements between two lists:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Common elements: {common}")

print("\n#############################################################################\n")

print("\n" + "="*50)
print("COMPARISON: Traditional Loop vs List Comprehension")
print("="*50)

print("\n#############################################################################\n")

print("\nTraditional Loop:")
squares_loop = []
for i in range(1, 11):
    squares_loop.append(i**2)
print(f"Squares: {squares_loop}")

print("\n#############################################################################\n")

print("\nList Comprehension:")
squares_comp = [i**2 for i in range(1, 11)]
print(f"Squares: {squares_comp}")

import time

start = time.time()
squares_loop = []
for i in range(1, 1000001):
    squares_loop.append(i**2)
end = time.time()
loop_time = end - start

start = time.time()
squares_comp = [i**2 for i in range(1, 1000001)]
end = time.time()
comp_time = end - start

print(f"\nPerformance (1,000,000 iterations):")
print(f"Traditional Loop: {loop_time:.4f} seconds")
print(f"List Comprehension: {comp_time:.4f} seconds")
print(f"List Comprehension is {(loop_time/comp_time):.2f}x faster!")

print("\n" + "="*70)
print("ASSIGNMENT COMPLETED SUCCESSFULLY")
print("="*70)

print("\nSUMMARY OF ALL SOLUTIONS:")
print("-"*70)
print("Part A: Basic List Comprehension")
print("  ✓ Q1: Numbers 1-10")
print("  ✓ Q2: Squares of 1-10")
print("  ✓ Q3: Cubes of 1-10")
print("  ✓ Q4: Even numbers 1-20")
print("  ✓ Q5: Odd numbers 1-20")
print("\nPart B: Conditional List Comprehension")
print("  ✓ Q6: Numbers > 20")
print("  ✓ Q7: Positive numbers")
print("  ✓ Q8: Uppercase words")
print("  ✓ Q9: Word lengths")
print("  ✓ Q10: Divisible by 3")
print("\nPart C: String Practice")
print("  ✓ Q11: Characters of word")
print("  ✓ Q12: Remove vowels")
print("\nPart D: Mixed Practice")
print("  ✓ Q13: Squares of even numbers")
print("  ✓ Q14: Words > 5 letters")
print("  ✓ Q15: Replace negatives with 0")
print("\nBonus Challenge:")
print("  ✓ Q16: Multiplication table of 5")
print("  ✓ Q17: Divisible by 5 and 7")
print("  ✓ Q18: First letters of names")
print("-"*70)

print("\n" + "="*70)