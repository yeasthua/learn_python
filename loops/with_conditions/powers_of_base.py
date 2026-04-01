# Similar program to "power_of_two.py" but this time, the user can input the desired base multiplier

limit = int(input("Upper limit: "))
multiplier = int(input("Base: "))       # Allows the user to set the base which is multiplied to the number
number = 1

while number <= limit:
    print(number)
    number *= multiplier