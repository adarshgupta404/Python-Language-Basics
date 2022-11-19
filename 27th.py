n=int(input("Enter size of list: "))
list =[0]*n

print("Enter element: ")
for i in range(n):
    list[i]=int(input())
max=list[0]
mini=list[0]
for i in list:
    if mini>i:
        mini=i
    if max<i:
        max=i
                 
print('Minimum Element in the list', mini)
print('Maximum Element in the list', max)