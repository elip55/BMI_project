
from .intro import goal

# Final calculations from gathered data
def calculations(): 

    print("Okay, lets get started on the BMI caclulations!")
    height = float(input("Please input your height in inches: "))
    weight = float(input("Please input your weight in lbs: "))
    BMI = round((weight/(pow(height,2)))*703,4)
    healthy_BMI_min = 18
    healthy_BMI_max= 24
    # Display the results 
    print("-------------------")
    print(f"Your BMI = {BMI} ")
    print("-------------------")
    if BMI <= healthy_BMI_max and BMI >= healthy_BMI_min:
        print("Congrats, you are at a healthy BMI!")
    else:
        print(f"Remember, a healthy BMI is between {healthy_BMI_min} and {healthy_BMI_max}! You have some work to do!")
    if weight > goal: 
        print("-------------------")
        print(f"You haven't reached your weight goal of {goal}.")
        print("-------------------")
    elif weight <= goal:
        print("-------------------")
        print(f"Congrats!  You have reached your weight goal of {goal}!")
        print("-------------------")