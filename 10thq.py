p=int(input("Enter principal amount: "))
t=int(input("Enter time for year: "))

if p<=200000:
    print("the simple intrest: ",(p*t*10)/100)
elif p>200000 and p<=1000000:
    print("The simple intrest: ",(p*t*12)/100)
else :
    print("the simple intrest: ",(p*t*15)/100)

    
