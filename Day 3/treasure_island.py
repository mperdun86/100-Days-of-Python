print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("your ship has crashed into the rocks outside the island, there is a hole to the right, and the deck to the left.\n"
                "Type \"left\" or \"right\".\n").lower()

if choice1 == "left":
    choice2 = input('you make it out of the ship, do you wait for your rescue crew, or swim . '
                    'Type "wait" to wait for crew. '
                    'Type "swim" to swim to the island.\n').lower()
    if choice2 == "wait":
        choice3 = input("Your crew shows up in the nick of time, and gets you safely to the island. "
                        "There is a cave with 3 doors, blue, yellow, and red. "
                        "Which door do you pick?\n").lower()
        if choice3 == "red":
            print("The room burst into flames, and you are incinerated. Game Over")
        elif choice3 == "yellow":
            print("You Win! All the gold it yours!")
        elif choice3 == "blue":
            print("the room is full of beasts that eat you. Game Over.")
        else:
            print("You picked a nonexistant door! the ghosts of the island are irritated and kill you. Game Over.")
    else:
        print("You got mauled by a trout, how did you let this happen? Game Over.")

else:
    print("You fell in a hole. Game Over.")