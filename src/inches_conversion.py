
# Function to convert ft to inches, making the calculations easier 
def inches_conversion(): 

    answer = input("Do you need to convert your current height to inches? y/n ")
    if answer == 'y' or answer == ' y':
        print("Okay, let's start with ft.")
        height_ft = float(input("Input your ft: "))
        print("Now, lets add inches.")
        height_in= float(input("Input your in: "))
        height_in_inches = round((height_ft*12) + height_in, 4)
        print(f"Your height in inches = {height_in_inches}")
    elif answer == 'n' or answer == ' n': # Bypass functiton 
        print("Okay, lets move along!")
    else: 
        print("That is not a valid input.")
        inches_conversion()