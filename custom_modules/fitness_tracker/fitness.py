# Function definitions of fitness.py module

def calculate_bmi(weight, height):
    result =  weight / height ** 2
    return result

def goal_status(steps):
    if steps >= 10000:
        return "Goal Reached"
    else:
        return "Keep Going"
    

    