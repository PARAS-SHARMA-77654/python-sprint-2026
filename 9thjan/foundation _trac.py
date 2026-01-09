user_choice=input("enter your move (rock,paper,scissor):")
import random
number = random.randint(1, 3)
if number==1:
    computer_move="paper"
elif number==2:
    computer_move="rock"
else:
    computer_move="scissor"




#win/wrong -----conditional
if user_choice==computer_move:
    result="tie"
elif user_choice=="rock" and computer_move=="scissor" or user_choice=="paper" and computer_move=="rock" or user_choice=="scissor" and computer_move=="paper":
    result=" you win"
else:
    result=" you loss"




          
print("YOUR MOVE:",user_choice)
print("COMPUTER MOVE:",computer_move)
print("RESULT:",result)
