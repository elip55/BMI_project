

from src.classes import BodyMassIndex
    
    
def data():
    throwaway = 0
    healthy_bmi = range(18, 26)
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
    
    # calculate bmi with gathered data
    calc_bmi = BodyMassIndex(throwaway, kg_weight, throwaway, throwaway, throwaway, meter_height) # lbs, kg, height_ft, height_in, height_cm, meters
    bmi = calc_bmi.bmi_calculation()
    rounded_bmi = round(bmi,0) # temporary fix
    if rounded_bmi in healthy_bmi:
        print(f'Your bmi is: {bmi}\nThis is within the healthy range')
    elif rounded_bmi not in healthy_bmi:
        print(f'Your bmi is: {bmi}\nRemember, a healthy range is 18-25, you have some work to do!')
    