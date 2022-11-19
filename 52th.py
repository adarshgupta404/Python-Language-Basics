def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#l, u = 2, 10
l=int(input("Enter lover limit: "))
u=int(input("Enter upper limit: "))
for num in range(l, u + 1):
   if isPrime(num):
       print(num, end = ' ')