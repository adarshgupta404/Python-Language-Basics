#qq38
n =int(input("Enter number of elements in tuple: "))
li=[0]*n
print("Input in tuple: ")
for i in range (n):
    li[i]=int(input())
p=[]
i=0
while i<n-1:
    d1=li[i]
    d2=li[i+1]
    i=i+1
    m=d1*d2
    k=[]
    if m%2==1:
        k=[d1,d2]
        p.append(k)

print("required pair: ",p)    
