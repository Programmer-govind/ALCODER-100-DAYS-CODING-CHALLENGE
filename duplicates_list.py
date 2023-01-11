A = eval(input("Enter list of numbers : "))

i = 0
while i < len(A):
    if A.count(A[i]) > 1:
        A.remove(A[i])
    else:
        i += 1
print("\nAfter removing duplicates, we get\n",A)