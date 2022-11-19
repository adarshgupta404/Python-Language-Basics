x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))

if x >y and x>z:
    if y>z:
        print("The sorted list : ",x,y,z)
    else :
        print("the sorted list : ",x,z,y)
elif y>z and y>x:
    if x>z:
        print("The sorted list : ",y,x,z)
    else:
        print("The sorted list : ",y,z,x)
else:
    if y>x:
        print("The sorted list: ",z,y,x)
    else:
        print("The sorted list: ",z,x,y)

        
        
    
    