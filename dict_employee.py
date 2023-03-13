


#Creating a dictionary for Employees

def create(dename,n):
    for i in range(n):
        ename = input("\nEnter the Employee name : ")
        sal = input("\nEnter Salary : ")
        job = input("\nEnter Job : ")
        dename[ename] = [sal,job]
        
        
demp = {}
n = int(input("\nHow many employees are there : "))
create(demp,n)
print("\nDictionary is ",demp)