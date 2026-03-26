# A program which asks the user for a year, and prints out the next leap year.

year = int(input("Year: "))
lyear = year    # Create a separate variable to increment so we preserve the original year
while True:
    lyear += 1  # Increment inside the loop to prevent it resetting to the year's original value
    
    # Exits the loop if the rule of leap year is met
    if (lyear % 4 == 0 and lyear % 100 != 0) or lyear % 400 == 0:
        break

print(f"The next leap year after {year} is {lyear}")
