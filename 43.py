d = {'b':2, 'd':4, 'c':3, 'e':5}
d1 = {}
for k,v in d.items():
    d1.setdefault(v,k)
print(d1)