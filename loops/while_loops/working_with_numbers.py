print("Please type in integer numbers. Type in 0 to finish.")

inputs = 0
sum = 0
positive = 0
negative = 0 
while True:
    numbers = int(input("Number: "))

    if numbers == 0:
        break
    # Increment is positioned here so when the loop breaks, it doesn't count the "0" input
    inputs += 1     # Serves as a tracker of how many times the loop runs (not including 0)
    sum += numbers   # Stores each value the {number} has, into the {sum} variable

    if numbers > 0:
        positive += 1

print(f"Numbers typed in {inputs}")
print(f"The sum of the numbers is {sum}")
print("The mean of the numbers is", sum/inputs)
print(f"Positive numbers {positive}")
print(f"Negative numbers {inputs - positive}")  

