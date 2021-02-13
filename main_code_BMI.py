import math 

def kilo_conversion():
    answer = input("Do you need to convert kilos to lbs? y/n ")
    if answer == 'y' or answer =='Y':
        weight_kg_eli = float(input("Please input your weight in kg "))
        weight_lbs_eli = weight_kg_eli*2.20462
        print("Weight in lbs = ")
        print(weight_lbs_eli)
    else: 
        print("Okay, let us move along!")

def inches_conversion():
    answer = input("Do you need to convert feet to inches? y/n ")
    if answer == 'y' or answer == "Y":
        print("Okay, let's start with ft: ")
        height_ft_eli = float(input("Input your ft: "))
        height_in_eli = float(input("Input your in: "))
        height_in_in_eli = (height_ft_eli*12) + height_in_eli
        print("Your height in inches = ")
        print(height_in_in_eli)
    else: 
        print("Okay, lets move along!")

def calculations_eli():
    print("And now, lets get started on the BMI caclulations!")
    height_eli = float(input("Eli, please intput your height in inches: "))
    weight_eli = float(input("Eli, please input your weight in lbs: "))
    BMI_eli = (weight_eli/(pow(height_eli,2)))*703
    healthy_BMI_min_eli = 18
    healthy_BMI_max_eli = 24
    print("Eli, your BMI = ")
    print(BMI_eli)

    if BMI_eli <= healthy_BMI_max_eli and BMI_eli >= healthy_BMI_min_eli:
        print("Congrats, you are at a helthy BMI!")
    else:
        print("You have some work to do.")
        
kilo_conversion()
inches_conversion()
calculations_eli()