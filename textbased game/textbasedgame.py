import time
def mainmenue ():
    print("loading.")
    time.sleep (0.5)
    print("loading..")
    time.sleep (0.5)
    print("loading...")
    time.sleep (0.5)
    print("loading.")
    time.sleep (0.5)
    print("loading..")
    time.sleep (0.5)
    print("loading...")
    time.sleep (0.5)
    print("loading.")
    time.sleep (0.5)
    print("loading..")
    time.sleep (0.5)
    print("loading...")
    time.sleep (0.5)
    inputted = False
    print("**********The epic cool origonal game**********")
    print("Play game")
    print("Credits")
    print("Close")
    while inputted == False:
        choice =int(input("what is your choice(1,2 or 3)"))
        if choice <= 3:
            inputted = True
        else:
            inputted =False
        if choice == 1:
            choice_print = "play game"
        elif choice == 2:
            choice_print = "Open Credits"
        elif choice ==3:
            choice_print = "Closegame"
        print (choice_print)
        return choice
def gamecode():
    print("**********2/4 life**********")
    print("you awake from your nap on the orange mesa transit systesm")
    print("Name: Morgon Freeman")
    print("age:23")
    print("job:anomolus freeserch")
    print("as you see the the everyday activity of orange mesa you remember that you are late for work")
    print(...)
    print(...)
    print("")

def outputs():
    choice = mainmenue()
    if choice == 1:
        gamecode()



outputs ()


