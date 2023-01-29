#open file
file = open('filename.txt', 'r')

#read each line of the file into a list
lines = file.readlines()

#loop through the list in reverse order
for line in reversed(lines):
    #print each line in reverse
    print(line[::-1], end='')

#close the file
file.close()