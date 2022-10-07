p=float(input("Enter principal: ")) 
t=int(input("Enter time in years: "))
if p<200000:
    r=10
elif p<=1000000:
    r=12
else:
    r=15
print("Rate=",r,"%")
i=p*r*t//100
print("Interest=",i)