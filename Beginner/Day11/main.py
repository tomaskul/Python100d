import random
import art

############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

def deal_card():
    '''Returns a random card from infinite deck.'''
    return random.choice(cards)

def calculate_score(cards_held):
    '''Returns score based on cards_held. Hand with 2 cards totalling 21 returns 0 (Blackjack).'''
    held_sum = sum(cards_held)

    if len(cards_held) == 2 and held_sum == 21:
        return 0
    
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    for card in cards_held:
        if card == 11 and held_sum > 21:
            return held_sum - 10
            

    return sum(cards_held)

def compare(dealer_score, user_score):
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, 
    # then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), 
    # then the user wins. If the user_score is over 21, then the user loses. 
    # If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    if dealer_score == user_score:
        print("It's a draw!")
        return True
    if dealer_score == 0:
        print("Dealer wins! (Blackjack)")
        return True
    if user_score == 0:
        print("You win! (Blackjack)")
        return True
    if user_score > 21:
        print("Dealer wins!")
        return True
    if dealer_score > 21:
        print("You win!")
        return True
    
    return False



print(art.logo)

user_cards = []
dealer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
user_score = calculate_score(user_cards)

dealer_cards.append(deal_card())
dealer_cards.append(deal_card())
dealer_score = calculate_score(dealer_cards)

print(f"You've drawn: {user_cards}\tDealer has drawn [{dealer_cards[0]}, ??]")

exit_condition = False
while not exit_condition:
    exit_condition = compare(dealer_score=dealer_score, user_score=user_score)
    if exit_condition:
        print(f"Your cards: {user_cards}\tDealer cards: {dealer_cards}")
        break

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    deal = input("Would you like to draw another card? (type 'y' or 'n')\t")[0]
    if deal == "y":
        user_cards.append(deal_card())
    
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    exit_condition = compare(dealer_score=dealer_score, user_score=user_score)
    if exit_condition:
        print(f"Your cards: {user_cards}\tDealer cards: {dealer_cards}")
        break

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    if dealer_score < 17:
        dealer_cards.append(deal_card())

    exit_condition = compare(dealer_score=dealer_score, user_score=user_score)
    if exit_condition:
        print(f"Your cards: {user_cards}\tDealer cards: {dealer_cards}")
        break

    if dealer_score > user_score:
        print("Dealer wins!")
        print(f"Your cards: {user_cards}\tDealer cards: {dealer_cards}")
        break
    if user_score > dealer_score:
        print("You win!")
        print(f"Your cards: {user_cards}\tDealer cards: {dealer_cards}")
        break

    

print("\t\t*.*. The end .*.*")

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
#input("\n\n\n\nWould you like to replay?")