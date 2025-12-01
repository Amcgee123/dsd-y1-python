def mainmenu():
    print("welcome to the health app what do you want to do")
    print("add to patient record (1)")
    print("enter bmi tracker (2)")
    print("dosage amount recommendations (3)")
    options = int(input("enter 1, 2 or 3: "))

    if options == 1:
        patientrecord()
    elif options == 2:
        bmitracker()
    else:
        medicinedrug()


def patientrecord():
    name = input("what is your name: ")
    age = int(input("what is your age: "))
    height = float(input("how tall are you in feet eg 6.3: "))

    print("hello you are", name, "you are", age, "years old and you are", height, "foot")


def bmitracker():
    print("this program calculates your bmi")
    height = float(input("please enter your height (m): "))
    weight = float(input("please enter your weight (kg): "))

    bmi = weight / (height * height)

    if bmi < 18.5:
        print("you are underweight")
    elif 18.5 <= bmi < 24.9:
        print("you are a healthy bmi")
    elif 25.0 <= bmi < 29.9:
        print("you are unhealthy")
    elif 30 <= bmi < 34.9:
        print("you are overweight")
    elif 35 <= bmi < 39.9:
        print("you are Obesity")
    else:
        print("you are fat")


def medicinedrug():
    mousebites = 15
    age = int(input("how old is the person taking the medicine: "))
    dosage = float(input("what is the dosage that that person has taken in mg: "))

    if dosage >= mousebites:
        print("no more medicine is needed today")
    else:
        moremousebites = mousebites - dosage
        print("you can have more medicine, estimated", moremousebites, "mg")


# Start the program
mainmenu()
