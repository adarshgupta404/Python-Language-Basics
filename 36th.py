tuple1 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) 
print("Tuple1: ", tuple1) 

unique_tuple = set(tuple1) 
print("Unique Tuple: ", unique_tuple) 

duplicate_tuple = [] 
for i in unique_tuple: 
    if tuple1.count(i) > 1: 
        duplicate_tuple.append(i) 
print("Duplicate Tuple: ", tuple(duplicate_tuple))