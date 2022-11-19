#Roots of a Quadratic Equations

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d = b**2-(4*a*c)
if d < 0:
    print("No real roots exist")
elif d==0:
   r1=r2= -b/(2*a)
   print("Real and equal roots are:",r1, r2)
else:
    r1= -b + d**0.5/(2*a)
    r2= -b - d**0.5/(2*a)
    print("Real and unequal roots are:",r1, r2)
Finally: print('    Thank You')