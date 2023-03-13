#Menu driven program to perform operations on Numbers entered by user 

def operation(x,y): #Function definition
    print("Choose operation you want to perform : \n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division")
    opt = int(input())
    if opt == 1:
        print("sum is ",x+y)
    elif opt == 2:
        print("Difference is ",x-y)
    elif opt == 3:
        print("Product is ",x*y)
    else:
        print("Quotient is ",x/y,"\nRemainder is ",x%y)
    n = int(input("Press 1 to calculate again and 0 for exit : "))
    if n == 1:
        operation(x,y)


#Main Method :- 
x = int(input("Input first number : "))
y = int(input("Input second number : "))
operation(x,y)  #Function Call
