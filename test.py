import random

def game():
    randomNumber = random.randint(0,9)
    guess = 10
    while randomNumber != guess:
        guess = int(input("Guess number (between 0 and 9)\n"))
        if guess == randomNumber:
            print("BRAVO")
        elif guess >randomNumber:
            print("TOO HIGH")
        else:
            print("TOO LOW")

x = "play"

while x != "exit":
    game()
    x = input("Type 'play' or 'exit'")
    if x == "play" or x == "exit":
        print("")
    else:
        print("Bad choice")
        break
