import random
import time


user_score = 0
ai_score = 0 #This represents the computer's choice

while True:

    choices = ["rock", "paper", "scissors"]
    player_choices = ['rock','paper','scissors']
    user_input = ""
    
    ai = random.choice(choices)



    print("Hi")
    time.sleep(1)
    print("Welcome to Rock Paper Scissiors !")
    for i in range(33):
        print("#", end="")

    time.sleep(2)
    print("\nTo play choose either Rock, Paper or Scissors")
    print("Type in your choice bellow")
    time.sleep(1)
    user_input = None

    while user_input not in player_choices:
        user_input = input("Type you choice here! : ").lower()

    if user_input == ai:
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("The game is a tie")
        print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))
    elif user_input == 'rock':
        if ai == "paper":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You loose !")
            ai_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))
        elif ai == "scissors":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You win !")
            user_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))
    elif user_input == 'paper':
        if ai == "scissors":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You loose !")
            ai_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))
        elif ai == "rock":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You win !")
            user_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))                 
    elif user_input == 'scissors':
        if ai == "rock":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You loose !")
            ai_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))
        elif ai == "paper":
            print("Your choice: " + user_input)
            print("Computer's choice: " + ai)
            print("You win !") 
            user_score += 1
            print("Player score: " + str(user_score) + " Computer score: " + str(ai_score))

    continue_game = input("Do you want to continue ? (yes/no): ").lower()

    if continue_game != "yes":
        break

print("Thanks for Playing !")    



