caloriesperminuet = 10 
converstion=1300


def mainmenu():
    print("calorie tracker(1)                                                                (3)medication timing")
    print("step to km converter(2)                                                         (4)medisine pack usage")
    print("heart recovery(5)")
    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        calorietracker()

    elif options == 2: 
        step()

    elif options == 3:
        medisinedrugtiming()

    elif options == 4:
        medisinedrugusage()


def calorietracker():
    time=int(input("how long where you working out for (in minuets)"))
    burnt = caloriesperminuet * time
    print("you have burned ",burnt," calories ")
    mainmenu()


def step():
    steps=int(input("how many steps have you taken"))
    distance=steps/converstion
    print("you have walked",distance," km ")
    mainmenu()

def medisinedrugtimeing():
    minuets=int(input("how long has it been since you have taken the tablets(minuets)"))
    
    

mainmenu()