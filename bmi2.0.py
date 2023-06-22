height = float(input("What is your height in m? "))
weight = float(input("What is your weight in kg? "))
bmi = weight / (height**2)
if bmi<18.5:
    print("Your bmi is ",round (bmi, 2),"and you are under weight")
if bmi>25.0:
    print("Your bmi is ",round(bmi, 2), "and you are over weight")
else:
    print("Your bmi is ",round(bmi,2), "and you are normal weight")
