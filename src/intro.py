from .colors import bcolors

print("This is a simple program to find your goal_weight weight and BMI.")

# Attain the users goals to congratulate them when they reach their goals
try:
    goal_weight = float(input("Before we start calculating, what is your goal_weight weight, in lbs?"))
    goal_BMI = float(input("What is your goal BMI?"))
except: 
    print(bcolors.FAIL + "INVALID: Goal weight should be an integer, please run the program again." + bcolors.ENDC)


