import random

def game():
    randomNumber = random.randint(0,9)
    numberOfChoices = 0
    guess = 10
    while randomNumber != guess:
        numberOfChoices += 1
        guess = int(input("Guess number (between 0 and 9)\n"))
        if guess == randomNumber:
            print("BRAVO")
            print(f"You needed {numberOfChoices} choices")
        elif guess >randomNumber:
            print("TOO HIGH")
        else:
            print("TOO LOW")

x = "play"
while x != "exit":
    game()
    x = input("Type 'play' or 'exit'\n")
    if x == "play" or x == "exit":
        print("")
    else:
        print("Bad choice")
        break
