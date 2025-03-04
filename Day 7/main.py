import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 8

print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

print("Word to guess:" + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"****************************{lives}/8 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in guessed_letters:
        print(f"You already tried \"{guess}\"! Guess again!")
    else:
        guessed_letters.append(guess)
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"There is no \"{guess}\" in the word! You lost a life!")

            if lives == 0:
                game_over = True

                print(f"Oh no! you failed! The word was {chosen_word}!\n***********************YOU LOSE**********************")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(stages[lives])
