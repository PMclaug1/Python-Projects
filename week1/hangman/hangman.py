import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
used_letters = []


print(logo)

# create blanks for guesses

display = []

for char in chosen_word:
    display.append("_")

#for char in chosen_word:
#   display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter. ").lower()

#check guessed letter
    for char in range(word_length):
        letter = chosen_word[char]
        if letter == guess:
            display[char] = letter
            used_letters += guess
            print(f" Used letters: {used_letters}")
    if guess not in chosen_word:
        lives -= 1
        used_letters += guess
        print(f" Used letters: {used_letters}")
        if lives == 0:
            end_of_game = True
            print(chosen_word)
            print("You lose. Good day sir!")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(stages[lives])






