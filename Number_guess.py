
#Number_guess game
import random

num = random.randint(1,20)


    

for i in range(3):
    guess = int(input("\nGuess a number between 1 to 20 : "))
    for a in range(3,1):
        printf("You have ",a," chance left.\n")
        a = a - 1
    if guess == num:
            print("*" * 20)
            print("    You win")
            print("*" * 20)
            break
    elif num < guess:
        print("\nSorry,Your guess is less than the number. ")
    elif num > guess:
        print("\nSorry your guess is greater than the number. ")
        
else:
     print("-"* 20)
     print("\n    Sorry, you loose.")
     print("-"* 20)
     

     print("\n\nThe number is",num)   
        





        
        
        
        