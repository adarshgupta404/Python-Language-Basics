r = int(input("Enter number of rows in list : "))
c = int(input("Enter number of coulumns in list : "))
a = []
b = []
m = []
print("\nInput for list 1: ")
for i in range(r):
        k = []
        print("Row", i+1)
        for j in range(c):
            k.append(int(input()))
        a.append(k)
print("\nInput for list 2: ")
for i in range(r):
        k = []
        print("Row", i+1)
        for j in range(c):
            k.append(int(input()))
        b.append(k)
for i in range(r):
    g = []
    d = 0
    for j in range(c):
        for k in range(c):      
            d = d + a[i][k]*b[k][j]
        g.append(d)
    m.append(g)
print("\nList after multiplication: ")
for i in range(r):
    for j in range(c):
        print(m[i][j], end = ' ')
    print()

