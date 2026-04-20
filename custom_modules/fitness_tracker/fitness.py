# Function definitions of fitness.py module

def calculate_bmi(weight, height):
    result =  weight / height ** 2
    rounded = round(result, 2)
    if result >= 25:
        return f"Your BMI is: {rounded}, Overweight"
    elif result >= 18.5:
        return f"Your BMI is: {rounded}, Normal weight"
    else:
        return f"Your BMI is: {rounded}, Underweight"


def goal_status(steps):
    if steps >= 10000:
        return "Goal Reached"
    else:
        return "Keep Going"
    

    