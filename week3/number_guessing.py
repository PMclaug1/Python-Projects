import random

logo = """
 _______               ___.                    ________                                          
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______ ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___// __ \_  __ \
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \\  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >\___  >__|   
        \/            \/    \/     \/                \/            \/     \/     \/     \/       
"""

def number_guesser():
    target = random.randint(0,100)
    print(logo)
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    def guess_a_number():
        guess = input("Make a guess. ")
        while guesses > 0:
            if guess > target:
                print("Too high, guess again.")
                print(f"You have {guesses} attempts to guess the number.")
                guesses = guesses - 1
                guess_a_number()
            elif guess < target:
                print("Too low, guess again.")
                print(f"You have {guesses} attempts to guess the number.")
                guesses = guesses - 1
                guess_a_number()
            else:
                print("You win!")
                break
    if difficulty == 'easy':
        guesses = 10
        print(f"You have {guesses} attempts to guess the number.")
        guess_a_number()
    elif difficulty == 'hard':
        guesses = 5
        print(f"You have {guesses} attempts to guess the number.")
        guess_a_number()
    else:
        print("Invalid selection.")

number_guesser()