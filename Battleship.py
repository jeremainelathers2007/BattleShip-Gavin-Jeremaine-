#Names: Gavin and Jeremaine

import random
playerShips = {}
allPlayerCoords = []
shipNumber = 2
shipSize = [1,2]
computerShips = {}
allComputerCoords = []

def createBoard(size, userBoard):
    userBoard.clear()
    boardCounter = 1
    for c in range(size):
        columns = []
        for f in range(size):
            columns.append(0)
        userBoard[boardCounter] = columns
        boardCounter +=1

def shipPlacement(shipCount, shipSize, userShips, allUserCoords):

    vOrH = ["horizontal", "vertical"]
    uOrD = ["up", "down"]
    lOrR = ["left", "right"]

    for ship in range(shipCount):
        if shipSize[ship] == 1:
            while True:
                userShipRow = random.randint(1, boardSize)
                userShipColumn = random.choice(usableLetters)
                single = (userShipRow, userShipColumn)
                if single not in allUserCoords:
                    userShips["dinghy"] = single
                    allUserCoords.append(single)
                    break

        if shipSize[ship] > 1:
            while True:
                biggerShip = []
                bigShipRow = random.randint(1, boardSize)
                bigShipColumn = random.choice(usableLetters)
                startCoord = (bigShipRow, bigShipColumn)
                if startCoord not in allUserCoords:
                    biggerShip.append(startCoord)
                shipDirection = random.choice(vOrH)
            
                if shipDirection == "horizontal":
                    columnNumber = ord(bigShipColumn) - ord('a')
                    if columnNumber == 0:
                        directionH = "right"
                    elif columnNumber == boardSize - 1:
                        directionH = "left"
                    else:
                        directionH = random.choice(lOrR)
                    for length in range(1):
                        if directionH == "right":
                            extension = columnNumber + 1
                        if directionH == "left":
                            extension = columnNumber - 1
                        additionalColumn = chr(extension + ord('a'))
                        additionalCoord = (bigShipRow, additionalColumn)
                        if additionalCoord not in allUserCoords:
                            biggerShip.append(additionalCoord)
                            allUserCoords.append(additionalCoord)
                            allUserCoords.append(startCoord)
                            if shipSize[1] == 2:
                                userShips["destroyer"] = biggerShip

                if shipDirection == "vertical":
                    if bigShipRow == 1:
                        directionV = "down"
                    elif bigShipRow == boardSize - 1:
                        directionV = "up"
                    else:
                        directionV = random.choice(uOrD)
                    for length in range(1):
                        if directionV == "down":
                            extension = bigShipRow + 1
                        if directionV == "up":
                            extension = bigShipRow - 1
                        additionalCoord = (extension, bigShipColumn)
                        if additionalCoord not in allUserCoords:
                            biggerShip.append(additionalCoord)
                            allUserCoords.append(additionalCoord)
                            allUserCoords.append(startCoord)
                            if shipSize[1] == 2:
                                playerShips["destroyer"] = biggerShip
                
                if len(biggerShip) == 2:
                    break
def checkHit(otherPlayerShips, otherPlayerBoard, otherPlayerShipsSunk, otherPlayer, currentPlayerDestroyerHits, currentPlayerDinghyHits, currentPlayer):
        columnNumber = ord(columnletter) - ord('a')
        if (rowGuess, columnletter) == otherPlayerShips["dinghy"]:
            print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
            currentPlayerDinghyHits.append((rowGuess,columnletter))

            if len(currentPlayerDinghyHits) == 1:
                print(f"{currentPlayer} sunk {otherPlayer}'s dinghy")
                otherPlayerBoard[rowGuess][columnNumber] += 2
                otherPlayerShipsSunk += 1

        elif (rowGuess,columnletter) in otherPlayerShips["destroyer"]:
            print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
            otherPlayerBoard[rowGuess][columnNumber] += 1
            currentPlayerDestroyerHits.append((rowGuess, columnletter))

            if len(currentPlayerDestroyerHits) == 2:
                print(f"{currentPlayer} sunk {otherPlayer}'s destroyer")
                otherPlayerShipsSunk += 1
                for row, column in currentPlayerDestroyerHits:
                    sunkColumn = ord(column) - ord('a')
                    otherPlayerBoard[row][sunkColumn] += 1

        else:
            print(f"{currentPlayer} missed!")

if __name__ == "__main__":
    print("--Welcome to Battleship--")
    while True:
        try:
            boardSize = int(input("What do you want the sidelength of board to be(min of 4, max of 10): "))
            if 4<= boardSize <= 10:
                break
            else:
                print("Please enter a valid side length(as a single number)")
        except:
            print("Please enter a number")

    usableLetters = []
    for f in range(boardSize):
        usableLetters.append(chr(f + ord('a')))
    rows = []
    rowCounter=1
    for a in range(boardSize):
        rows.append(rowCounter)
        rowCounter+=1

    playerBoard = {}
    createBoard(boardSize, playerBoard)
    
    shipPlacement(shipNumber, shipSize, playerShips, allPlayerCoords)
    print(f"player ships {playerShips}")

    shipPlacement(shipNumber, shipSize, computerShips, allComputerCoords)
    print(f"computer ships {computerShips}")

    computerBoard = {}
    createBoard(boardSize, computerBoard)
    
    playerGuesses = []
    computerGuesses = []
    playerDinghyHits =[]
    playerDestroyerHits = []
    computerDinghyHits =[]
    computerDestroyerHits =[]
    attempts = 1
    playerShipsSunk = 0
    computerShipsSunk = 0

    while True:
        print(f"\nPlayer Attempt #{attempts}")
        while True:
            while True:
                try:
                    rowGuess = int(input(f"Please enter a row(1-{boardSize}): "))
                    if 1<=rowGuess<=boardSize:
                        break
                except:
                    print(f"Enter a number 1-{boardSize}")
            while True:
                columnletter = input(f"Please enter a column{usableLetters}").strip() .lower()
                if columnletter in usableLetters:
                    break
                else:
                    print(f"Please enter one of the following:{usableLetters}")
                    
            columnNumber = ord(columnletter) - ord('a')
            if (rowGuess, columnletter) not in playerGuesses:
                playerGuesses.append((rowGuess, columnletter))
                computerBoard[rowGuess][columnNumber] += 1
                break
            else:
                print("Coordinate already guessed, try again")

        checkHit(computerShips, computerBoard, computerShipsSunk, "computer", playerDestroyerHits, playerDinghyHits, "user")
        
        print(f"Computer Attempt #{attempts}")
        while True:
            compRowGuess = random.randint(1, boardSize)
            compColumnletter = random.choice(usableLetters)
            computerShot = (compRowGuess, compColumnletter)
            
            if computerShot not in computerGuesses:
                print(f"The computer shot at ({compRowGuess},{compColumnletter})")
                computerGuesses.append(computerShot)
                columnNumber = ord(compColumnletter) - ord('a')
                playerBoard[compRowGuess][columnNumber] +=1

                checkHit(playerShips, playerBoard, playerShipsSunk, "user", computerDestroyerHits, computerDinghyHits, "computer")
                break
            
        if playerShipsSunk == shipNumber:
            print("The computer sank all of your ships")
            break

        if computerShipsSunk == shipNumber:
            print("You sunk all of the computer's ships!")
            break
        
        updatedCompCounter = 1
        updatedPlayerCounter = 1
        print("\nUpdated Computer Board:")
        for row in range(boardSize):
            print(computerBoard[updatedCompCounter])
            updatedCompCounter +=1
        
        print("\nUpdated player Board:")
        for row in range(boardSize):
            print(playerBoard[updatedPlayerCounter])
            updatedPlayerCounter += 1

        attempts += 1
            
        if playerShipsSunk == (2):
            print("The computer sunk all of your ships")
            print("You lose Battleship")
            break
        if computerShipsSunk == (2):
            print("You sunk all of the computer's ships.")
            print("You won Battleship")
            break
        
    finalPlayerCounter = 1
    finalCompCounter = 1
    print("\nFinal Player Board:")
    for row in range(boardSize):
        print(playerBoard[finalPlayerCounter])
        finalPlayerCounter += 1

    print("\nFinal Computer Board:")
    for row in range(boardSize):
        print(computerBoard[finalCompCounter])
        finalCompCounter += 1