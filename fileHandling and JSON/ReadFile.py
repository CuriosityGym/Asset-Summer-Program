fileHandle=open("travelogue.json", "r") # Open file to read
fileContents=fileHandle.read() # read contents of file in a variable
print(fileContents) #print file contents
fileHandle.close() #close the file
