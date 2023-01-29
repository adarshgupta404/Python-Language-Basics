src_file = open("src_file.py", "r") 
  
# The destination file 
dst_file = open("dst_file.py", "w") 
  
# Iterate over each line in the source file 
for line in src_file: 
  
    # Check if the line doesn't start with '#' 
    if not line.startswith('#'): 
  
        # Write the line to the destination file 
        dst_file.write(line) 
  
# Close the files 
src_file.close() 
dst_file.close()