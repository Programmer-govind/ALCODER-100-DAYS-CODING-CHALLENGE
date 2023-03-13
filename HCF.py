

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
while n1 % n2 != 0:
    rem = n1 % n2
    n1 = n2
    n2 = rem
print("HCF is",n2)

#HCF of two numbers
