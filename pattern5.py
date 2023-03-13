num = int(input("How many rows are there :"))
for a in range(1,num+1):
    for s in range(num-a):
        print(" ",end=' ')
    for t in range(2*a-1):
        print("*",end=' ')
    print()
for a in range(num-1,0,-1):
    for s in range(num-a):
        print(" ",end=' ')
    for t in range(2*a-1):
        print("¥",end=' ')
    print()
#Number Pattern      
        
            
        