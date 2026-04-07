# A new version of the program in the previous exercise (consecutive_numbers.py). 
# In addition to the result it should also print out the calculation performed

limit = int(input("Limit: "))
num = 0
sum = 0
result = ""        # For storing strings
while sum < limit:

    num += 1 
    result += f"{num} + "      # Appending a new text every iteration and storing it inside {result}
    sum += num

result = result[:-2]    # String slicing, removing the last two index of the string ("+ ") using negative indexing
print(f"The consecutive sum: {result}= {sum}")
