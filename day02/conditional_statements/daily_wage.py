hourly_wage = float(input("Hourly wage: "))
hours_work = float(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    # double pay on sunday
    # overwrites hourly_wage if the condition is true
    hourly_wage = float(hourly_wage * 2)

# prints the final daily pay
daily_pay = float(hourly_wage * hours_work)
print("Daily wages:", daily_pay, "euros")