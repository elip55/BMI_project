

# Function to convert kilos to lbs, since Americans are more comfortable with lbs 
def kilo_conversion(): 
    
    print("And now, lets get started on conversions, if needed.")
    answer = input("Do you need to convert kilos to lbs? y/n ")
    if answer == 'y' or answer ==' y':
        weight_kg = float(input("Please input your weight in kg "))
        weight_lbs = round(weight_kg*2.20462, 4)
        print(f"Your weight in lbs = {weight_lbs}")
    elif answer == 'n' or answer == ' n': # Bypass function 
        print("Okay, let us move along!")
    else:
        print("That is not a valid input.") # In the case that the input was invalid
        kilo_conversion()