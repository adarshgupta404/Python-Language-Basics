def is_palindrome(str):

    if str == str[::-1]:
      return True

    else:
     return False

str = input("Enter string: ")

if is_palindrome(str):
    print(str, "is a palindrome")

else:
    print(str, "is not a palindrome")
    