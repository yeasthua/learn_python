# A program which asks the user for two strings and then prints out whichever is the longer of the two
# If the strings are of equal length, the program should print out "The strings are equally long".

string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

# len() returns the total number of characters in a string
if len(string1) > len(string2):
    print(f"{string1} is longer")

elif len(string1) < len(string2):
    print(f"{string2} is longer")

else:
    print("The strings are equally long")