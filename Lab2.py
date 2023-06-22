def display_main_menu():
    print("enter some numbers seperated by commas ")

def calc_average(float_list):
    y = sum(float_list)/len(float_list)
    return y

    x=input().split(",")
    y=[]
    for i in x:
        y.append(float(i))
    return y

def find_min_max(float_list):   
    minimum=min(float_list)
    maximum=max(float_list)
    print("The minimum value is ",minimum)
    print("The maximum value is ",maximum)

def sort_temp():
    print("sort_temp")
def calc_median_temp():
    print("calc_median_temp")
def calc_bmi():
    height = float(input("What is your height in m? "))
    weight = float(input("wWhat is your weight in kg? "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Your bmi is ", round(bmi, 2), "and you are under weight")
    if bmi > 25.0:
        print("Your bmi is ", round(bmi, 2), "and you are over weight")
    else:
        print("Your bmi is ", round(bmi, 2), "and you are normal weight")





