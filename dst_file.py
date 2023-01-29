infile = open("input.txt", "r")
outfile = open("output.txt", "w")

contents = infile.read()

reverse_contents = contents[::-1]

outfile.write(reverse_contents)

infile.close()
outfile.close()