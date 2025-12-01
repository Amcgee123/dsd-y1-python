
import random
score = random.randint (10,1000)
username = input("what is you username? ")
print("your score is ",score,"")
with open("scores.txt","a") as file:
    data = score , " " , username,"\n"
    file.write(str(data))
