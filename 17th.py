a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

if(a>b):
    max=a
else:
    max=b
while(True):
    if(max%a==0 and max%b==0):
        print("The LCM is",max)
        break
    max+=1
    
        