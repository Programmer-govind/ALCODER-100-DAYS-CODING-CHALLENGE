#program to generate GST invoice

name=input("Customer Name:")
mob=int(input("Enter mobile no:"))
qty=float(input("Enter quantity:"))
rate=float(input("Rate:"))
amt=qty*rate
GST=5*amt/100
total=amt+GST

if amt <= 499:
   Delivery_charge = 50
else:
    Delivery_charge = 0
    print("Congrats, you are eligible for Free Delivery")
print("    ---------")
print("    Invoice:")
print("    ---------")    
print("Amount:",amt,"Rs")
print("GST @ 5%:",GST,"Rs")
print("Delivery Charge :",Delivery_charge)
print("Total amount to be paid:",total+Delivery_charge, "Rs")
Finally: print('Thank You')

