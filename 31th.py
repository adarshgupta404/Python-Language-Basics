n1=int(input("Enter size of list1: "))
n2=int(input("Enter size of list2: "))
list1=[0]*n1
list2=[0]*n2
print("Enter the element list1: ")
for i in range(n1):
    list1[i]=int(input())
print("Enter the element list2: ")
for i in range(n2):
    list2[i]=int(input())
list=[]
for i in list2:
    k=0
    for j in list1:
        if i==j:
            k=1
            break
    if k==0:
        list.append(i)
print("Required list: ",list)


