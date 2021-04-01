
# Function to convert ft to inches, making the calculations easier 
def inches_conversion(): 
    
    print("To utilize the formula corectly, we need to convert your height to inches.")
    answer_convert_cm = input("Do you need to convert your height in cm to strictly inches? y/n")
    if answer_convert_cm == 'y' or answer_convert_cm == ' y':
        height_cm = float(input("Input your height in cm: "))
        height_cm_to_in = round(height_cm/2.54, 4)
        print(f"Your height in cm = {height_cm_to_in}")
    else:
        ft_conversion = input("Do you need to convert your current height in (ft,inches) to stricly inches? y/n ")
        if ft_conversion  == 'y' or ft_conversion  == ' y':
            print("Okay, let's start with ft.")
            height_ft = float(input("Input your ft: "))
            print("Now, lets add inches.")
            height_in= float(input("Input your in: "))
            height_in_inches = round((height_ft*12) + height_in, 4)
            print(f"Your height in inches = {height_in_inches}")
        elif ft_conversion  == 'n' or ft_conversion  == ' n': # Bypass functiton 
            print("Okay, lets move along!")
        else: 
            print("That is not a valid input.")
            inches_conversion()