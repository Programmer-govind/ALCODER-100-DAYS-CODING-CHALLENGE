n = int(input("Enter number upto which you want to get Fibonacci Series:"))
a = 0
b = 1
if n <= 2:
    print(a,b,end=' ')
else:
    for i in range(n-2):
        c = a + b
        print(c,end=' ')
        a = b
        b = c
#Fibonacci Series
