# A  program which asks the user for three letters.
# The program should then print out whichever of the three letters would be in the middle
# if the letters were in alphabetical order.

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")


# Case 1: [second - FIRST - third]   OR   [third - FIRST - second]
if (first > second and first < third) or (first < second and first > third):
    print(f"The letter in the middle is {first}")

# CASE 2: [first - SECOND - third]  OR  [third - SECOND - first]
elif (second > first and second < third) or (second < first and second > third):
    print(f"The letter in the middle is {second}")

# ELSE CASE: [first - THIRD - second]   OR  [second - THIRD - first]
else:
    print(f"The letter in the middle is {third}")
