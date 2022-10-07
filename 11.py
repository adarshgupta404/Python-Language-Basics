print("Pattern A")
k=1
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if j==i:
            print(k, end='')
        else:   
            print(str(k)+", ", end=' ')
        k=k+1
    print()

print("\nPattern B")
row = 5
for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='') 
    # printing space and staying in same line
    for j in range(2*i-1):
        print('*',end='') 
    # printing * and staying in same line
    print()
