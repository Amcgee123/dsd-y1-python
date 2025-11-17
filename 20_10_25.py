def home ():
    print("medsafety(1)                                                                      (3)sleep tracker")
    print("fitness cemter acess(2)")
    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
       medsafety()

    elif options == 2: 
        fitnesscenter()

    elif options == 3:
        pass ()

    elif options == 4:
        pass ()

def medsafety() :
    age=int(input("enter patient age"))
    weaght=float(input("please enter patient weaight kg"))
    
    if age > 12 and weaght > 40:
        print("safe to give")

    else:
        print("not safe to give")

    home()

def fitnesscenter():
    age=int(input("enter patient age"))
    permition=str(input("enter yes or no do you have medical clearance"))

    if age >= 18 or permition == "yes":
        print("you are allowed in to the intensive zone")

    elif age < 18 or permition == "no":
        print("you are not allowed in to the intensive zone")
    



home()