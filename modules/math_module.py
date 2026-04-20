import math     # Imports the built-in math module to access mathematical functions

num = float(input("Enter a number: "))

sq_root = math.sqrt(num)        # computes the square root of a number
ceiling = math.ceil(num)        # rounds the number UP to the nearest whole number
flr = math.floor(num)           # rounds the number DOWN to the nearest whole number
fact = math.factorial(int(num)) # computes the product of all positive integers up to num

# Displays the variables onto the console
print(f"Square root: {round(sq_root, 3)}")
print(f"Ceiling: {ceiling}")
print(f"Floor: {flr}")
print(f"Factorial: {fact}")