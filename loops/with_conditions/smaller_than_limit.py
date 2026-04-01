# A program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

limit = int(input("Upper limit: "))
increment = 1

while increment < limit:        # Assures that all numbers that will be printed are greater than 0
    print(increment)
    increment += 1              # Increments by 1 so the loop will eventually comes to a stop