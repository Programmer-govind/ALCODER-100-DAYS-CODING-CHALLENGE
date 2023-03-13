#Number Patterns
num = int(input("Enter a number to print Pattern :"))
for a in range(1,num+1):
    for b in range(5,a-1,-1):
        print(b,end=' ')
    print()