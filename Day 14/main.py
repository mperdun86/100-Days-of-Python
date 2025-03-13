import random
from art import logo
from art import vs
from game_data import data
def get_choice():
    while True:
        guess = input("Who has more instagram followers? select 'A' or 'B': ").lower().strip()
        print("\n")
        if guess in ('a', 'b'):
            return guess
        else:
            print("Incorrect input")

def influencer_description(selection):
    name = selection['name']
    description = selection['description']
    country = selection['country']
    return f"{name} is a {description} from {country}"

def determine_correct_answer(choice_a, choice_b):
    if choice_a > choice_b:
        return 'a'
    else:
        return 'b'

print(f"{logo}Welcome to the Higher or Lower game!\n")
score = 0
influencer_b = random.choice(data)
game_active = True
while game_active:

    influencer_a = influencer_b
    influencer_b = random.choice(data)

    if influencer_a == influencer_b:
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
        game_active = False








