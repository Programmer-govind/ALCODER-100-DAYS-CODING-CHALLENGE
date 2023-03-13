#Number Patterns
num = int(input("Enter how many rows are there :"))
for a in range(num,0,-1):
    for b in range(1,a+1):
        print(b,end=' ')
    print()