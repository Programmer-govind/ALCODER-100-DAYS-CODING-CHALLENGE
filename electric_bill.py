#Electricity Bill Generation

units=int(input("Enter no. of units consumed:"))
if units <= 100:
    bill = units*5
elif units <= 200:
    bill = units*6
elif units <= 300:
    bill = units*7
elif units > 300:
    bill = units*8
print("Dear Customer, your electricity Bill is:",bill," Rs")
Finally: print("     Thank You")    