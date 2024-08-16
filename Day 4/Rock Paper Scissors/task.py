rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
'''
player_guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors\n"))
computer_guess = random.randint(0, 2)
print(player_guess, computer_guess)
if player_guess == 1 and computer_guess == 0:
    print(paper)
    print("Computer chose\n", rock)
    print("You win")
elif player_guess == 0 and computer_guess == 1:
    print(rock)
    print("Computer chose\n", paper)
    print("You lose")
elif player_guess == 2 and computer_guess == 0:
    print(scissors)
    print("Computer chose\n", rock)
    print("You lose")
elif player_guess == 0 and computer_guess == 2:
    print(rock)
    print("Computer chose\n", scissors)
    print("You win")
elif player_guess == 1 and computer_guess == 2:
    print(paper)
    print("Computer chose\n", scissors)
    print("You lose")
elif player_guess == 2 and computer_guess == 1:
    print(scissors)
    print("Computer chose\n", paper)
    print("You win")
elif player_guess == 0 and computer_guess == 0:
    print(rock)
    print("Computer chose\n", rock)
    print("It's a Draw match.")
elif player_guess == 1 and computer_guess == 1:
    print(paper)
    print("Computer chose\n", paper)
    print("It's a Draw match.")
elif player_guess == 2 and computer_guess == 2:
    print(scissors)
    print("Computer chose\n", scissors)
    print("It's a Draw match.")
else:
    print("Invalid guess. Try again!")
    '''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")











