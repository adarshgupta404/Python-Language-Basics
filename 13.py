x=int(input("Enter 1st Number: "))
y=int(input("Enter 2nd Number: "))
k=1
if x>y:
    for i in range(1,y+1,1):
        if x%i==0 & y%i==0:
            k=i
else:
    for i in range(1,x+1,1):
        if x%i==0 & y%i==0:
            k=i
print("Greatest Common Divisor = ", k)