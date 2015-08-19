#Open mbox-short.txt and read it.line starts 'From using split() and print out the second word .

fname = input("Enter file name: ")
try:
 fh= open(fname)
except:
 fh= open("mbox-short.txt")
count= 0
for line in fh:
  line = line.rstrip()
  if not line.startswith("From"): continue    
  words = line.split()
  if words[0] == "From:" : continue
  count= count +1
  print(words[1])
print("There were", count, "lines in the file with From as the first word")
 
 
#if len(fname) < 1 : fname = "mbox-short.txt"
#fh = open(fname)
#count = 0
#print 