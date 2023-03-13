'''finding LCM of two numbers'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    f = num1
else:
    f = num2
for i in range(f,num1*num2 + 1):
            if i % num1 == 0 and i % num2 == 0:
                print("LCM of",num1,"and",num2,"are: ",i)
                break
    
