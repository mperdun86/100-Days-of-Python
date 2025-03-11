import random
from operator import truediv

from art import logo

print(f"{logo}\nWelcome to guess the number!\n")

def set_number():
    return random.randint(1, 100)

def set_difficulty():
    while True:
        difficulty_choice = input("Select a difficulty level\nPlease type 'easy', 'normal', or 'hard").lower().strip()
        if difficulty_choice == 'easy':
            return 20
        elif difficulty_choice == 'normal':
            return 10
        elif difficulty_choice == 'hard':
            return 5
        else:
            print("Invalid input!")

def attempt_processing(goal):
    while True:
        #!!!!!!!!!!!!!!!!!!!!!!LEFT OFF HERE!!!!!!!!!!!!!!!!!!!!!!!
        Guess = input("Please guess a number.")


def main_game_loop():
    attempts = set_difficulty()
    target_number = set_number()
    game_active = True
    while game_active:
        attempt_processing(target_number)





