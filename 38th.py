tuple = (2, 4, 6, 8, 10)

distinct_pair = []

for i in range(0, len(tuple)):
    for j in range(i+1, len(tuple)):
        if tuple[i] * tuple[j] % 2 == 0:
            distinct_pair.append((tuple[i], tuple[j]))

print(distinct_pair)