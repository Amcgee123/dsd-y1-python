arcademaciens = {
    "01":{"name":"pinball wizzard","catagory":"pinball","status":"working"},
    "02 X":{"name":"Dance Floor X","catagory":"rythm","status":"working"},
    "03":{"name":"Retro Racer","catagory":"racing","status":"needs service"},
    "04":{"name":"Alien Blaster","catagory":"shooter","status":"working"}
}


def mainmenu():
    print("(1)                                                                (3)")
    print("(2)                                                                (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        for key, info in arcademaciens.items():
            print(f"{key}: {info}")

        mainmenu()

    elif options == 2: 
        pass
        mainmenu()

    elif options == 3:
        pass
        mainmenu()

    elif options == 4:
        pass
        mainmenu()

mainmenu()


