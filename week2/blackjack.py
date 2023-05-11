import art4
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

print(art4.logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():
    def deal_card():
        card = random.choice(cards)
        return card

    def calc_total(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    player_cards = []
    dealer_cards = []
    should_continue = True

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    player_points = calc_total(player_cards)
    dealer_points = calc_total(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_points}.")
    print(f"Dealer's first card {dealer_cards[0]}")

    if player_points == 0 or dealer_points == 0 or player_points > 21:
        should_continue = False

    hit = input("Do you want to be dealt another card? Type 'y' or 'n'. ").lower()
    while hit == "y":
        player_cards.append(deal_card())
        player_points = calc_total(player_cards)
        if player_points > 21:
            print(f"{player_points}. Bust! You lose.")
            break
        print(f"Your cards: {player_cards}, current score: {player_points}.")
        hit = input("Do you want to be dealt another card? Type 'y' or 'n'. ").lower()

    while dealer_points < 17 and dealer_points != 0:
        dealer_cards.append(deal_card())
        dealer_points = calc_total(dealer_cards)
        if dealer_points > 21:
            print(f"{dealer_points} Dealer busts.")
            break

    def compare_totals(player_points, dealer_points):
        print(f"Player has {player_points}, dealer has {dealer_points}")
        if player_points == dealer_points:
            return "Tie game."
        elif player_points > dealer_points:
            return "You win."
        elif dealer_points > player_points:
            return "Dealer wins."
        elif dealer_points > 21:
            return "Dealer busts. You win."
        elif player_points > 21:
            return "You bust and lose."
    
    print(compare_totals(player_points, dealer_points))

play_blackjack()
play_continue = True
while play_continue:
    another_game = input("Play another game? Type 'y' or 'n'. ")
    if another_game == 'y':
        print(art4.logo)
        play_blackjack()
    else:
        print("Thanks for playing.")
        break