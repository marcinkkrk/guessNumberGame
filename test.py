# menu = int(input("1. Zagraj\n2. Wyjdź\n"))
#

x = 1
while x == 1:
    print("Player 1 choice:\n1. Rock\n2. Paper\n3. Scissors\n")
    player1choice = int(input())
    print("Player 2 choice:\n1. Rock\n2. Paper\n3. Scissors\n")
    player2choice = int(input())
    if player2choice & player1choice > 3:
        print("Zły wybór")
        break
    else:
        if player1choice == 1:
            if player2choice == 1:
                print("Both players have rock, its draw")
            elif player2choice == 2:
                print("Player 2 won with his paper against player 1 rock")
            elif player2choice == 3:
                print("Player 1 won with his rock against player 2 scissors")
        elif player1choice == 2:
            if player2choice == 2:
                print("Both players have paper, its draw")
            elif player2choice == 1:
                print("Player 1 won with his paper against player 2 rock")
            elif player2choice == 3:
                print("Player 2 won with his scissors against player 1 paper")
        elif player1choice == 3:
            if player2choice == 3:
                print("Both players have scissors, its draw")
            elif player2choice == 1:
                print("Player 2 won with his rock against player 1 scissors")
            elif player2choice == 2:
                print("Player 1 won with his scissors against player 2 paper")

    x = int(input("1. Graj dalej\n2. Wyjdź\n"))





