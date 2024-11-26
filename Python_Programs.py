# Keanu valencia
# 11/26/24
# ICS 169
# This Python file contains a list of mini Python programs for my introductory information security class

# Program 1: Test Score Evaluator
x = int(input("Enter your test score: "))

if x >= 90:
  print("You passed the test with an A! Keep up the good work!")
elif x >= 80 and x <= 89:
  print("You passed the test with a B! Keep up the good work!")
elif x >= 70 and x <= 79:
  print("You passed the test with a C! Lets strive for a B or A next time!")
elif x >= 60 and x <= 69:
  print("You passed the test with a D! Keep trying your best!")
else:
  print("You got an F. Please see me after class.")

# Program 2: Simple Calculator
def cal(val_1, val_2, ope):
  if ope == "Add" or ope == "add":
    print(val_1 + val_2)
  elif ope == "Subtract" or ope == "subtract":
    print(val_1 - val_2)
  elif ope == "Multiply" or ope == "multiply":
    print(val_1 * val_2)
  elif ope == "Divide" or ope == "divide":
    print(val_1 / val_2)
  else:
    print("Invalid operation")

cal(val_1 = 100, val_2 = 10, ope = "divide")

#Program 3: Number Printer
def binary_generator(length):
  for i in range (2 ** length):
    binary_str = f"{i:0{length}b}"
    print(binary_str)

binary_generator(length=100) # It looks like your mining for bitcoin, Hahaha.
