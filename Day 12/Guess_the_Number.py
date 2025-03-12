import random
from art import logo

def set_number():
    return random.randint(1, 100)

def set_difficulty():
    while True:
        difficulty_choice = input("Select a difficulty level\nPlease type 'easy', 'normal', or 'hard': ").lower().strip()
        if difficulty_choice == 'easy':
            return 20
        elif difficulty_choice == 'normal':
            return 10
        elif difficulty_choice == 'hard':
            return 5
        else:
            print("Invalid input.\n")

def attempt_processing(goal, difficulty):
    attempts_remaining = difficulty
    while True:
        try:
            #!!!!!!!!!!!!!CHEAT FOR TESTING!!!!!!!!
            print(f"CHEAT ACTIVE: THE NUMBER IS {goal}")
            print(f"Attempts remaining: {attempts_remaining}")
            guess = int(input("Please guess a number between 1 and 100: ").strip())
            if not(1 <= guess <= 100):
                print("Invalid input.\n")
            else:
                if guess > goal:
                    print("Too high!\n")
                    attempts_remaining -= 1
                    if attempts_remaining <= 0:
                        print("You have lost!\n")
                        return

                elif guess < goal:
                    print("Too low!\n")
                    attempts_remaining -= 1
                    if attempts_remaining <= 0:
                        print("You have lost!\n")
                        return
                else:
                    print("You guessed the answer!\n")
                    return

        except ValueError:
            print("Invalid input.\n")

def main_game_start():
    difficulty = set_difficulty()
    target_number = set_number()
    attempt_processing(target_number, difficulty)

def new_game_choice():
    while True:
        choice = input("Would you like to play again?\nPlease type 'yes' or 'no': ").lower().strip()
        if choice == "yes":
            return
        if choice == "no":
            input("Thank you for playing Guess the Number, please hit enter to shut down the program")
            exit()
        else:
            print("Invalid input.")


# Main Loop
while True:
    print(f"{logo}\nWelcome to Guess the Number!\n")
    main_game_start()
    new_game_choice()



