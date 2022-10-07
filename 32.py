n = int(input("Number of elements in the list:"))
li = [0]*n
print("Input in list")
for i in range(n):
    li[i] = int(input())
p = []
i = 0
while i<n-1:
    d1 = li[i]
    d2 = li[i+1]
    i = i+1
    m = d1*d2
    k = []
    if m%2 == 0:
        k = [d1, d2]
        p.append(k)
print("Required pairs: ",p)