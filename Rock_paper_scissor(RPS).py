#Rock Paper and Scissor (RPS) Game

import random

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

# User's Choice
user_choice= int(input('''What do you choose? Enter:
1 for Rock
2 for Paper
3 for Scissors
\n'''))

if 1 <= user_choice <= 3:
    print(f"You Chose: {user_choice}")
    if user_choice == 1:
        print(rock)
    elif user_choice == 2:
        print(paper)
    elif user_choice == 3:
        print(scissors)
    
    # Bot's Choice
    print("Bot chose:")

    bot_choice = random.randint(1, 3)

    if bot_choice == 1:
        print(rock)
    elif bot_choice == 2:
        print(paper)
    elif bot_choice == 3:
        print(scissors)

    # Game Logic
    if user_choice == bot_choice:
        print("It's a draw.")
    elif user_choice == 1 and bot_choice == 3:
        print("You Won!")
    elif user_choice == 2 and bot_choice == 1:
        print("You Won!")
    elif user_choice == 3 and bot_choice == 2:
        print("You Won!")
    else:
        print("You Loose!")
else:
    print("Please enter a valid choice.")
    print("Run the game again for a retry.")