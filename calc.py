import numpy
import random
import math 
import datetime
import time


def mainmenu():
    print("(1)                                                                (3)")
    print("(2)                                                                (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        
        number = int(input("Enter a number"))
        numbersquareroot = (math.sqrt(number))
        numbersquared = (number*number)
        rounded = round(number)
        areaofcircle = 3.14159265359 * numbersquared
        print("Square root:",numbersquareroot,"")
        print("Squared:",numbersquared,"")
        print("Rounded:",rounded,"")
        print("Area of cucle with your number as radius:",areaofcircle,"") 
        time.sleep(1)
        mainmenu()

    elif options == 2: 
        totaltries = 3 
        while totaltries > 0:
            print("You have",totaltries,"lives left")
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
            dicetotal=dice1+dice2
            input("press enter to rool the dice")
            if dicetotal == 7 or dicetotal == 11:
                print("you got ",dicetotal,"")
                print("you win")
                totaltries -= 1
            else:
                print("you got ",dicetotal,"")
                print("try again")
                
                totaltries -= 1
        mainmenu()
    elif options == 3:
        currentdate = datetime.datetime.now()
        currentday = currentdate.day
        currentmonth = currentdate.month
        currentyear = currentdate.year

        currenthour = currentdate.hour
        currentminuet = currentdate.minute
        currentseconds = currentdate.second

        print("the date is" ,currentday,currentmonth,currentyear,"")
        print("the time is"  ,currenthour,currentminuet,currentseconds,"")
        year = int(input("what year where you born"))
        month = int(input("what month where you born(number)"))
        day = int (input("what date where you born day"))
        age = currentyear - year 
        print("you are",age,"years old")
        
        mainmenu()
    elif options == 4:
        pass
    mainmenu()
mainmenu()