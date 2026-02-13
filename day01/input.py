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