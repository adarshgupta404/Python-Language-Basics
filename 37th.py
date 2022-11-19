tuple1 = (1, 2, 1, 4, 2, 6, 2, 4, 2, 4) 

d = {} 

for i in tuple1: 
    if i in d: 
        d[i] += 1
    else: 
        d[i] = 1

for key, value in d.items(): 
    print (" frequency of elemnt ",key ,"= ", value)