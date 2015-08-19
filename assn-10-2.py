#Program that read the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
bigcount= None
bigword= None
horas= list()
counts= dict()
for line in fh:
  line = line.rstrip()
  if not line.startswith("From"): continue    
  words = line.split()
  if words[0] == "From:" : continue
  allhrs = words[5]
  found = allhrs.split(":")
  tiempo = found[0]
  horas.append(tiempo)
#print(horas)
   
for hora in horas:
  counts[hora] = counts.get(hora,0)  + 1
#print (counts)
#for hora, values in counts.items():
#print (hora, values)
#for hora, values in counts.items():
# print (hora, values)
  arreglo = (sorted([(hora,values) for hora,values in counts.items()]))
for a,b in arreglo:
 print(a,b)


