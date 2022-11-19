string = input ("Enter the string to check if it is a palindrome: ")
string = string.casefold ()
reverse_string = reversed (string)

if list(string) == list(reverse_string):
    print ("The string is a palindrome.")
else:
    print ("The string is not a palindrome.")