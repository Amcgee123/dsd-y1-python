one = "available"
two = "in use"
three = "under maitinence"

laneone = one
lanetwo = one
lanethree = one
lanefouw = one
lanefive = one
lanesix = one
laneseven = two
laneeight = one
lanenine = three

def mainmenu():
    print("(1)                                                                (3)")
    print("check and change availability (2)                                    (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        pass#book 

    elif options == 2: 
        print("lane one is ",laneone,"") 
        print("lane two is",lanetwo,"") 
        print("lane three is",lanethree,"")
        print("lane 4 is",lanefouw,"")
        print("lane five is",lanefive,"")
        print("lane six is",lanesix,"")
        print("lane seven is ",laneseven,"")
        print("lane eight is",laneeight,"")
        print("lane nine is ",lanenine,"")

        no=int(input("what lane do you want to change avilability type 0 for back"))
            
        num_to_word = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
            }       

        print("you are changeing lane ",no,"")
        print("type 1 available use 2 for in use and 3 for under maintinence ")
        if no == 0:
            mainmenu()
        
        elif no > 0:
            option=int(input("enter what you whant to do(1,2 or 3)"))





    elif options == 3:
        pass

    elif options == 4:
        pass
    
    mainmenu()