try:
    n = int(input("Enter a number: "))
    print("The square of the number is: ", n**2)
except KeyboardInterrupt:
    print("You have pressed Ctrl + C")
except ValueError:
    print("You have entered an invalid input")