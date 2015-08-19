# This program which reads list of numbers until "done" is entered. Once "done" is entered print out the total, count ,and average of the numbers.

largest = None
smallest = None

while True:
  num = input("Enter your list of numbers or done: ")
  if num == "done": break
  try:
   enter = float(num)
  except:
   print ("Invalid input")
   continue
  if smallest is None :
   smallest = enter
  elif enter < smallest:
   smallest = enter
# print ("Minimum", smallest )
  if largest is None:
   largest = enter
  elif enter >largest:
   largest = enter
#  print ("Maximum", largest )
print ("Minimum is", smallest )
print("Maximum is", largest)