#Armstrong Number
for a in range(100,1000):
    num = a
    sum = 0
    while num > 0:
            d = num % 10
            sum = sum + d**3
            num = num//10
    
    if sum == a:
        print(a,"is armstrong number.")
            
        