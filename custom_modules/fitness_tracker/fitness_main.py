import fitness  # Imports fitness.py to access its functions

# Stores user inputs onto their own variables
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))
steps_walked = int(input("Enter your total steps: "))

# Displays the functions inside fitness.py and use the user inputs as the functions arguments
fitness.calculate_bmi(weight, height)
fitness.goal_status(steps_walked)