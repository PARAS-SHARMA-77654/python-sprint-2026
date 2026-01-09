import random

user = 0
computer = 0

name = input("ENTER YOUR NAME: ")
rounds = int(input("ENTER NUMBER OF ROUNDS: "))

for i in range(rounds):
    user_choice = input("Enter your move (rock, paper, scissor): ").strip().lower()
    
    number = random.randint(1, 3)
    if number == 1:
        computer_move = "paper"
    elif number == 2:
        computer_move = "rock"
    else:
        computer_move = "scissor"
    
    # Determine winner
    if user_choice == computer_move:
        result = "Tie"
    elif (user_choice == "rock" and computer_move == "scissor") or \
         (user_choice == "paper" and computer_move == "rock") or \
         (user_choice == "scissor" and computer_move == "paper"):
        result = "You win"
        user += 1
    else:
        result = "You lose"
        computer += 1
    
    print("Computer chose:", computer_move)
    print("Result:", result)
    print("-----------------------------")

# Final scoreboard
print("-------------SCOREBOARD-----------------")
print(name, ":", user)
print("Computer :", computer)
