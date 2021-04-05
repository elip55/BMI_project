
from .colors import bcolors
from .intro import goal
import csv

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
        print(bcolors.OKBLUE + "\n Congrats, you are at a healthy BMI!" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + f"\n Remember, a healthy BMI is between {healthy_BMI_min} and {healthy_BMI_max}! You have some work to do!" + bcolors.ENDC)
    if weight > goal: 
        print("-------------------")
        print(bcolors.FAIL + f"\n You haven't reached your weight goal of {goal}." + bcolors.ENDC)
        print("-------------------")
    elif weight <= goal:
        print("-------------------")
        print(bcolors.OKBLUE + f"\n Congrats!  You have reached your weight goal of {goal}!" + bcolors.ENDC)
        print("-------------------")
    
    # This option will save an excel formatted file for records
    csv_option = input("Would you like to generate an excel file for your records? y/n ")
    if csv_option == 'y' or csv_option == ' y':
        rowlist = [[" ", "WEIGHT", "BMI"],
                ["LOW", " ", healthy_BMI_min],
                ["HIGH", " ", healthy_BMI_max],
                ["GOAL", goal, " "],
                ["ACTUAL", weight, BMI]]
                
        with open('results.csv', 'w') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerows(rowlist)
    else: 
        print("Thank you for visitng my program!")