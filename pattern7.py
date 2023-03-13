num = int(input("How many rows are there:"))
for i in range(num,0,-1):
    for s in range(i):
        print("*",end='')
    for t in range(num-i):
        print("  ",end='')
    for s in range(i):
        print("*",end='')
    print()
    
for i in range(1,num+1):
    for s in range(i):
        print("*",end='')
    for t in range(num-i):
        print("  ",end='')
    for s in range(i):
        print("*",end='')
    print()
    
#Number Pattern
    