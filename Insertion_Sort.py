# Insertion Sort

a = eval(input("Enter the list of  numbers : "))

n = len(a)

print("\nBefore swap",a)

for i in range(1,n):
         
         num = a[i]
         j = i - 1
         while j >=0 and num < a[j]:
             a[j+1] = a[j]
             j -= 1
         a[j+1] = num

print("\nAfter swap",a)
             
         
    