

print("This is a simple program to find your goal weight and BMI.")
try:
    goal = float(input("Before we start calculating, what is your goal weight, in lbs?"))
except:
    print("Not a valid input, try again.")
finally: 
    goal = float(input("Before we start calculating, what is your goal weight, in lbs?"))
