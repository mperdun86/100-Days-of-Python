import random
from resources import logo
from resources import rules

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []

def deal_cards(hand, num_of_cards):
    """Used to add cards to a hand."""
    hand.extend(random.choices(cards, k=num_of_cards))

def calculate_score(hand):
    """Used for adjusting the value of an ace, and for checking for blackjack in initial deal."""
    score = sum(hand)
    if 11 in hand and 10 in hand:
        return 0
    elif score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def initial_deal():
    """Sets initial state of game by clearing all hands, redrawing, and checking for blackjack."""
    user_hand.clear()
    dealer_hand.clear()

    deal_cards(user_hand, 2)
    deal_cards(dealer_hand, 2)

    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score == 0:
        print(f"Dealer has Blackjack: {dealer_hand}. You lose!\n")
        return
    elif user_score == 0:
        print(f"You have Blackjack: {user_hand}. You win!\n")
        return
    user_round()


def user_round():
    """Allows the user to hit or stand, then either busting or leading to dealers turn"""
    while True:
        user_score = calculate_score(user_hand)
        print(f"Your hand: {user_hand} Total: {sum(user_hand)} | Dealer's hand: [{dealer_hand[0]}, ?]")
        if user_score > 21:
            print(f"You BUSTED! Your total was {user_score}.")
            return

        user_round_choice = input("\nWould you like to hit or stand?\nPlease type 'hit' or 'stand': ").lower()
        if user_round_choice == "hit":
            deal_cards(user_hand, 1)
        elif user_round_choice == "stand":
            print("Now it is the dealer's turn.")
            dealer_round()
            return
        else:
            print("Invalid input! Try again.")
            continue

def dealer_round():
    """Allows the dealer to draw until bust or dealer score >=16"""
    while True:
        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21:
            print(f"Dealer BUSTED with {dealer_hand}, totaling {dealer_score}! You win!\n")
            return
        elif dealer_score <= 17:
            print("Dealer draws a card...")
            deal_cards(dealer_hand, 1)
        else:
            break
    final_evaluation()

def final_evaluation():
    """Calculates the victor"""
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your hand: {user_hand} ({user_score}) | Dealer's hand: {dealer_hand} ({dealer_score})")
    if user_score > 21:
        print("You BUSTED! Dealer wins.")
    elif dealer_score > user_score:
        print("Dealer wins.")
    elif dealer_score > 21 or user_score > dealer_score:
        print("You WIN!")
    else:
        print("It's a tie!")

# MAIN LOOP
while True:
    main_loop_choice = input("Would you like to play a new round of Blackjack? You can also check the rules.\nPlease type 'yes', 'no', or 'rules': ").lower()
    if main_loop_choice == "yes":
        print("\n" * 100 + logo)
        initial_deal()
    elif main_loop_choice == "no":
        print("Thanks for playing Blackjack!")
        break
    elif main_loop_choice == "rules":
        print(rules)
    else:
        print("Invalid input!")