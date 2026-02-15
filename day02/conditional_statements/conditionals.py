# Simple if block
number = int(input("Please type in a number: "))

if number == 1984:      # == means equals to
    print("You won the lotto!")


# Absolute value program
number = int(input("Please type in a number: "))

if number < 0:
    print(f"The absolute value of this number is {number * -1}")

if number >= 0:
    print(f"The absolute value of this number is {number * 1}")


# If block skips if "Jerry" was input by the user
name = input("Please tell me your name: ")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    price = 5.90
    print(f"The total cost is {price * portions}")
    print("Next please!")

print("Next please!")


# Order of magnitude program
number = int(input("Please type in a number: "))

if number < 1000:
    print("This number is smaller than 1000")

if number < 100:
    print("This number is smaller than 100")

if number < 10:
    print("This number is smaller than 10")

print("Thank you!")



