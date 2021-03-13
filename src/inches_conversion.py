

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