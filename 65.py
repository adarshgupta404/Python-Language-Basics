# open files for reading and writing 
infile = open("input.txt", "r")
outfile = open("output.txt", "w")

# read the contents of the input file 
contents = infile.read()

# reverse the contents of the file 
reverse_contents = contents[::-1]

# write the reversed contents to the output file 
outfile.write(reverse_contents)

# close the files 
infile.close()
outfile.close()