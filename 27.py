n = int(input("Number of elements in the list:"))
li = [0]*n
print("Input in list")
for i in range(n):
    li[i] = int(input(""))
l = li[0]
s = li[0]
for i in li:
    if(s>i):
        s = i
    if(l<i):
        l = i
print("Largest element in list",l)
print("Smallest element in list",s)






