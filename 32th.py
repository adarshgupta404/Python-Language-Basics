n=int(input("size of list: "))
l1=[0]*n
print("Enter a number: ")
for i in range(n):
    l1[i]=int(input())
p=[]
i=0
while i<n-1:
    d1=l1[i]
    d2=l1[i+1]
    i=i+1
    m=d1*d2
    k=[]
    if m%2==0:
        k=[d1,d2]
        p.append(k)
print('required pair',p)


