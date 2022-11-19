current_num = 1
rows = 5
stop = 2
for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 1
 