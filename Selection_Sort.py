
#Selection Sort


A = eval(input("Input a list of numbers : "))
n = len(A)

for i in range(n-1):
    for j in range(i+1,n):
        if A[i] > A[j]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

print("\nList in Ascending order :\n",A)


for i in range(n-1):
    for j in range(i+1,n):
        if A[i] < A[j]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

print("\nList in Descending order :\n",A)