def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("BMI = ", bmi)
    if bmi < 18.5:
        print("Your bmi is ", bmi, "and you are under weight")
        return -1
    if bmi > 25.0:
        print("Your bmi is " , bmi , "and you are over weight")
        return 1
    else:
        print("your bmi is " , bmi , "and you are normal weight")
        return 0



x=  calculate_bmi(weight=57,height=1.73)
print(x)



