    #DICE GAME on Character User Interface

import random
import time
name1 = input("Enter name of player 1 : ")
name2 = input("Enter name of player 2 : ")

val1 = random.randint(1,6)
val2 = random.randint(1,6)
time.sleep(2)
print("\n",name1," got ",val1)
time.sleep(2)
print("\n",name2," got ",val2)
time.sleep(2)
if val1>val2:
    print("\n",name1," wins.")
elif val2>val1:
    print("\n",name2," wins.")
else:
    print("\nThe game is draw.")