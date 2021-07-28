


from colors import bcolors


print("This is a simple program to find your goal weight and BMI.")

# Attain the users goals to congratulate them when they reach their goals
try:
    goal_weight = float(input("Before we begin, what is your goal weight in kg? "))
    goal_BMI = float(input("What is your goal BMI? "))
except: 
    print(bcolors.FAIL + "ERROR: Goal weight should be an integer, please run the program again." + bcolors.ENDC)
    exit()

def calc1():
    global m
    print("Okay, lets get started!\nWe need to ask a few questions before we can calculate.")
    q1 = input('Do you need to convers ft and inches into meters? (y/n) ')

    if q1 == 'y' or q1 == ' y':
        ft = float(input("Please input height in: ft: "))
        inches = float(input("Please input height in: in: "))
        m = (ft*0.3048) + (inches*0.0254)   
    elif q1 == 'n' or q1 == ' n':
        answ1 = float(input("Input your height in meters: "))
        m = answ1
    else: 
        print(bcolors.FAIL + "INVALID INPUT" +  bcolors.ENDC)
        calc1()

def calc2():
    global kg
    q2 = input("Great!\nDo you need to convert lbs to kg? (y/n) ")
    if q2 == 'y' or q2 == ' y':
        lbs = float(input("How much do you weigh, in lbs: "))
        kg = lbs*0.453592
    elif q2 == 'n' or q2 == ' n':
        answ2 = float(input("Input your weight in kg: "))
        kg = answ2
    else: 
        print(bcolors.FAIL + "INVALID INPUT" +  bcolors.ENDC)
        calc2()

def calc3():
    calc1()
    calc2()
    bmi = kg/(m**2)
    print(f'Your weight in kg is: {kg}')
    print(f'Your BMI is: {bmi}')
    if bmi <= goal_BMI:
        print(bcolors.OKBLUE + 'Congrats! You have reached your goal!' + bcolors.ENDC)
    else: 
        print(bcolors.FAIL + 'You have not reached your goal' + bcolors.ENDC)
    if kg <= goal_weight:
        print(bcolors.OKBLUE + 'Congrats! You have reached your goal!' + bcolors.ENDC)
    else: 
        print(bcolors.FAIL + 'You have not reached your goal' + bcolors.ENDC)

calc3()
