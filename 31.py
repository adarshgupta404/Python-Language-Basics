n1 = int(input("Number of elements in the list 1:"))
n2 = int(input("Number of elements in the list 2:"))
li1 = [0]*n1
li2 = [0]*n2
print("Input in list 1 ")
for i in range(n1):
    li1[i] = int(input())
print("Input in list 2 ")
for i in range(n2):
    li2[i] = int(input())
l = []
for i in li2:
    k = 0
    for j in li1:
            if(i==j):
                k = l
                break
    if(k==0):
            l.append(i)
print("Required list: ", l)