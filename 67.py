# open source and destination files 
with open("source.txt", "r") as source_file: 
    with open("destination.txt", "w") as dest_file: 
        # read source file 
        text = source_file.read() 
  
        # convert text to upper case 
        text = text.upper() 
  
        # write to destination file 
        dest_file.write(text)