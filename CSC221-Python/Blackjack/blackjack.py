#Matthew Cerniglia
#BlackJack
#Complete Project
#LF298.CSC.221.100V.SP26

#This program is simulating the game of blackjack. The objective is to get the total of your hand as close to 21 as possible without going over (busting).
#The player competes against the dealer, and the one with the higher hand value wins, unless one of them busts. 
#The program creates a deck of cards, deals hands to the player and dealer, calculates hand values, and simulates the game by dealing additional cards until a winner is determined.

#used to shuffle the deck of cards to ensure a random order for each game.
import random

#used to create the deck of cards by combining ranks and suits, and to generate the full 52-card deck.
import itertools

#suits is the variable used to store the four options of suits a card can be: '♥', '♦', '♣', '♠'
#ranks is the variable used to store the number or letter value for the cards, being multiplied by 4 to account for the four suits
#deck is the variable used to store the full deck of cards.
#this function creates a 52-card deck, 13 values for each 4 suits, the deck is then shuffled to esnure a random order in the game.
#Deck using the itertools.product function to combine the ranks and suits.
def create_deck():
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    deck = list(itertools.product(ranks, suits))
    random.shuffle(deck)
    return deck

#player_hand is the variable used to create the list for the players hand.
#dealer_hand is the variable used to create the list for the dealers hand.
#this function deals two cards to both the player and the dealer, then saves the new lists with the two cards each added to the respective variables. 
#The cards are removed from the deck using the pop() method.
def first_deal(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

#value is the variable used to keep track of the total value of the hand, starting at 0 to signify no starting value.
#aces is initally set to 0 as it can be used for 1 or 11 depending if that will make player/dealer bust or not.
def calculate_hand_value(hand):
    value = 0
    aces = 0

#setting the value of face cards (J,Q,K) to 10.
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            value += 10

#setting the value of Aces to 11 if it doesn't cause a bust, otherwise setting it to 1.
        elif rank == 'A':
            if value + 11 <= 21:
                value += 11
            if value > 21:
                value += 1        
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1

#returning the total value of the hand after calculating the values of all cards and adjusting for Aces if necessary.
    return value


#this function displays the player and dealer cards and total value, also checking for Blackjack (21) for both.
def display_hands(player_hand, dealer_hand):
    print("Player's Hand:", player_hand, "Value:", calculate_hand_value(player_hand))
    print("Dealer's Hand:", dealer_hand, "Value:", calculate_hand_value(dealer_hand))
 
 #this is the part of the function that checks for blackjack.
    if player_hand == 21:
        print("Player has Blackjack!")
    if dealer_hand == 21:
        print("Dealer has Blackjack!")


#deck is the variable created using the create_deck() function
#player_hand and dealer_hand are initialized with the first_deal() function, and the hands are displayed using the display_hands() function.
#this function simulates the game by dealing a card to player then dealer, and stopping when either hand is equal or more than 21.
#the winner will be determined by comparing the hand values, with checks for busts and ties (pushes) included.
def simulate_game():
    deck = create_deck()
    player_hand, dealer_hand = first_deal(deck)
    display_hands(player_hand, dealer_hand)

#checking that both hands are less than 21 before dealing additional cards.
    while calculate_hand_value(player_hand) < 21 and calculate_hand_value(dealer_hand) < 21:
            player_hand.append(deck.pop())
            print("Player hits, card dealt:", player_hand[-1], "Total:", calculate_hand_value(player_hand))

#after the card is dealt, it does a check to see if the player has busted (hand value over 21), if so the dealer wins and the game ends.
# If not, the dealer is dealt a card and a similar check is done for the dealer.
#If neither busts, the hands are displayed again and the loop continues until one of them busts or both reach 21.
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins!")
                return
            dealer_hand.append(deck.pop())
            print("Dealer hits, card dealt:", dealer_hand[-1], "Total:", calculate_hand_value(dealer_hand))
            if calculate_hand_value(dealer_hand) > 21:
                print("Dealer busts! Player wins!")
                return
            display_hands(player_hand, dealer_hand)

#if it reaches this point (which in theory would not happen as either player or dealer would have busted or reached 21) it means neither player nor dealer has busted.
#Their hand values are compared to determine the winner, or if it's a tie (push).
    if calculate_hand_value(player_hand) == 21 and calculate_hand_value(dealer_hand) == 21:
        print("Both player and dealer have 21! It's a push (tie)!")
    else:
        if calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
            print("Player wins!")
        elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
            print("Dealer wins!")
        else:
            print("It's a push (tie)!")

#the main block of the program calls the simulate_game() function to start the game when the script is run.
if __name__ == "__main__":
    simulate_game()