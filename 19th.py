p=0 ; c=0 

while(1):
    f=0
    a=int(input("Enter number: "))
    if a==-1:
        print("Exittng.")
        break
    if a==1:
        continue
    for i in range(2,a):
        if a%i==0:
            f=f+1
            break
    if f==0:
        p=p+1
    else:
        c=c+1
        
print("Total no. prime number: ",p)
print("Total no. of Composite number: ",c)
        
    


    