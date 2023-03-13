
#Union and intersection of lists

a = eval(input("Enter list 1 : "))
b = eval(input("\nEnter list 2 : "))

U = a.copy()
I = []

for val in b:
    if val in a:
        I.append(val)
    else:
        U.append(val)
        
print("\nList 1 is ",a)
print("\nList 2 is ",b)
print("\nUnion of lists is ",U)
print("\nIntersection of lists is ",I)