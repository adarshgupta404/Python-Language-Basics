n=int(input("Enter a number: "))

x=0
num=n

while(num>0):
    x=x+((num%10)**3)
    num=num//10
if x==n:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
    
    