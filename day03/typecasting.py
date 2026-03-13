# A program which asks the user for a floating point number 
# and then prints out the integer part and the decimal part separately.

number = float(input("Please type in a number: "))

print(f"Integer part: {int(number)}")            # Prints the integer number inputted by the user
print(f"Decimal part: {number - int(number)}")     # Prints the decimal version of the number