
# Food expenditure calculator
meals_per_week= float(input("How many times a week do you eat at the student cafeteria?"))
lunch_cost = float(input("The price of a typical student lunch?"))
groceries_per_week = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure:")
print(f"Daily: {(lunch_cost * meals_per_week + groceries_per_week) / 7 } euros")
# divided by 7 because 7 days a week
print(f"Weekly: {(lunch_cost * meals_per_week) + (groceries_per_week * 4) / 4} euros")
# multiplied by 4 because there are 4 weeks per month and divided by 4 because of the same reason