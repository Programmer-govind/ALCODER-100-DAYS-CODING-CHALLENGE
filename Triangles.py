#Equilateral, Isosceles, Scalene Triangle

a = int(input("Enter first side of triangle (in cm):"))
b = int(input("Enter second side of triangle (in cm):"))
c = int(input("Enter third side of triangle (in cm):"))
if a == b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or c == a:
    print("Triangle is isosceles")
else:
    print("Triangle is Scalene")
Finally: print('        Thank You')