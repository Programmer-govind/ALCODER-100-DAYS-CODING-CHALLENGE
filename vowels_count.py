text = input("Enter a string : ")

count = 0

for char in text:
    if char in 'aeiouAEIOU':
        count += 1
        
print("\nNo of vowels = ",count)
    