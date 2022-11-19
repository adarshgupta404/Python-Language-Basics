import statistics

sample_list = [1,2,3,4,5,6,7,8,9,10]

x = statistics.mean(sample_list)
y = statistics.median(sample_list)
z = statistics.stdev(sample_list)

print("Mean: ", x)
print("Median: ", y)
print("Standard Deviation: ", z)