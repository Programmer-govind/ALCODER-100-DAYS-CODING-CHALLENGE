#Automorphic Number An automorphic number is an integer whose square ends with the given integer

num = int(input("Enter a number : "))
count = len(str(num))
square = num**2
print("Square is ",square)
rem = square % (10**count)
if rem == num :
    print(num," is Automorphic number.")
else:
     print(num," is not a Automorphic number.")