import random
from art import logo
from art import vs
from game_data import data

def get_choice():
    """Gets user's guess"""
    while True:
        guess = input("Who has more instagram followers? select 'A' or 'B': ").lower().strip()
        if guess in ('a', 'b'):
            return guess
        else:
            print("Incorrect input.\n")

def continue_game_choice():
    """Allows the user to begin a new game or end the program"""
    while True:
        continue_choice = input("Would you like to play again?\nPlease type 'yes' or 'no': ")
        if continue_choice == 'yes':
            print(logo)
            return 0, True
        elif continue_choice == 'no':
            input("Thank you for playing Higher or Lower!\nPlease hit 'ENTER' to close program")
            return 0, False
        else:
            print("Incorrect input.\n")

def influencer_description(selection):
    """Returns a string with the influencer's name, description, and country"""
    name = selection['name']
    description = selection['description']
    country = selection['country']
    return f"{name} is a {description} from {country}"

def determine_correct_answer(choice_a, choice_b):
    """Determines which influencer has more followers"""
    if choice_a > choice_b:
        return 'a'
    else:
        return 'b'

print(f"{logo}-==Welcome to Higher or Lower!==-\n")
score = 0
influencer_b = random.choice(data)
game_active = True

# Main loop
while game_active:
    influencer_a = influencer_b
    influencer_b = random.choice(data)

    while influencer_a == influencer_b:
        influencer_a = random.choice(data)

    a_followers = influencer_a['follower_count']
    b_followers = influencer_b['follower_count']

    print(f"Choice A: {influencer_description(influencer_a)}\n{vs}\nChoice B: {influencer_description(influencer_b)}")
    correct_answer = determine_correct_answer(a_followers, b_followers)
    choice = get_choice()

    if choice == correct_answer:
        score += 1
        print(f"Correct!\n[Current Score:{score}]\n")
    else:
        print(f"Incorrect! You have lost!\n[Final Score:{score}]")
        score, game_active = continue_game_choice()