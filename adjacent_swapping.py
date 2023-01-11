
#Adjacent Swapping

list = eval(input("Enter a list of values : "))

print("\nBefore Swap : ",list)

n = len(list)

for i in range(0,n,2):
    if i + 1 < len(list):
        list[i],list[i+1] = list[i+1],list[i]
    
print("\nAfter Swap : ",list)