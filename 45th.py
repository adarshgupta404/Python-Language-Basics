def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm


def gcd(x, y):
   if x > y:
       smaller = y
   else:
       smaller = x
   for i in range(1,smaller+1):
       if((x % i == 0) and (y % i == 0)):
           gcd = i
   return gcd


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1,"and", num2,"is", lcm(num1, num2))
print("The GCD of", num1,"and", num2,"is", gcd(num1, num2))