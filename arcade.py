machines  = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"] 
categories = ["Pinball", "Rhythm", "Racing", "Shooter"] 
status     = ["Working", "Working", "Needs Service", "Working"] 

def mainmenu():
    print("vew all machines(1)                                                (3)")
    print("(2)                                                                (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        print ("machines  categories  status")
        print ("",machines[0],"",categories[0],"",status[0],"")
        print ("",machines[1],"",categories[1],"",status[1],"")
        print ("",machines[2],"",categories[2],"",status[2],"")
        print ("",machines[3],"",categories[3],"",status[3],"")
        print ("",machines[4],"",categories[4],"",status[4],"")
        print ("",machines[5],"",categories[5],"",status[5],"")
        print ("",machines[6],"",categories[6],"",status[6],"")
        print ("",machines[7],"",categories[7],"",status[7],"")
        mainmenu()

    elif options == 2:

        machine=input("Enter the new machine name")
        cat=input("Enter the machine category ")
        stats=input("Enter the machine status(working or needs service)")

        machines.append(machine)
        categories.append(cat)
        status.append(stats)

        mainmenu()

    elif options == 3:
        pass

    elif options == 4:
        pass

mainmenu()
