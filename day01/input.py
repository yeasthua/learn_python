# Prompts the user to type and stores it to variable "student"
# then prints the variable
student = input("Enter your name: ")
print("Oh hello there! " + student)

# Concatenating a variable and a text into a single string
name = input("What is your name? ")
print("!" + name + "!" + name + "!")

# Using multiple variables for storing multiple inputs
name = input("Given name: ")
family_name = input("Family name: ")
address = input("Street address: ")
postal_code = input("City and postal code: ")

print(name + " " + family_name)
print(address)
print(postal_code)

# Storing inputs in their variables for utterances
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")