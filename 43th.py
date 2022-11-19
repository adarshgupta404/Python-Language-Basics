d = {1: 10, 2: 30, 3: 22}  
l = sorted(d.items(), key=lambda kv: kv[1])
d = dict(l)
print(d)