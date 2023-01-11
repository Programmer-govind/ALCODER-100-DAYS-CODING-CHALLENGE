
#Binary Search
n = int(input("\nHow many elements you have "))
list = eval(input("\nEnter your list of numbers : "))
for i in range(5):
    num = int(input("\nEnter the number you want to search : "))
    beg = 0
    end = len(list) - 1
    while beg <= end:
        mid = (beg + end)//2
        if list[mid] == num:
            print("\nFound at position ",mid+1)
            break
        elif num > list[mid]:
         beg = mid + 1
        elif num < list[mid]:
         end = mid - 1
    else:
         print("\nNumber Not Found")
     
     
    
