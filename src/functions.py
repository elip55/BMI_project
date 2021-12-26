

class BodyMassIndex:

    def __init__(self, lbs, kg, height_ft, height_in):
        self.lbs = lbs
        self.kg = kg
        self.height_ft = height_ft
        self.height_in = height_in

    def calculation_lbs(self): 
        kilos = self.lbs*0.45359237
        height_meters = (self.height_ft*0.3048) + (self.height_in*0.0254)
        bmi = round(kilos/(height_meters**2), 4)
        return bmi
    
    def calculation_kg(self):
        height_meters = (self.height_ft*0.3048) + (self.height_in*0.0254)
        bmi = round(self.kg/(height_meters**2), 4)
        return bmi
    
    
def main_bmi_function1():
    print("Please input your height in feet & inches")
    ft = float(input("ft: "))
    inches = float(input("in: "))
    question1 = input("Do you weigh yourself in lbs or kg? (l/k):")
    if question1 == 'l' or question1 == ' l':
        kg = 0
        lbs = float(input("Please input your weight in lbs: "))
        calculations = BodyMassIndex(lbs, kg, ft, inches)
        bmi = calculations.calculation_lbs() # bmi calculation works
    elif question1 == 'k' or question1 == ' k':
        lbs = 0
        kilos = float(input("Please input your weight in kg: "))
        kg = kilos
        calculations = BodyMassIndex(lbs, kg, ft, inches)
        bmi = calculations.calculation_kg() # bmi calculation works
    else:
        print("INVALID INPUT.  PLEASE RUN THE PROGRAM AGAIN.")
        exit()