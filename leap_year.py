#Program to check whether a year is leap year or not

year=int(input("Enter year you want to check:"))
if year % 100 == 0:
   if year % 400 == 0:
       print(year,"is a leap year")
   else:
       print (year,"is not a leap year")
else:
    if year % 4 == 0:
        print(year,"is a leap year")
    else:
        print (year,"is not a leap year")
Finally: print('    Thank You')