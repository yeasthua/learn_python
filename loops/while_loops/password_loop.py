# Asks the user to enter a password 
# and the program should keep on asking until the user types the first password again correctly.

password = input("Password: ")

while True:

    retry = input("Repeat password: ")

    if retry == password:
        break

    print("They do not match!")

print("User account created!")