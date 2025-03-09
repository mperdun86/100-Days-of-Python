from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def get_number_input(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input!")

def get_operation_input():
    while True:
        operation = input("Please choose an operation, please type '+', '-', '*', or '/': ")
        if operation in calculator_functions:
            return operation
        else:
            print("Invalid input!")

def calculator():
    first_number = get_number_input("Please enter the first number: ")

    continue_calculating = True
    while continue_calculating:
        operation = get_operation_input()
        second_number = get_number_input("Please enter the second number: ")

        result = calculator_functions[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        choice = input(f"Would you like to continue using {result}?\nPlease type 'yes', 'no', or type 'exit' to quit the program: ").lower()

        if choice == "yes":
                first_number = result
        elif choice == 'no':
                continue_calculating = False
                calculator()
        elif choice == 'exit':
                input("Thank you for using the Calculator!")
                exit()
        else:
            print("Incorrect input")

calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(logo)
calculator()