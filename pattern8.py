num = int(input("How many rows are there:"))
for a in range(1,num+1):
    for b in range(1,num+1):
        if a==b or a+b == num+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
#Number Pattern