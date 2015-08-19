#This program to prompt the user for hours and rate per hour  to compute  gross pay.

hours = float(input("How many hours do you work?"))
rate = float(input("Which is your rate per hour?"))
if hours <= 40:
 Gross_pay = hours * rate
 print("Your Gross pay is:", Gross_pay)
else:
 Gross_pay = 40*rate + (hours-40)*rate*1.5
 print("Your Gross pay is:", Gross_pay)
 
