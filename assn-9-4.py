#Program that read the mbox-short.txt and figure out who sent the greatest # of mail.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
bigcount= None
bigword= None
names= list()
counts= dict()
for line in fh:
  line = line.rstrip()
  if not line.startswith("From"): continue    
  words = line.split()
  if words[0] == "From:" : continue
  allmail = words[1]
  names.append(allmail)
#print(names)

#for name in names:
# if name not in count:
#  count[name] = 1
# else:
#  count[name] = count[name] + 1
#print(counts)
   
for name in names:
  counts[name] = counts.get(name,0)  + 1
#print (counts)

for word, count in counts.items():
 if bigcount is None or count > bigcount:
  bigword= word
  bigcount= count
print(bigword, bigcount)

