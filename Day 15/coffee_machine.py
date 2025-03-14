from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def main_menu():
    """Allows user to pick drink, see machine report, or turn it off."""
    machine_on = True
    while machine_on:
        user_choice = input(
            "What drink would you like?\nPlease type 'espresso', 'latte', or 'cappuccino': ").lower().strip()
        if user_choice in ['espresso', 'latte', 'cappuccino']:
            check_if_available(user_choice)
        elif user_choice == 'report':
            print(f"\n{resources}\n")
        elif user_choice == 'off':
            input("\nPlease press enter to shut down machine")
            machine_on = False
        else:
            print("\nI don't know how to make that!\n")

def check_if_available(drink_to_check):
    """Checks resources to see if enough are there for the requested drink."""
    can_make = True
    for ingredient in resources:
        if ingredient in MENU[drink_to_check]['ingredients']:
            if resources[ingredient] < MENU[drink_to_check]['ingredients'][ingredient]:
                print(f"\nSorry, we cannot make that because we are low on {ingredient}.\n")
                can_make = False
                break
    if can_make:
        print("\nWe can make that!\n")
        payment(drink_to_check)

def validate_float(prompt):
    """Allows programmer to easily validate float inputs."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("\nInvalid input. Please enter a non-negative number.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def payment(drink_to_purchase):
    """Requests number of coins to pay for chosen drink, gives change, or reject amount that is too low."""
    money_added = 0.0
    price = MENU[drink_to_purchase]['cost']
    print(f"It will be {price:.2f} please.")

    quarters = validate_float("How many quarters?: ")
    money_added += 0.25 * quarters
    dimes = validate_float("How many dimes?: ")
    money_added += 0.10 * dimes
    nickels = validate_float("How many nickels?: ")
    money_added += 0.05 * nickels
    pennies = validate_float("How many pennies?: ")
    money_added += 0.01 * pennies

    money_added = round(money_added, 2)
    price = round(price, 2)

    if money_added > price:
        change = round(money_added - price, 2)
        print(f"Thank you! Your change is {change:.2f}")
        make_drink(price, drink_to_purchase)
    elif money_added == price:
        print("Thank you!")
        make_drink(price, drink_to_purchase)
    else:
        print("\nSorry, you do not have enough money.\n")

def make_drink(money_to_add, drink_to_make):
    """Removes ingredients needed for drink, and adds payment to resources."""
    for ingredient, amount in MENU[drink_to_make]['ingredients'].items():
        resources[ingredient] -= amount

    resources['money'] += money_to_add
    print(f"\nEnjoy your {drink_to_make}! ☕\n")

#START THE PROGRAM
main_menu()










