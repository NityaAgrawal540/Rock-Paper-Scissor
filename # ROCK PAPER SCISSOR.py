# ROCK PAPER SCISSOR
# INSERT USER (ROCK,PAPER,SCISSOR) 
#COMPUTER CHOICE (RANDOM AND NOT CONDITIONAL)

# CASES
#CASE 1 ROCK 
# ROCK - ROCK = TIE 
#ROCK - SCISSOR = WIN
#ROCK - PAPER - LOOSE 

#CASE 2 PAPER
# PAPER - PAPER = TIE
# PAPER - ROCK = WIN
# PAPER - SCISSOR = LOOSE

# CASE 3 SCISSOR
# SCISSOR - SCISSOR = TIE
#SCISSOR - PAPER = WIN
# SCISSOR - ROCK = LOOSE


import random 
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock , paper, scissor) = ")
computer_choice = random.choice(item_list)

print(f"User_choice = {user_choice}, Computer_choice = {computer_choice}" )

# CONDITIONS 

if user_choice == computer_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")