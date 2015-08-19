# program that prompts for a file name then open that file and read trough it and print the average.

fn= input("Enter the file name:")
try:
 fh= open(fn)
except:
 print("Error")
 exit()
count= 0
total= 0
for line in fh:
  if not line.startswith("X-DSPAM-Confidence:"): continue
  count= count +1
  fin1= line.find(":")
  convert= float(line[fin1 + 1: ])
  total= total + convert
 #print(count, convert, total )
  print(count, convert, total)
print(total/count)