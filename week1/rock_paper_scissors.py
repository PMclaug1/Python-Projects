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

game_images = [rock, paper, scissors]

choice_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))

if choice_input < 3 and choice_input > 0:
    print(game_images[choice_input])

computer_play = random.randint(0, 2)

if choice_input < 3 and choice_input > 0:
    print(f"Computer chose {computer_play} {game_images[computer_play]}")


if choice_input >= 3 or choice_input < 0:
    print("You selected an invalid number.")
elif choice_input == 0 and computer_play == 2:
    print("You win!")
elif computer_play == 0 and choice_input == 2:
    print("You lose!")
elif computer_play > choice_input:
    print("You lose!")
elif choice_input > computer_play:
    print("You lose!")
elif computer_play == choice_input:
    print("You tie!")
