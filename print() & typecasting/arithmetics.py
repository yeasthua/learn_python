# Converts input into int and use it to perform arithmetic operations
num_input = int(input("Please type in a number: "))
print(f"{num_input} times 5 is {num_input * 5}")


# A program which asks for a name and a birth year and calculates it's age at the end of 2021
name = input("What is your name? ")
birthyear = int(input("Which year were you born? "))

print(f"Hi {name}, you will be {2021 - birthyear} years old at the end of the year 2021")


#Prints the minutes in a year using arithmetic operators
print(365 * 24 * 60)    
#There are 365 days in a year multiplied (*) by 24 hours (1 day) and 60 minutes (1 hour)


#Prints the number of seconds in whatever how many days the user inputs
days = int(input("How many days? "))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")
# variable {days} x 24 hours x 60 mins x 60 seconds



# Asks the user to enter 3 numbers, then multiplies those 3
product1 = int(input("Please type in the first number: "))
product2 = int(input("Please type in the second number: "))
product3 = int(input("Please type in the third number: "))

print(f"The product is {product1 * product2 * product3}")



# Asks the user for two numbers. Then prints out the sum and the product of the two numbers.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")



# Asks for 4 numbers, then prints the sum and it's mean
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
num4 = int(input("Number 4: "))
sum = num1 + num2 + num3 + num4

print(f"The sum of the numbers is {sum} and the mean is {sum / 4}")