import math 

def kilo_conversion(): # Function to convert kilos to lbs, since Americans are more comfortable with lbs 
    print("And now, lets get started on conversions, if needed.")
    answer = input("Do you need to convert kilos to lbs? y/n ")
    if answer == 'y' or answer =='Y':
        weight_kg = float(input("Please input your weight in kg "))
        weight_lbs = round(weight_kg*2.20462, 4)
        print(f"Your weight in lbs = {weight_lbs}")
    elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No': # Bypass function 
        print("Okay, let us move along!")
    else:
        print("That is not a valid input.")
        kilo_conversion()
        

def inches_conversion(): # Function to convert ft to inches 
    answer = input("Do you need to convert feet to inches? y/n ")
    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes':
        print("Okay, let's start with ft.")
        height_ft = float(input("Input your ft: "))
        print("Now, lets add inches.")
        height_in= float(input("Input your in: "))
        height_in_inches = round((height_ft*12) + height_in, 4)
        print(f"Your height in inches = {height_in_inches}")
    elif answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N': # Bypass functiton 
        print("Okay, lets move along!")
    else: 
        print("That is not a valid input.")
        inches_conversion()
        
        
def calculations(): # Final calculations 
    print("And now, lets get started on the BMI caclulations!")
    height = float(input("please input your height in inches: "))
    weight = float(input("please input your weight in lbs: "))
    BMI = round((weight/(pow(height,2)))*703,4)
    healthy_BMI_min = 18
    healthy_BMI_max= 24
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

print("This is a simple program to find your goal weight and BMI.")
goal = float(input("Let's start here, what is your goal weight, in lbs?"))
kilo_conversion()
inches_conversion()
calculations()