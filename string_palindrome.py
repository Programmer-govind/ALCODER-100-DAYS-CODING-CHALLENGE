# String Palindrome

txt = input("Enter a string value : ")

rev = ""
for i in range(len(txt)-1,-1,-1):
    rev += txt[i]

print("\nString is ",txt)


print("Reverse is ",rev)

if rev == txt:
    print("\nGiven String value is Palindrome.")
else:
    print("\nGiven String value is not Palindrome.")
    
