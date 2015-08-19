#This is a program to prompt for a score between 0.0 and 1.0 and print a grade using a table.

score = float(input("Enter a score between 0.0 and 1.0"))
if score < 0.6:
 print ("F")
elif score >= 0.6 and score < 0.7:
 print ("D")
elif score >= 0.7 and score < 0.8:
 print ("C")
elif score >= 0.8 and score < 0.9:
 print ("B")
elif score >= 0.9 and score <= 1.0:
 print ("A")
else:
 print ("ERROR: The score that you introduce is out of the range")