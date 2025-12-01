import time
global age, height, weight  

age = int(input("Enter your age: "))
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))
waterpoints = 0.0  

def mainmenu():
    print("(1) Arithmetic Basics                                          (3) Screen Time Flag")
    print("(2) BMI Calculator                                             (4) Hydration Streak")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        arithmeticbasics()
    elif options == 2: 
        bmi()
    elif options == 3:
        screentimeflag()
    elif options == 4:
        hydrationstreak()
    elif options == 5:
        freeclass()
    
    else:
        print("Invalid option, try again.")
        mainmenu()

def arithmeticbasics():
    totalsteps = 10000
    steps = int(input("Enter amount of steps taken: "))
    percentage = steps / totalsteps * 100
    totalsteps = totalsteps - steps
    print("You have done", percentage, "% of your goal and there are", totalsteps, "steps left.")
    mainmenu()

def bmi():
    global height, weight
    bmi= weight / height ** 2
    time.sleep (1)
    if bmi<= 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("You are healthy")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")
    time.sleep (2)
    mainmenu()

def screentimeflag():
    dailyscreenminutes = int(input("How long have you spent on your screen today? "))
    steps = int(input("Enter amount of steps taken: "))
    nightscreenminutes = int(input("How long have you spent on your screen tonight? "))

    if (dailyscreenminutes > 240 and steps < 5000) or nightscreenminutes > 60:
        print("Too much screen time")
        mainmenu()

    else:
        mainmenu ()

def hydrationstreak():
    global waterpoints
    waterml = int(input("How much water have you drank today (ml)? "))
    waterpoints = waterml / 250
    extra = waterml / 2000
    waterpoints = extra * 5
    print("You have", waterpoints, "points for drinking water")
    mainmenu()


def freeclass():
    lowincomeparticipant = input("Are you considered a low-income participant? (True/False): ").strip().lower() == "true"
    freeclass30days = input("Have you received a free class in the past 30 days? (True/False): ").strip().lower() == "true"
    
    # Check eligibility
    if (16 <= age <= 25 and not freeclass30days) or (lowincomeparticipant and not freeclass30days):
        print("You are eligible for a free class!")
    else:
        print("You are not eligible for a free class.")
mainmenu()
    

mainmenu()


