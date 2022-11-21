#Student Grade


'''
~~~~~~~~~
>= 91 A+
81 - 90 A
71 - 80 B1
61 - 70 B2
51 - 60 C1
41 - 50 C2
<50   - D
~~~~~~~~~~
'''
per = int(input("Enter marks percentage of student:"))
if per >= 91:
    print("Grade is A+")
elif per > 80:
    print("Grade is A ")
elif per > 70:
    print("Grade is B1")
elif per > 60:
    print("Grade is B2")
elif per > 50:
    print("Grade is C1")
elif per > 40:
    print("Grade is C2")
else:
    print("Grade is D")