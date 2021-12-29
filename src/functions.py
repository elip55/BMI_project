

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
    
    
def main_function():
    throwaway = 0
    
    # height
    height_measurement_pref = input("Do you measure yourself if cm, m, or ft & in? (cm/m/ft): ")
    if height_measurement_pref == "cm" or height_measurement_pref == ' cm':
        cm_height = float(input("Please input your height in cm: "))
        calc_cm = BodyMassIndex(throwaway, throwaway, throwaway, throwaway, cm_height, throwaway)
        meter_height = calc_cm.cm_to_m() # conversion works
    if height_measurement_pref == 'ft' or height_measurement_pref == ' ft': 
        ft = int(input("Please input your height\nft: "))
        inch = float(input("in: "))
        calc_ft = BodyMassIndex(throwaway, throwaway, ft, inch, throwaway, throwaway)
        meter_height = calc_ft.ft_to_m()
    if height_measurement_pref == 'm' or height_measurement_pref == ' m':
        meter_height = float(input("Please input your height in meters: "))
    
    # weight
    weight_measurement_pref = input("Do you weigh yourself in lbs or kg? (l/k):")
    if weight_measurement_pref == 'l' or weight_measurement_pref == ' l':
        lbs = float(input("Please input your weight in lbs: "))
        calc_lbs = BodyMassIndex(lbs, throwaway, throwaway, throwaway, throwaway, throwaway)
        kg_weight = calc_lbs.lbs_to_kg()
    if weight_measurement_pref == 'k' or weight_measurement_pref == ' k':
        kg_weight = float(input("Please input your weight in kg: "))
    