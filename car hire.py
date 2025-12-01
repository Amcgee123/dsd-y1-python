def dase () :
    mileagestart = 1360 
    perdaycharge = 20 
    permilecharge = 0.05
    days=int(input("how many days was the car hired for"))

    if days < 1:
        dase () 

    else:
        print("you have hired the care for",days,"days")
        mileagecalc ()

    def mileagecalc ():
        mileageend=int(input("what is the current mileage"))

        if mileageend <= 1360:
            print("mileage enterd is smaller than start")
            mileagecalc()

        else:
            totalmiles = mileageend - mileagestart
            print("you have driven ",totalmiles,"miles")
            totaldayscharge=days * perdaycharge
            moneymile=totalmiles*permilecharge
            totalcharge=totaldayscharge + moneymile 
 
            print("based of 0.05 pence per mile you owe",moneymile,"pounds and pence")
            print("and you owe 20 puound per day wich is ",totaldayscharge,"£")
            print("intotal you owe",totalcharge,"£")
    mileagestart ()    
dase ()