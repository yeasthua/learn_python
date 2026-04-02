# A program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
# until the sum is at least equal to the limit set by the user.

limit = int(input("Limit: "))
num = 0
sum = 0
while sum < limit:
    #print("Loop runs")

    num += 1        # Increments num by one each iteration and stores it

    #print("num:", num)

    sum += num      # Increments sum by the value of num per iteration and stores it.

    #print(f"sum: {sum} \n")

print(sum) 