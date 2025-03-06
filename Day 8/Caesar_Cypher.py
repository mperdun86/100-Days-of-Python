from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
running = True

print(logo)


def caesar(original_text, shift_amount):
    encrypted_message = ""

    for letter in original_text:
        if letter not in alphabet:
            encrypted_message += letter
        else:
            new_index = ((alphabet.index(letter) + shift_amount) % len(alphabet))
            encrypted_message += alphabet[new_index]

    print(f"Message after {direction}d: {encrypted_message}")


while running:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            break
        else:
            print("Invalid input.")

    text = input("Type your message:\n").lower()

    while True:
        try:
            shift = int(input("Enter a shift number: "))
            break
        except ValueError:
            print("Invalid input.")

    if direction == "decode":
        shift *= -1

    caesar(text, shift)

    while True:
        continue_choice = input("Would you like to continue? Type 'yes' or 'no':\n").lower()

        if continue_choice == "no":
            print("Thank you for using the Caesar Cipher.")
            running = False
            break
        elif continue_choice == "yes":
            break  # exit the loop to continue the program
        else:
            print("Invalid input.")




