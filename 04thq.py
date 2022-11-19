A = int(input("Enter 1st number: "))
B = int(input("Enter 2nd number: "))
A = A ^ B
B = A ^ B
A = A ^ B
print("After the swapping:")
print("The value of A: ", A)
print("The value of B: ", B)
