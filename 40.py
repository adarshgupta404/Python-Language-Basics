dic = {}
string = input()

for char in string:
    if char not in dic:
       dic[char] = 1 
    else:
        dic[char] += 1
print (dic)