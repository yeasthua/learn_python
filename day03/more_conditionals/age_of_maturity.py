# A program which asks the user for their age.
# The program then prints out a message based on whether the user is of age or not, using 18 as the age of maturity.

age = int(input("How old are you? "))

if age >= 18:                   # Runs if age is greater than or equal to 18.
    print("You are of age!")

else:                           # Otherwise this block will run.
    print("You are not of age!")
