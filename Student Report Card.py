name=(input("Enter name:"))
eng=float(input("Marks obtained in English:"))
hindi=float(input("Marks obtained in Hindi:"))
math=float(input("Marks obtained in Math:"))
sci=float(input("Marks obtained in Science:"))
sst=float(input("Marks obtained in SST:"))
total=eng+hindi+math+sci+sst
print("---------------------")
print("Report Card of",name)
print("---------------------")
print("Total marks scored:",total,"out of 500")
per= total/5
print("Percentage:",per,"%")
if per>=40:
    print("   Congratulations! ",name)
else:
    print("   Sorry, Better Luck next time.")


#Student's Report Card
Finally: print('Thank You')