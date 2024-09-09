import random
import time

choices = ["rock", "paper", "scissiors"]
player_choices = ['rock','paper','scissors']
user_input = ""
user_score = 0
ai_score = 0

ai = random.choice(choices)



print("Hi")
#time.sleep(1)
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

print("You have selected: " + user_input)
print(ai)

if user_input == ai:
    print("Your choice: " + user_input)
    print("Computer's choice: " + ai)
    print("The game is a tie")
elif user_input == 'rock':
    if ai == "paper":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You loose !")
        ai_score += 1
    elif ai == "scissors":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You win !")
        user_score += 1
elif user_input == 'paper':
    if ai == "scissors":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You loose !")
        ai_score += 1
    elif ai == "rock":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You win !")
        user_score += 1                 
elif user_input == 'scissors':
    if ai == "rock":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You loose !")
        ai_score += 1
    elif ai == "paper":
        print("Your choice: " + user_input)
        print("Computer's choice: " + ai)
        print("You win !") 
        user_score += 1
        print("Player score: " + str(user_score) + "Computer score: " + str(ai_score))

