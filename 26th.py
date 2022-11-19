str1=input("Enter string1: ")
str2=input("Enter string2: ")
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)
if((sorted_str1)==(sorted_str2)):
    print("The given string is anagrams")
else:
    print("The given string is not anagrams")
