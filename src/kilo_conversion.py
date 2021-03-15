


def kilo_conversion(): # Function to convert kilos to lbs, since Americans are more comfortable with lbs 
    print("And now, lets get started on conversions, if needed.")
    answer = input("Do you need to convert kilos to lbs? y/n ")
    if answer == 'y' or answer ==' y':
        weight_kg = float(input("Please input your weight in kg "))
        weight_lbs = round(weight_kg*2.20462, 4)
        print(f"Your weight in lbs = {weight_lbs}")
    elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No': # Bypass function 
        print("Okay, let us move along!")
    else:
        print("That is not a valid input.")
        kilo_conversion()