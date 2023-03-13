
# Reversing a string word by word

text = input("Enter a string to be reversed : ")

char = text.split( )
char = char[::-1]

res = ""
for w in char:
    res += w + " "
    
print("\n",res)


''' Another method using join

res = " ".join(char)

print("\n",res) '''
