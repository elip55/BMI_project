import math 

def kilo_conversion():
    answer = input("Do you need to convert kilos to lbs? y/n ")
    
    if answer == 'y' or answer =='Y':
        weight_kg_eli = float(input("Please input your weight in kg "))
        weight_lbs_eli = round(weight_kg_eli*2.20462, 4)
        print(f"Your weight in lbs = {weight_lbs_eli}")
    
    elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No': 
        print("Okay, let us move along!")
    
    else:
        print("That is not a valid input.")
        kilo_conversion()
        

def inches_conversion():
    answer = input("Do you need to convert feet to inches? y/n ")
    
    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes':
        print("Okay, let's start with ft.")
        height_ft_eli = float(input("Input your ft: "))
        print("Now, lets add inches.")
        height_in_eli = float(input("Input your in: "))
        height_in_in_eli = round((height_ft_eli*12) + height_in_eli, 4)
        print(f"Your height in inches = {height_in_in_eli}")
    
    elif answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N':
        print("Okay, lets move along!")
    
    else: 
        print("That is not a valid input.")
        inches_conversion()
        
def calculations_eli():
    
    print("And now, lets get started on the BMI caclulations!")
    height_eli = float(input("please intput your height in inches: "))
    weight_eli = float(input("please input your weight in lbs: "))
    BMI_eli = round((weight_eli/(pow(height_eli,2)))*703,4)
    healthy_BMI_min_eli = 18
    healthy_BMI_max_eli = 24
    print(f"your BMI = {BMI_eli} ")
    
    if BMI_eli <= healthy_BMI_max_eli and BMI_eli >= healthy_BMI_min_eli:
        print("Congrats, you are at a healthy BMI!")
    
    else:
        print("You have some work to do.")
        
kilo_conversion()
inches_conversion()
calculations_eli()