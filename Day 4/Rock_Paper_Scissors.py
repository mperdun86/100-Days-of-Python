import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

while True:
    try:
        user_hand = int(input("Let's play Rock, Paper, Scissors!\nChoose \"0\" for Rock, \"1\" for Paper, and \"2\" for Scissors: "))
        if 0 <= user_hand <= 2:
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")

print(hands[user_hand])
opponent_hand = random.randint(0, 2)
print(hands[opponent_hand])

if user_hand == opponent_hand:
    print("Tied!")
elif (user_hand == 0 and opponent_hand == 2) or (user_hand == 1 and opponent_hand == 0) or (user_hand == 2 and opponent_hand == 1):
    print("Victory!")
else:
    print("You Lose!")
