print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))

tip_amount = round(bill * tip/100, 2)
total = tip_amount + bill
split = total / people

print(f"At {tip}%, the total tip is ${tip_amount:.2f}, which equals a total of ${total:.2f}\nWhen split amongst {people} people, each person should pay ${split:.2f}")




