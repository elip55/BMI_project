
from .intro import goal
from tqdm import tqdm
import plotly.graph_objects as go

def calculations(): # Final calculations 

    print("Okay, lets get started on the BMI caclulations!")
    height = float(input("please input your height in inches: "))
    weight = float(input("please input your weight in lbs: "))
    BMI = round((weight/(pow(height,2)))*703,4)
    healthy_BMI_min = 18
    healthy_BMI_max= 24

    fig = go.Figure(data=[go.Table(header=dict(values=['Healthy BMI min', 'Healthy BMI max', 'Your BMI']),
                 cells=dict(values=[[healthy_BMI_min], [healthy_BMI_max], [BMI]]))
                     ])
    for i in tqdm(range(100)):
        pass
    fig.show()


    if BMI <= healthy_BMI_max and BMI >= healthy_BMI_min:
        print("Congrats, you are at a healthy BMI!")
    else:
        print(f"\n Remember, a healthy BMI is between {healthy_BMI_min} and {healthy_BMI_max}! You have some work to do!")
    if weight > goal: 
        print("-------------------")
        print(f"You haven't reached your weight goal of {goal}.")
        print("-------------------")
    elif weight <= goal:
        print("-------------------")
        print(f"Congrats!  You have reached your weight goal of {goal}!")
        print("-------------------")