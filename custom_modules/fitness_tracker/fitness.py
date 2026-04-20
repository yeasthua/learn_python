# Function definitions of fitness.py module

def calculate_bmi(weight, height):
    result =  weight / height ** 2
    rounded = round(result, 2)
    if result >= 95:
        print(f"Your BMI is: {rounded}, Overweight")
    elif result >= 85:
        print(f"Your BMI is: {rounded}, At risk of overweight")
    elif result >= 5:
        print(f"Your BMI is: {rounded}, Normal weight")
    else:
        print(f"Your BMI is: {rounded},  Underweight")


def goal_status(steps):
    if steps >= 10000:
        print("Goal Reached")
    else:
        print("Keep Going")
    

    