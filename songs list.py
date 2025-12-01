def start():
    favoraatesongs = ["feel good inc (gorillaz)", "dirty harry (gorillaz)", "clint eastwood (gorillaz)", "song 2 (blur)", "let it happen (tame impala)"]
    print("1: top 5 songs")
    print("3: replace song")
    enter = input(" ")

    if enter == "1":
        print("my favorite songs are", favoraatesongs[0], "", favoraatesongs[1], "", favoraatesongs[2], "", favoraatesongs[3], "", favoraatesongs[4], "")
        start()

    elif enter == "2":
        song = int(input("what song do you want to replace 1,2,3,4,5 (input): "))
        if song == 1:
            newsong1 = input("enter new song: ")
            favoraatesongs[0] = newsong1

        elif song == 2:
            newsong2 = input("enter new song: ")
            favoraatesongs[1] = newsong2

        elif song == 3:
            newsong3 = input("enter new song: ")
            favoraatesongs[2] = newsong3

        elif song == 4:
            newsong4 = input("enter new song: ")
            favoraatesongs[3] = newsong4

        elif song == 5:
            newsong5 = input("enter new song: ")
            favoraatesongs[4] = newsong5

        print("updated list:", favoraatesongs)
        start()

start()
