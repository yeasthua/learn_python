number = int(input("Please type in a number: "))

print( "condition: ", number > 100)         # Checks if the number inputted is greater than 100
if number > 100:
    print("The number was greater than one hundred")
    print("Original number: ", number)      # Prints the original number
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)       # Prints the number decreased by 100

print(number, "must be my lucky number!")
print("Have a nice day!")