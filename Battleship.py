import random

if __name__ == "__main__":
    print("--Welcome to Battleship--")
    while True:
        boardSize = input("What size do you want the board to be(min of 4x4, max of 10x10): ")
        if boardSize == "4x4" or boardSize == "5x5" or boardSize == "6x6" or boardSize == "7x7" or boardSize == "8x8" or boardSize == "9x9" or boardSize == "10x10":
            break
        else:
            print("Please enter your board size in the proper format, i.e. 4x4, 5x5, 6x6 ...")
      
    if boardSize == "4x4":
        board = {
            1: [0, 0, 0, 0],
            2: [0, 0, 0, 0],
            3: [0, 0, 0, 0],
            4: [0, 0, 0, 0]
        }
        columns = ["a", "b", "c", "d"]
        shipRow = random.randint(1, 4)
    if boardSize == "5x5":
        columns = ["a", "b", "c", "d", "e"]
        shipRow = random.randint(1, 5)
    if boardSize == "6x6":
        columns = ["a", "b", "c", "d", "e", "f"]
        shipRow = random.randint(1, 6)
    if boardSize == "7x7":
        columns = ["a", "b", "c", "d", "e", "f", "g"]
        shipRow = random.randint(1, 7)
    if boardSize == "8x8":
        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        shipRow = random.randint(1, 8)
    if boardSize == "9x9":
        columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        shipRow = random.randint(1, 9)
    if boardSize == "10x10":
        columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        shipRow = random.randint(1, 10)
    shipColumn = random.choice(columns)
    shipCoord = (shipRow, shipColumn)
    print(shipCoord)
    playerGuesses = []
    attempts = 0
    
    print(f"Starting Board: \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")

    while True:
        columnNum = 0
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
                if columnGuess == "a":
                    columnNum += 0
                if columnGuess == "b":
                    columnNum += 1
                if columnGuess == "c":
                    columnNum += 2
                if columnGuess == "d":
                    columnNum += 3
                elif columnGuess == "a" or columnGuess == "b" or columnGuess == "c" or columnGuess == "d":
                    break
                else:
                    print("Please enter one of the following: a, b, c, d")
            if (rowGuess, columnGuess) not in playerGuesses:
                playerGuesses.append((rowGuess, columnGuess))
                board[rowGuess][columnNum] += 1
                print(f"Updated Board: \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")
                break
            else:
                print("Coordinate already guessed, try again")

        if (rowGuess, columnGuess) == shipCoord:
            board[rowGuess][columnNum] += 1
            print(f"Final Board: \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")
            print("Congrats you sunk the ship!")
            break
        else:
            print("You missed! Try Again")

        else:
            print("You missed try again.")

    

        