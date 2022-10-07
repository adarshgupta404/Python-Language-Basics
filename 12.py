a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))
i=a
print("Odd numbers: ", end='')
while i<=b:
    if i%2==1:
        print(i, end=' ')    
    i=i+1
