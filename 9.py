x=int(input("Enter number 1: "))

y=int(input("Enter number 2: "))

z=int(input("Enter number 3: ")) 
print("Sorted Numbers in descending order: ",end="")
if x>=y:
    if x>=z:
        if y>=z:
            print(x," ",y," ",z)
        else:
            print(x," ",z," ",y)
    else:
            print(z," ",x," ",y)
else:
    if y>=z:
        if x>=z:
            print(y," ",x," ",z)
        else:
            print(y," ",z," ",x)
    else:
        print(z," ",y," ",x)