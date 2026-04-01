# A program which asks the user to type in an upper limit. 
# The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. 
# That is, the program prints out powers of two in order.

limit = int(input("Upper limit: "))
power = 1

while power <= limit:
    print(power)
    power *= 2      # Increments {power} by multiplying the value by 2 and storing it inside {power}