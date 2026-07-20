import random

if __name__ == "__main__":
    columns = ["a", "b", "c", "d"]
    shipRow = random.randint(1, 4)
    shipColumn = random.choice(columns)
    shipCoord = (shipRow, shipColumn)
    print(shipCoord)
    playerGuesses = []
    attempts = 0

    while True:
        attempts += 1
        print(f"\nAttempt #{attempts}")
        while True:
            while True:
                try:
                    rowGuess = int(input("Please enter a row(1-4): "))
                    break
                except:
                    print("Enter a number 1-4")
            while True:
                columnGuess = input("Please enter a column(a, b, c, d)").strip() .lower()
                if columnGuess == "a" or columnGuess == "b" or columnGuess == "c" or columnGuess == "d":
                    break
                else:
                    print("Please enter one of the following: a, b, c, d")
            if (rowGuess, columnGuess) not in playerGuesses:
                playerGuesses.append((rowGuess, columnGuess))
                break
            else:
                print("Coordinate already guessed, try again")

        if (rowGuess, columnGuess) == shipCoord:
            print("Congrats you sunk the ship!")
            break

    

        