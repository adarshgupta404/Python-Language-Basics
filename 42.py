cricket = {}
n = int(input("Enter no. of players: "))
for i in range(n):
    name=input("Enter player name: ")
    runs=int(input("Enter runs scored: "))
    cricket[name]=runs
print("Updated dictionary is: ",cricket)
while True:
    name = input("Enter player name to get runs scored: ")
    if name in cricket:
        print("Runs scored by ",name," are ",cricket[name])
    else:
        print("-1")