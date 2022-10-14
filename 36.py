#q36
x=int(input("Enter the no of elemnts to be added "))
tuple=()
for i in range(x):
    y=int(input("Enter elemnts to be added "))
    tuple=tuple+(y,)
c=0
tuple1=()
tuple2=()
for i in tuple:
    for j in tuple:
        if(i == j):
            c=c+1
    if(c>=2):
        tuple1=tuple1+(i,)
        c=0
    else:
        tuple2=tuple2+(i,)
        c=0   
            
print(" duplicate elements are =  ",tuple1)
print(" unique elements are =  ",tuple2)

            
        
