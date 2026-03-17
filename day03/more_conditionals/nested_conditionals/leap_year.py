# A  program which asks the user for a year, and then prints out whether that year is a leap year or not.

year = int(input("Please type in a year: "))

# If the year is divisible by 4 and divisible by 100 and 400
if year % 4 == 0 and year % 400 == 0:
    print("That year is a leap year.")

# If the year is ONLY divisible by 4 and not divisible by 100
elif year % 4 == 0 and year % 100 != 0:
    print("That year is a leap year.")

else:
    print("That year is not a leap year.")



# ALTERNATIVE SOLUTION

#   Assumes that a year is not a leap year
# leap_year = False
# if num % 100 == 0:
#     if num % 400 == 0:
#         leap_year = True

# elif num % 4 == 0:
#     leap_year = True

# if leap_year:
#     print("That year is not a leap year.")
# else:
#     print("That year is a leap year.")

    