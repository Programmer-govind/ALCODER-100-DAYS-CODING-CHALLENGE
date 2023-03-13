#Palindrome Number
n = int(input("Enter a number :"))
res = 0
p = n
while (n > 0):
    d = n % 10
    res = res * 10 + d
    n = n // 10
print("Reverse of number is :",p)
if res == p:
    print(p," is a palindrome number.")
else:
    print(p," is not a palindrome number.")