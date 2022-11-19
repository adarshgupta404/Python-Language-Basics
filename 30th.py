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
list=[ x for y in [list1,list2] for x in y]
print("list1: ",list1)
print("list2: ",list2)
print("union of list: ",list)
