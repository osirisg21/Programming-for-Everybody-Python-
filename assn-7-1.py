#This program read through a file and print the contests line by line all in upper.

fname= input("Enter the file name:")
try:
 fh= open(fname)
except:
 print("Error")
 exit()
for line in fh:
 line= line.upper()
 line= line.rstrip()
 print(line)