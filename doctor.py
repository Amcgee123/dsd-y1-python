mgdlconversions = 0.0555
mmolLconversion = 23
fievertemp = 38
total_patients = 0

def mainmenu():
    print("(1)                                                                (3)")
    print("(2)                                                                (4)")

    options = int(input("Enter (1, 2, 3 or 4): "))
    
    if options == 1:
        labresultsconverter()

    elif options == 2: 
        tempchecker()

    elif options == 3:
        add_patient()

    elif options == 4:
        view_total()

def labresultsconverter():
    print("What lab results are you converting between?")
    options = int(input("Type 1 for mg/dL --> mmol/L and 2 for mg/dL <-- mmol/L: "))   

    if options == 1:
        mgdl = float(input("Please enter the mg/dL: "))
        mmolnew = mgdl * mgdlconversions
        print(mmolnew, "mmol/L")
        mainmenu()  

    elif options == 2:
        mmol = float(input("Please enter the mmol/L: "))
        mgdlnew = mmol * mmolLconversion
        print(mgdlnew, "mg/dL")
        mainmenu()  
    temp1 = int(input("Please enter first temp: "))
    temp2 = int(input("Please enter second temp: "))
    temp3 = int(input("Please enter third temp: "))

    avragetemp = (temp1 + temp2 + temp3) / 3

    print("Average temp is", avragetemp)

    if avragetemp > fievertemp:
        print("The temp of", avragetemp, "exceeds the fever threshold constant")
        mainmenu()

    else:
        print("The temp of", avragetemp, "is fine the patient is healthy")
        mainmenu()

def add_patient():
    global total_patients  # global
    total_patients += 1 
    name = input("Enter name: ")  # local
    age2 = int(input("Enter age: "))
    print("Patient added:", name)
    mainmenu()

def view_total():
    print("Total patients:", total_patients)
    mainmenu()

mainmenu()
