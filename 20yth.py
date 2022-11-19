limit = 100
sum = 0
a = 1
b = 1
while b < limit:
  if b % 2 == 0 : 
      sum += b
      print(b)
  h = a + b
  a, b = b, h
  
print("The sum of all even term is",sum) 