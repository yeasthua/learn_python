from datetime import datetime  #  built-in datetime module to perform date calculations.

# Converts the user's input string (e.g. "2004-05-21") into a datetime object so it can be subtracted to today's date
# strptime() strips the string using the format YYYY-MM-DD translated into "%Y-%m-%d" using format specifiers
birthdate = datetime.strptime(input("Input your birthdate (YYYY-MM-DD): "), "%Y-%m-%d")

# Subtracts the {birthdate} from today's date, resulting in a timedelta object
current_age = datetime.today() - birthdate

# .days extracts the total number of days from the timedelta object inside the datetime module
# // 365 performs floor division to convert days into whole years
print(f"Current age: {current_age.days // 365} years old.")

# Prints the total days of {current_age} using .days 
print(f"Numbers of days lived: {current_age.days} days")
