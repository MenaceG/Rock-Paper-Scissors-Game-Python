import random
from traceback import print_tb

lives = 0
user_win = 0
computer_win = 0
options = ["Rock", "Paper", "Scissors"]

lives = int(input("Select Lives: "))

while lives != 0:
    user_input = input("Choose Rock, Paper or Scissors: ")
    user_input = user_input.capitalize()
    if user_input not in options:
        print("Select Correct Option")
        continue

    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print("Computer Choosed " + computer_choice)

    if user_input== computer_choice:
        print("Draw")
        user_win = 0

    elif user_input== "Paper" and computer_choice == "Rock":
        print("You Won")
        user_win += 1
    elif user_input == "Rock" and computer_choice == "Scissors":
        print("You Won")
        user_win += 1
    elif user_input == "Scissors" and computer_choice == "Paper":
        print("You Won")
        user_win += 1
    
    else:
        print("You Lost, Computer Won")
        computer_win += 1
        lives -= 1

print("Your Score is ", user_win)
print("Computer Score is ", computer_win)








