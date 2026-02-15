# Simple calculator using if blocks
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation:")

if operation == "add" or operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

if operation == "multiply" or operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

if operation == "subtract" or operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
    