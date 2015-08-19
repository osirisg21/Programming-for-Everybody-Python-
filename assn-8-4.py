#open romeo.txt and read it using split() if the word is not already in the list if not append it when finish sort and print it.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
fh = open(fname)
poema = list()
for line in fh:
 line = line.rstrip()
 words = line.split()
 for word in words:
  if word not in poema:
   poema.append(word)
   #print(poema)
   #print(len(poema))
   romeo = sorted(poema)  
print(romeo) 
