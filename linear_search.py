list = eval(input("Enter a list of numbers : "))
num = int(input("Enter the number you want to search : "))

count = 0

for i in range(len(list)):
    if list[i] == num:
        print("\nFound at ",i+1)
        count += 1
if count == 0: 
    print("\nNumber not found.")