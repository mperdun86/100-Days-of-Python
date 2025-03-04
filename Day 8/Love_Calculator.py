print("Welcome to the Love Calculator!")
name1 = input("Please enter the first person's name: ")
name2 = input("Please enter the second person's name: ")

def calculate_love_score(name1, name2):
    digit1 = 0
    digit2 = 0
    word1 = "true"
    word2 = "love"
    both_names = (name1+name2).lower()
    for letter in both_names:
        if letter in word1:
            digit1 += 1
        if letter in word2:
            digit2 += 1

    score = (str(digit1) + str(digit2))
    print(f"The love score between {name1} and {name2} is {score}%!")

calculate_love_score(name1, name2)




