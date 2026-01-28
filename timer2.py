import time
def mainmenu():
    print("(1)                                                                (3)")
    print("(2)                                                                (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        timer()

    elif options == 2: 
        pass

    elif options == 3:
        pass

    elif options == 4:
        pass

def timer():
    print("This program will count down to a specific time.")

    # current time input

    timeh = int(input("Enter the current time hour (0-23): "))
    timem = int(input("Enter the current time minute (0-59): "))
    times = int(input("Enter the current time second (0-59): "))

    # desired time input
    timewantedh = int(input("Enter the desired time hour (0-23): "))
    timewantedm = int(input("Enter the desired time minute (0-59): "))
    timewanteds = int(input("Enter the desired time second (0-59): "))

    name=input("what do you want to call this timer?")

    # convert hours and minutes to seconds (FIXED)
    timewantedsecondsh = timewantedh * 3600
    timewantedsecondsm = timewantedm * 60

    timesecondsh = timeh * 3600
    timesecondsm = timem * 60

# total seconds
    timesecondswanted = timewantedsecondsh + timewantedsecondsm + timewanteds
    timesecondscurrent = timesecondsh + timesecondsm + times

    print(timesecondswanted)
    print(timesecondscurrent)
    timeinsecondsleft = timesecondswanted - timesecondscurrent
    print(timeinsecondsleft)

    while timeinsecondsleft > 0:
        print(",there is ",timeinsecondsleft,"seconds left until",name,"")
        time.sleep(0.9985)
        timeinsecondsleft -= 1
            
    while timeinsecondsleft < 0:
        print("it is time for ",name,".")
        mainmenu()

    mainmenu()