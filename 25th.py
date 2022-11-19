string=input("Enter string: ")

subs=[]
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        subs.append(string[i:j])
print(subs)