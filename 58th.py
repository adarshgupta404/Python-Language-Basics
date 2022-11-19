try: 
    num1 = int(input("Enter first number: ")) 
    num2 = int(input("Enter second number: ")) 
  
    print("Addition of two numbers = ", num1 + num2) 
    print("Multiplication of two numbers = ", num1 * num2) 
    print("Subtraction of two numbers = ", num1 - num2) 
    print("Division of two numbers = ", num1 / num2) 
except ValueError: 
    print("Error Occurred!!!") 
except ZeroDivisionError: 
    print("Divided by Zero") 
except: 
    print("wrong input") 



