#q35
x=int(input("Enter the no of elemnts to be added "))

tuple=()
for i in range(x):
    y=int(input("Enter elemnts to be added "))
    tuple=tuple+(y,)
mean=0
for i in tuple:
    mean=mean+i
print("mean = ",mean/x)
