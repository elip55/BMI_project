# color options
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'



class BodyMassIndex:

    def __init__(self, ft, inches, weight):
        self.v1 = ft # ft -> cm
        self.v2 = inches # in -> None
        self.v3 = weight # lbs -> kg

    def bald_eagle_cals(self):
        conversion1 = self.v1*12
        inches = conversion1 + self.v2
        inches = inches**2
        formula = (self.v3/inches)*703
        return round(formula, 4)
    
    def metric_cals(self):
        squared = self.v1**2
        formula = self.v3/squared
        return round(formula, 4)

def bald_eagle():
    healthy_bmi = range(18, 26)
    print('What is your height?\n')
    ft = int(input('ft: '))
    inch = float(input('in: '))
    print('What is your current weight?')
    weight = float(input('lbs: '))
    b = BodyMassIndex(ft, inch, weight)
    bmi = b.bald_eagle_cals()
    if bmi in healthy_bmi:
        print(f'Your bmi is {bmi}, good job!')
    else:
        print(f'Your bmi is {bmi}, you have work to do')
    


def metric():
    healthy_bmi = range(18, 26)
    print('What is your height?\n')
    cm = float(input('cm: '))
    kg = float(input('kg: '))
    b = BodyMassIndex(cm, None, kg)
    bmi = b.metric_cals()
    if bmi in healthy_bmi:
        print(f'Your bmi is {bmi}, good job!')
    else:
        print(f'Your bmi is {bmi}, you have work to do')