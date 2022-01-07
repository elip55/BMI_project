

class BodyMassIndex:

    def __init__(self, lbs, kg, height_ft, height_in, height_cm, meters):
        self.lbs = lbs
        self.kg = kg
        self.height_ft = height_ft
        self.height_in = height_in
        self.height_cm = height_cm
        self.meters = meters
        
    def lbs_to_kg(self):
        kilos = self.lbs*0.45359237
        return kilos
    
    def cm_to_m(self):
        m = self.height_cm*0.01
        return m
    
    def ft_to_m(self):
        m = (self.height_ft*0.3048) + (self.height_in*0.0254)
        return m
    
    def bmi_calculation(self):
        bmi = round(self.kg/(self.meters**2), 4)
        return(bmi)