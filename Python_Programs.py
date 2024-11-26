# Keanu valencia
# 11/26/24
# ICS 169
# This Python file contains a list of mini Python programs for my introductory information security class

# Program 1: Test Score Evaluator
int(input("Enter your test score: ", x))

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
