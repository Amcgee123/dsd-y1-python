def start():
    print("vital sighns monitor")
    temp = float(input("what is your temperature in C "))
    oxygen = int(input("what is your Oxygen blood %"))
    heart = int(input("what is your heartrate"))
    
    temp_check(temp)
    oxygen_check(oxygen)
    heart_check(heart)
    
def temp_check(temp):
    if temp > 37.5:
        print("high temperature")
    else:
        print("tempareature good")

def oxygen_check(oxygen):
    if oxygen < 92:
        print("low oxygen")
    else:
        print("oxygen good")

def heart_check(heart):
    if 60 <= heart <= 100:
        print("heart rate normal")
    else:
        print("heart rate abnormal")

start()
