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

def shipPlacement(shipCount, shipSize, userShips, allUserCoords, boardSize):
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
                                biggerShip.append(startCoord)
                                allUserCoords.append(additionalCoord)
                                allUserCoords.append(startCoord)
                                if shipSize[1] == 2:
                                    userShips["destroyer"] = biggerShip

                    if shipDirection == "vertical":
                        if bigShipRow == 1:
                            directionV = "down"
                        elif bigShipRow == boardSize:
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
                                biggerShip.append(startCoord)
                                allUserCoords.append(additionalCoord)
                                allUserCoords.append(startCoord)
                                if shipSize[1] == 2:
                                    userShips["destroyer"] = biggerShip
                    
                    if len(biggerShip) == 2:
                        break

def checkHit(otherPlayerShips, otherPlayerBoard, otherPlayerShipsSunk, otherPlayer, currentPlayerDestroyerHits, currentPlayer, currentPlayerGuess, rowGuess, columnletter):
    columnNumber = ord(columnletter) - ord('a')

    if currentPlayerGuess == otherPlayerShips["dinghy"]:
        print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
        print(f"{currentPlayer} sunk {otherPlayer}'s dinghy")
        otherPlayerBoard[rowGuess][columnNumber] += 2
        otherPlayerShipsSunk += 1

    elif currentPlayerGuess in otherPlayerShips["destroyer"]:
        print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
        otherPlayerBoard[rowGuess][columnNumber] += 1
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

def validateInput(row, column, boardSize, guesses):
    columnNumber = ord(column) - ord('a')
    if row < 1 or row > boardSize:
        return False
    elif columnNumber < 0 or columnNumber >= boardSize:
        return False
    elif (row, column) in guesses:
        return False
    return True

def winChecker(shipsSunk, shipNumber):
    if shipsSunk == shipNumber:
        return True
    return False


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
    shipPlacement(shipNumber, shipSize, playerShips, allPlayerCoords, boardSize)
    for row, column in allPlayerCoords:
        columnNumber = ord(column) - ord('a')
        playerBoard[row][columnNumber] += 5
    print(f"player ships {playerShips}")

    computerBoard = {}
    createBoard(boardSize, computerBoard)
    shipPlacement(shipNumber, shipSize, computerShips, allComputerCoords, boardSize)
    print(f"computer ships {computerShips}")

    playerGuesses = []
    computerGuesses = []
    playerDestroyerHits = 0
    computerDestroyerHits = 0
    attempts = 1
    playerShipsSunk = 0
    computerShipsSunk = 0
    maxLetter = chr((boardSize-1) + ord('a'))

    while True:
        print(f"\nPlayer Attempt #{attempts}")
    
        while True:
            try:
                rowGuess = int(input(f"Please enter a row(1-{boardSize}): "))
                columnletter = (input(f"please enter a column (a - {maxLetter}): ")).strip().lower()
                if validateInput(rowGuess,columnletter,boardSize,playerGuesses):
                    columnNumber = ord(columnletter)- ord('a')
                    playerGuesses.append((rowGuess,columnletter))
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
            compColumnletter = random.choice(usableLetters)
            computerShot = (compRowGuess, compColumnletter)
            if validateInput(compRowGuess,compColumnletter,boardSize,computerGuesses):
                compColumnNumber = ord(compColumnletter)- ord('a')
                computerGuesses.append(computerShot)
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