#Names: Gavin and Jeremaine

import random
playerShips = {}
allPlayerCoords = []
shipNumber = 5
shipSize = []
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

def shipPlacement( userShips, allUserCoord, maxLetter, ShipNumber):
    while True:
            
            while True:
                biggerShip = []
                destroyerShipRow = random.randint(1, boardSize)
                destroyerShipColumn = chr(random.randint(ord('a'), ord(maxLetter)))
                startCoord = (destroyerShipRow, destroyerShipColumn)
                if startCoord not in allUserCoords:
                    shipDirection = random.randint(1,2)
                    if shipDirection == 1:
                        columnNumber = ord(destroyerShipColumn) - ord('a')
                        if columnNumber == 0:
                            directionH = 1
                        elif columnNumber == boardSize - 1:
                            directionH = 2
                        else:
                            directionH = random.randint(1,2)
                        for length in range(1):
                            if directionH == 1:
                                extension = columnNumber + 1
                            if directionH == 2:
                                extension = columnNumber - 1
                            additionalColumn = chr(extension + ord('a'))
                            additionalCoord = (destroyerShipRow, additionalColumn)
                            if additionalCoord not in allUserCoords:
                                biggerShip.append(additionalCoord)
                                biggerShip.append(startCoord)
                                allUserCoords.append(additionalCoord)
                                allUserCoords.append(startCoord)
                                if shipSize[1] == 2:
                                    userShips["destroyer"] = biggerShip

                    if shipDirection == 2:
                        if destroyerShipRow == 1:
                            directionV = 1
                        elif destroyerShipRow == boardSize:
                            directionV = 2
                        else:
                            directionV = random.randint(1,2)
                        for length in range(1):
                            if directionV == 1:
                                extension = destroyerShipRow + 1
                            if directionV == 2:
                                extension = destroyerShipRow - 1
                            additionalCoord = (extension, destroyerShipColumn)
                            if additionalCoord not in allUserCoords:
                                biggerShip.append(additionalCoord)
                                biggerShip.append(startCoord)
                                allUserCoords.append(additionalCoord)
                                allUserCoords.append(startCoord)
                                if shipSize[1] == 2:
                                    userShips["destroyer"] = biggerShip

                    if len(biggerShip) == 2:
                        break

def checkHit(otherPlayerShips, otherPlayerBoard, otherPlayerShipsSunk, otherPlayer, currentPlayer, currentPlayerGuess, rowGuess, columnletter, currentPlayerCarrierHits, currentPlayerSubmarineHits, currentPlayerCrusierHits, currentPlayerBattleshipHits):
    columnNumber = ord(columnletter) - ord('a')


    if currentPlayerGuess in otherPlayerShips["carrier"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships!")
        currentPlayerCarrierHits += 1 
        if currentPlayerCarrierHits == 5:
            print(f"{currentPlayer} sunk one of the {otherPlayer}'s Carriers!")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["battleship"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    elif currentPlayerGuess in otherPlayerShips["battleship"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships")
        currentPlayerBattleshipHits += 1
        if currentPlayerBattleshipHits == 4:
            print(f"{currentPlayer} sunk one of the {otherPlayer}'s Battleships!")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["battleship"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    elif currentPlayerGuess in otherPlayerShips ["cruiser"] and ["submarine"]:

        if currentPlayerGuess in otherPlayerShips ["cruiser"]:
            print(f"{currentPlayer} hit one of the {otherPlayer}'s ships!")
            currentPlayerCrusierHits += 1
        if currentPlayerCrusierHits == 3:
            print(f"{currentPlayer} sunk one of the {otherPlayer}'s Cruisers! ")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["cruiser"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3


        elif currentPlayerGuess in otherPlayerShips["submarine"]:
            print(f"{currentPlayer} hit one of the {otherPlayer}'s ships")
            otherPlayerBoard[rowGuess][compColumnNumber] == 3
            currentPlayerSubmarineHits += 1
            if currentPlayerSubmarineHits == 3:
                print(f"{currentPlayer} sunk one of the {otherPlayer}'s Submarines")
                otherPlayerShipsSunk += 1
                for row, column in otherPlayerShips["submarine"]:
                    columnNumber = ord(column) - ord('a')
                    otherPlayerBoard[row][columnNumber] == 3

    elif currentPlayerGuess in otherPlayerShips["destroyer"]:
        print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
        otherPlayerBoard[rowGuess][columnNumber] == 2
        currentPlayerDestroyerHits += 1

        if currentPlayerDestroyerHits == 2:
            print(f"{currentPlayer} sunk {otherPlayer}'s destroyer")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["destroyer"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    else:
        print(f"{currentPlayer} missed!")

    return otherPlayerShipsSunk, currentPlayerDestroyerHits

def validateInput(row, column, boardSize, currentPlayerBoard):
    columnNumber = ord(column) - ord('a')

    if row < 0 or row > boardSize:
        return False
    elif columnNumber < 0 or columnNumber >= boardSize:
        return False
    cell = currentPlayerBoard[row][columnNumber]
    if cell != 0 and cell != 5:
        return False
    return True

def winChecker(shipsSunk, shipNumber):
    if shipsSunk == shipNumber:
        return True
    return False


if __name__ == "__main__":
    print("--Welcome to Battleship--")

    boardSize = 10
           
    maxLetter = chr((boardSize-1) + ord('a'))
    rows = []
    rowCounter=1
    for a in range(boardSize):
        rows.append(rowCounter)
        rowCounter+=1

    playerBoard = {}
    createBoard(boardSize, playerBoard)
    shipPlacement(shipNumber, playerShips, allPlayerCoords, boardSize, maxLetter)
    for row, column in allPlayerCoords:
        columnNumber = ord(column) - ord('a')
        playerBoard[row][columnNumber] += 5
    print(f"player ships {playerShips}")

    computerBoard = {}
    createBoard(boardSize, computerBoard)
    shipPlacement(shipNumber, shipSize, computerShips, allComputerCoords, boardSize, maxLetter)
    print(f"computer ships {computerShips}")

    playerDestroyerHits = 0
    computerDestroyerHits = 0
    attempts = 1
    playerShipsSunk = 0
    computerShipsSunk = 0

    while True:
        print(f"\nPlayer Attempt #{attempts}")
    
        while True:
            try:
                rowGuess = int(input(f"Please enter a row(1-{boardSize}): "))
                columnletter = (input(f"please enter a column (a - {maxLetter}): ")).strip().lower()
                if validateInput(rowGuess,columnletter,boardSize, computerBoard):
                    columnNumber = ord(columnletter)- ord('a')
                    computerBoard[rowGuess][columnNumber] += 1
                    break
                else:
                    print("Invalid coordinate or already guessed, try again")
            except:
                print("Please enter a valid coordinate")

        playerGuess = (rowGuess, columnletter)
        computerShipsSunk, playerDestroyerHits = checkHit(computerShips, computerBoard, computerShipsSunk, "computer", playerDestroyerHits, "user", playerGuess, rowGuess, columnletter)
        if winChecker(computerShipsSunk, shipNumber) == True:
            print("You sank all of the computers ships") 
            print("You Win!")       
            break

        print(f"Computer Attempt #{attempts}")
        while True:
            compRowGuess = random.randint(1, boardSize)
            compColumnletter = chr(random.randint(ord('a'), ord(maxLetter)))
            computerShot = (compRowGuess, compColumnletter)
            if validateInput(compRowGuess,compColumnletter,boardSize, playerBoard):
                compColumnNumber = ord(compColumnletter)- ord('a')
                playerBoard[compRowGuess][compColumnNumber] += 1
                print(f"The computer guessed {computerShot}")
                break
            else:
                continue

        playerShipsSunk, computerDestroyerHits = checkHit(playerShips, playerBoard, playerShipsSunk, "user", computerDestroyerHits, "computer", computerShot, compRowGuess, compColumnletter)
        
        if winChecker(playerShipsSunk, shipNumber) == True:
            print("The computer sank all of your ships")
            print("You lose")
            break

        updatedCompCounter = 1
        print("\nUpdated Computer Board:")
        for row in range(boardSize):
            print(computerBoard[updatedCompCounter])
            updatedCompCounter +=1

        updatedPlayerCounter = 1
        print("\nUpdated player Board:")
        for row in range(boardSize):
            print(playerBoard[updatedPlayerCounter])
            updatedPlayerCounter += 1

        attempts += 1
        
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