mgdlconversions=0.0555
mmolLconversion=23
mmol=float
mgdl=float
mmolnew=float
mgd1new=float
def labresultsconverter ():
    print("what lab results are you conreting between")
    options=int(input("type 1 for mg/dL --> mmol/L and 2 for mg/dL <-- mmol/L "))   

    if options == 1:
        
        mgdl=input("please enter the mg/dl")
        mmolnew=mgdl*mgdlconversions
        print("",mmolnew,"mmol/l")

    elif options ==2:
        mmol=input("please enter the mmol/l")
        mgd1new=mmol*mmolLconversion
        print("",mgd1new,"mg/gl")
        