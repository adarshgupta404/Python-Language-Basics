import random
def shuffle(low,high,n):
 for i in range(n):
  print(random.randint(low,high),end=" ")
low=int(input("Enter lower range:"))
high=int(input("Enter upper range:"))
n=int(input("Enter number of elements:"))
shuffle(low,high,n)
