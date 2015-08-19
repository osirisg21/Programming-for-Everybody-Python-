#This program to prompt to compute gross pay using try and except.

hours = input("How many hours do you work?")
try:
 h = float(hours)
except:
 h = -1
rate = input("Which is your rate per hour?")
try:
 r = float(rate)
except:
 r = -1
if h <= 40:
 Gross_pay = h * r
 print("Your Gross pay is:", Gross_pay)
else:
 Gross_pay = 40*r + (h-40)*r*1.5
 print("Your Gross pay is:", Gross_pay)