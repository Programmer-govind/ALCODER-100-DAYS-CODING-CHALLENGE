#Checking whether a number is prime or not
num = int(input("Enter a number:"))
f = 0
for i in range(1,num+1):
    if num%i == 0:
        f += 1
if f == 2:
    print("\n",num,"is prime number")
else:
    print("\n",num,"is not a prime number")