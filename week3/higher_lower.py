import art
from game_data import data
import random

# higher/lower game - compares who has more instagram followers
# 1. start game with logo and first comparison
# 2. second logo/art and 2nd half of the comparison
# 3. Chooose a or b and compare followers from data file
# 4. If incorrect, break. If correct show correct and increment score
# 5. continue until an incorrect answer
# 6. when continuing move B answer to A and get a new B from list randomly

print(art.logo)

def play_game():
    player_score = 0
    a_comparison = random.choice(data)
    b_comparison = random.choice(data)
    if a_comparison == b_comparison:
        b_comparison = random.choice
    should_continue = True

    while should_continue:
        print(f"Compare A: {a_comparison['name']}, a {a_comparison['description']}, from {a_comparison['country']}.")
        print(art.vs)
        print(f"Against B: {b_comparison['name']}, a {b_comparison['description']}, from {b_comparison['country']}.")
        choice = input("Who has more followers? Type 'A' or 'B'? ").upper()
    
        if choice == 'B':
            print(f"{b_comparison['follower_count']} > {a_comparison['follower_count']}")
            if b_comparison['follower_count'] > a_comparison['follower_count']:
                player_score += 1
                print(f"You're right! Current score: {player_score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {player_score}")
                should_continue = False
        else:
            print(f"{a_comparison['follower_count']} > {b_comparison['follower_count']}")
            if a_comparison['follower_count'] > b_comparison['follower_count']:
                player_score += 1
                print(f"You're right! Current score: {player_score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {player_score}")
                should_continue = False
        a_comparison = b_comparison
        b_comparison = random.choice(data)

play_game()