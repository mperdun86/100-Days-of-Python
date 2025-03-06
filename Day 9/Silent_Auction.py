import os
from art import logo

bidding_list = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    winner = ""
    winning_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = bidder
    print(f"{winner} is the winner, with a bid of ${winning_bid}")

print(logo)
print("------=========] Welcome to the Silent Auction [=========------")

while True:
    name = input("Please enter your name: ")

    while True:
        try:
            bid = int(input("Please enter your bid: $"))
            bidding_list[name] = bid
            break
        except ValueError:
            print("Incorrect input - Must be a whole number")

    while True:
        choice = input("Would someone else like to place a bid? Please type 'yes' or 'no': ").lower()
        if choice in ["yes", "no"]:
            break
        print("Incorrect input - Please type 'yes' or 'no'")

    if choice == "no":
        clear_screen()
        find_highest_bidder(bidding_list)
        break

    clear_screen()


