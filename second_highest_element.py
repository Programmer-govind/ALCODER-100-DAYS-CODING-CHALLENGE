
#Finding second heighest element by applying logic

A = eval(input("Input a list of numbers : "))

print("\nHighest element in list is ", max(A))

m = max(A)
while m in A:
    A.remove(m)

res = max(A)
print("\nSecond highest element in list is ",res)

'''
#Another method :

A = eval(input("Input a list of numbers : "))

n = 0
for num in A:
    if num > n:
        n = num
print("\nHighest element in list is ", n)

res = 0
for num in A:
    if num!= n and num > res:
        res = num
        
print("\nSecond highest element in list is ", res)
'''
    