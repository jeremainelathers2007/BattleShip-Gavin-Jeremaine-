import random

if __name__ == "__main__":
    print("--Welcome to Battleship--")
    while True:
        boardSize = int(input("What do you want the sidelength of board to be(min of 4, max of 10): "))
        if 4<= boardSize <= 10:
            break
        else:
            print("Please enter a valid side length(as a single number)")
    
    rows = []
    rowCounter=1
    for a in range(boardSize):
        rows.append(rowCounter)
        rowCounter+=1

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    usableLetters = []
    for e in range(boardSize):
        usableLetters.append(letters[e])
    columns = []
    for c in range(boardSize):
        columns.append(0)

    boardCounter = 1
    board = {}
    for b in range(boardSize):
        board[boardCounter] = columns
        boardCounter +=1
    while True:
        placementQ = input("Do you want to place your own ships or have them randomly placed? ")
        if placementQ == "place" or placementQ == "random":
            break
        else:
            print("Try saying 'place' to place your own ships or 'random' to have them placed for you. ")
    
    shipLocations = []
    if placementQ == "random":
        for d in range(boardSize//2):
            while True:
                shipRow = random.randint(1, boardSize)
                shipColumn = random.choice(usableLetters)
                shipCoord = (shipRow, shipColumn)
                if shipCoord not in shipLocations:
                    shipLocations.append(shipCoord)
                    break
        print(shipLocations)

    if placementQ == "place":
        for d in range(boardSize//2):
            while True:
                while True:
                    shipRow = int(input(f"What row do you want the ship to be on (1-{boardSize}: )"))
                    if 1<=shipRow<=boardSize:
                        break
                    else:
                        print("Try a valid integer in the range")
                while True:
                    shipColumn = input(f"What column do you want to place your ship on {usableLetters}: ")
                    if shipColumn in usableLetters:
                        break
                    else:
                        print("Try a valid letter.")
                shipCoord = (shipRow, shipColumn)
                if shipCoord not in shipLocations:
                    shipLocations.append(shipCoord)
                    break
        print(shipLocations)
    
    playerGuesses = []
    attempts = 0
    
    startingCounter = 1
    print("Starting Board:")
    for row in range(boardSize):
        print(board[startingCounter])
        startingCounter +=1

    while True and attempts <= 5:
        columnNum = 0
        attempts += 1
        print(f"\nAttempt #{attempts}")
        while True:
            while True:
                try:
                    rowGuess = int(input(f"Please enter a row(1-{boardSize}): "))
                    if 1<=rowGuess<=boardSize:
                        break
                except:
                    print(f"Enter a number 1-{boardSize}")
            while True:
                columnGuess = input(f"Please enter a column{usableLetters}").strip() .lower()
                if columnGuess == "a":
                    columnNum += 0
                if columnGuess == "b":
                    columnNum += 1
                if columnGuess == "c":
                    columnNum += 2
                if columnGuess == "d":
                    columnNum += 3
                if columnGuess == "e":
                    columnNum += 4
                if columnGuess == "f":
                    columnNum += 5
                if columnGuess == "g":
                    columnNum += 6
                if columnGuess == "h":
                    columnNum += 7
                if columnGuess == "i":
                    columnNum += 8
                if columnGuess == "j":
                    columnNum += 9
                elif columnGuess in usableLetters:
                    break
                else:
                    print("Please enter one of the following: a, b, c, d")
            if (rowGuess, columnGuess) not in playerGuesses:
                playerGuesses.append((rowGuess, columnGuess))
                board[rowGuess][columnNum] += 1
                updatedCounter = 1
                print("Updated Board:")
                for row in range(boardSize):
                    print(board[updatedCounter])
                    updatedCounter +=1
                break
            else:
                print("Coordinate already guessed, try again")

        if (rowGuess, columnGuess) == shipCoord:
            board[rowGuess][columnNum] += 1
            finalCounter = 1
            print("Final Board:")
            for row in range(boardSize):
                print(board[finalCounter])
                finalCounter += 1
            print("Congrats you sunk the ship!")
            break
        else:
            print("You missed! Try Again")