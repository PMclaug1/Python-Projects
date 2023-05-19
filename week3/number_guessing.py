import random

logo = """
 _______               ___.                    ________                                          
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______ ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___// __ \_  __ \
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \\  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >\___  >__|   
        \/            \/    \/     \/                \/            \/     \/     \/     \/       
"""


target = random.randint(0,100)
EASY_GUESSES = 10
HARD_GUESSES = 5
print(logo)
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
def set_difficulty():
    if difficulty == 'easy':
        return EASY_GUESSES
    elif difficulty == 'hard':
        return HARD_GUESSES
    else:
        print("Invalid selection.")

def guess_a_number():
    guesses = set_difficulty()    
    while guesses > 0:
        guess = int(input("Make a guess. "))
        if guess > target:
            print("Too high, guess again.")
            guesses -= 1
            print(f"You have {guesses} attempts to guess the number.") 
        elif guess < target:
            print("Too low, guess again.")
            guesses -= 1
            print(f"You have {guesses} attempts to guess the number.")
        else:
            print("You win!")
            break

    
guess_a_number()
