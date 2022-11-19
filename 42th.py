cricket={}
n=int(input("enter the no of players: "))
for i in range(n):
    name=input("enter the name of the player: ")
    runs=int(input("enter the runs scored by the player: "))
    cricket[name]=runs
print(cricket)

name=input("enter the name of the player: ")
for i in cricket:
    if i==name:
        print(cricket[i])

else:
    print("-1")