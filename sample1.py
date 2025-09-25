"""
sample1.py
Author: Jacob Catayoc
Date:   September 11, 2025
"""
name = input("What is your name? ")
age = input("How old are you? ")
color = input("What is your favourite color? ")

# Method 1: String concatenation
print("Hello " + name + "!")
print("You are " + age + " years old.")
print("Your favorite color is " + color)

# Method 2: String interpolation
print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"Your favourite color is {color}")

# Method 3: Using , in print()
print("Hello", name, "!")
print("You are", age, "years old.")
print("Your favorite color is", color)