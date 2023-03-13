
# Cartesian Products of two lists

a = eval(input("\nEnter the list 1 : "))
b = eval(input("\nEnter the list 2 : "))

cp = []

for n1 in a:
    for n2 in b:
        cp.append((n1,n2))
        
print("\nCartesian Product is ",cp)
