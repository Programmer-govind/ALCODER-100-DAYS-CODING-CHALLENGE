
# Reversing a list

for i in range(3):
    list = eval(input("\nEnter a list of values : "))
    
    count = len(list)
    
    n = count//2
    
    for i in range(0,n,1):
            list[i],list[count-i-1] = list[count-i-1],list[i]
        
    print("\n",list)