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

choice_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))

computer_play = random.randint(0, 2)
#print(computer_play)

if choice_input == 0 and computer_play == 2:
    print("You win!")
elif computer_play > choice_input:
    print("You lose!")
elif computer_play == choice_input:
    print("You tie!")
else:
    print("You win!")