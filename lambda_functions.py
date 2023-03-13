# Using Lambda functions


x = int(input("\nEnter first no : "))
y = int(input("\nEnter second no : "))

adder = lambda x,y : x + y
subtractor = lambda x,y : x - y
multiplier = lambda x,y : x*y
divisor = lambda x,y : x//y
remainder = lambda x,y : x%y

print("\nSum is ",adder(x,y))
print("\nDifference is ",subtractor(x,y))
print("\nProduct is ",multiplier(x,y))
print("\nQuotient is ",divisor(x,y))
print("\nRemainder is ",remainder(x,y))