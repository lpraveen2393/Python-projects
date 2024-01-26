import random
import sys
from enum import Enum
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

playerchoice=input('Enter \n1. for Rock\n2. for Paper\n3. for Scissors\n\n')
print(playerchoice)

choice =int(playerchoice)
if choice < 1 or choice > 3:
    sys.exit("You must enter 1,2, or 3")

computerchoice =random.choice("123")

computer=int(computerchoice)

print("You chose " + str(RPS(choice)).replace('RPS.','')+".")
print("python  chose " + str(RPS(computer)).replace('RPS.','')+".")
print("")

if choice == 1 and computer == 3:
    print("🥳 You won!")
elif choice == 2 and computer ==1 :
    print("🥳 You won!")
elif choice == 3 and computer == 2:
    print("🥳 You won!")
elif choice == computer:
    print("😲Tie game!")
else:
    print(" 🐍 Python won")

