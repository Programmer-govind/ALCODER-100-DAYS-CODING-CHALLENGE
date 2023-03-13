
#Perfect number - sum of factors of a Number equal to number itself 

num = int(input("Enter a number you want to check:"))
s = 0
print("\nFactors are : ")
for a in range (1,num+1):
    if num % a == 0:
        print(a)

#Checking perfect or not
for a in range (1,num):
    if num % a == 0:
        s += a
if s == num:
    print("\n",num,"is a perfect number")
else:
    print("\n",num,"is not a perfect number")