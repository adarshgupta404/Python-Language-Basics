str = input("Enter a string: ")
print(str[:-1].replace(str[len(str)-1], "*",) + str[len(str)-1])
