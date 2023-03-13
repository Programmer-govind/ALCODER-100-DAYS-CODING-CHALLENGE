# Complement of a list

a = eval(input("Enter list 1 : "))
b = eval(input("Enter list 2 : "))

a_comp = []
b_comp = []

for val in b:
    if val not in a:
        a_comp.append(val)
    
for val in a:
    if val not in b:
        b_comp.append(val)
    
print("\nList 1 Compliment : ",a_comp)
print("\nList 2 Compliment : ",b_comp)
