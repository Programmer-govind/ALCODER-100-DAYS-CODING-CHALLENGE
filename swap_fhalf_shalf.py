
list = eval(input("Enter a list of values : "))

print("\nBefore Swap : ",list)

n = len(list)

mid = n // 2

if len(list) % 2 == 0:
    for i in range(0,mid,1):
        list[i],list[mid+i] = list[mid+i],list[i]
    
    print("\nAfter Swap : ",list)

else:
    for i in range(0,mid,1):
        if i + 1 < len(list):
            list[i],list[mid+i+1] = list[mid+i+1],list[i]
    print("\nAfter Swap : ",list)