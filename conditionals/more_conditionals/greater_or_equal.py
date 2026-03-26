# A program which asks for two integer numbers. The program then prints out whichever is greater.
# If the numbers are equal, the program prints a different message.

first_num = int(input("Please type in the first number: "))
second_num = int(input("Please type in another number: "))

if first_num > second_num:
    print("The greater num was:", first_num)

elif second_num > first_num:
    print("The greater num was:", second_num)

else:
    print("The numbers are equal!")