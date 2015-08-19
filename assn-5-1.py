# This program which reads list of numbers until "done" is entered. Once "done" is entered print out the total, count ,and average of the numbers.
count = 0
total = 0

while True:
  enter = input("Enter your list of numbers or done: ")
  if enter == "done": break
  try:
    num = float(enter)
  except:
   print ("Enter a correct value")
   continue
  count = count +1
  total = total + num
  print ("before", count, total, num)
print ("After", count, total, total/count)
 