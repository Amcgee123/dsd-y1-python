def hospital():

    name=input("enter Patient Name:")
    age =input("enter age")
    height= input("height")
    weight= input("WEIGHT")
    
    bmi=weight/(height*height)
    
    if bmi>30:
        print("overweight")
    else:
        print("oyou are healthy")
    
    print("Patient:",name,"has bmi of",bmi)
hospital()
