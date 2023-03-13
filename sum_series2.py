x = int(input("Enter x:"))
n = int(input("Enter n:"))
sum = 0
for i in range(1,n+1):
    if i<n:
        print(x,'^',i,'+',end=' ')
    else:
        print(x,'^',n,end=' ')
    sum += x**i
print("\n=",sum)


#Sum of Series