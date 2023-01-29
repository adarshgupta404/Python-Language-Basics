#Open the source and target files
source_file = open('source_file.bin', 'rb')
target_file = open('target_file.bin', 'wb')

#Read the first 100 characters from source file
data = source_file.read(100)

#Write the first 100 characters to target file
target_file.write(data)

#Close the source and target files
source_file.close()
target_file.close()