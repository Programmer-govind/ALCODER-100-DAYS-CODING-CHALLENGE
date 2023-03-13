
#Profit or Loss
cp = int(input("Enter cost price:"))
sp = int(input("Enter selling price:"))
if sp > cp:
    print("Profit is ",sp - cp)
elif cp > sp:
    print("Loss is ",cp - sp)
else:
    print('No profit No loss')