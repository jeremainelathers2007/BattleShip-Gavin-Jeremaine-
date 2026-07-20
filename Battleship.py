import random

if __name__ == "__main__":
    print("--Welcome to Battleship--")
    while True:
        boardSize = int(input("What do you want the sidelength of board to be(min of 4, max of 10): "))
        if boardSize == 4 or boardSize == 5 or boardSize == 6 or boardSize == 7 or boardSize == 8 or boardSize == 9 or boardSize == 10:
            break
        else:
            print("Please enter a valid side length(as a single number)")
    
    rows = []
    rowCounter=1
    for a in range(boardSize):
        rows.append(rowCounter)
        rowCounter+=1

    columns = []
    for c in range(boardSize):
        columns.append(0)

    boardCounter = 1
    board = {}
    for b in range(boardSize):
        board[boardCounter] = columns
        boardCounter +=1

    shipRow = random.randint(1, boardSize)
    shipColumn = random.choice(columns)
    shipCoord = (shipRow, shipColumn)
    print(shipCoord)
    playerGuesses = []
    attempts = 0
    
    startingCounter = 1
    print("Starting Board:")
    for row in range(boardSize):
        print(board[startingCounter])
        startingCounter +=1

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

    

    

        