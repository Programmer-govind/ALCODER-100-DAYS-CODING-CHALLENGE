
# Toggling using built in function : Swapcase

txt = input("\nEnter a string : ")
res = print("\nResultant string after toggling is",txt.swapcase())

#Another method 

res = ""
for ch in txt:
    if ch.islower():
        res += ch.upper()
    elif ch.isupper():
        res += ch.lower()
    else:
        res += ch
        
print("\nResultant string after toggling is ",res)


# Another Method used in other languages like C, C++ where built in functions are not present

result = ""

for ch in txt:
    if ascii(ch) >= 97 and ascii(ch) <= 122:
        result += chr(ascii(ch) - 32)
    if ascii(ch) >= 65 and ascii(ch) <= 90:
        result += chr(ascii(ch) + 32)
       
    else:
        result += ch
 
print("\nResultant string after toggling is ",result)
    
        



        
    

