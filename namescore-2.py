name = input("what is your name? ")
score = input("what score did you get? ")
with open("scores2.txt","a")as file:
    with open("scores2.txt","a") as file:
        write = score , " " , name,"\n"
        file.write(write)