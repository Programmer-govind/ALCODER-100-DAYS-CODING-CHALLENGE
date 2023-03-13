# Sum of Series
num = int(input("Enter a number :"))
sum = 0
for i in range(1,num+1):
    sum += 1/i
    if i<num:
        print(1,'+',1,'/',i,'+',end=' ')
    else:
        print(1,'+',1,'/',i,end=' ')
print("\n= ",round(sum,2))
