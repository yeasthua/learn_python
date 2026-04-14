# A program which asks the user for a string and an amount.
# The program then prints out the string as many times as specified by the amount in one line and no spaces.

word = input("Please type in a string: ")
repeat = int(input("Please type in an amount: "))

print(word * repeat)    # The string is repeated by the number inside {repeat}