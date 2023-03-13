# Sum of digits of a number

#Sum of digits of a number
num = int(input("Enter a number :"))
s = 0
a = num
while num != 0:
    d = num % 10
    s += d
    num = num // 10
print("Sum of digits of",a," is",s)