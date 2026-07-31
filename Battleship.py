#Names: Gavin and Jeremaine

import random
playerShips = {}
shipNumber = 5
computerShips = {}

playerShips["Carrier"] = []
playerShips["Battleship"] = []
playerShips["Cruiser"] = []
playerShips["Submarine"] = []
playerShips["Destroyer"] = []

computerShips["Carrier"] = []
computerShips["Battleship"] = []
computerShips["Cruiser"] = []
computerShips["Submarine"] = []
computerShips["Destroyer"] = []


def createBoard(size, userBoard):
    userBoard.clear()
    boardCounter = 1
    for c in range(size):
        columns = []
        for f in range(size):
            columns.append(0)
        userBoard[boardCounter] = columns
        boardCounter +=1

def shipPlacement(userShips, boardSize, maxLetter):
    while (len(userShips["Carrier"]) < 5 or len(userShips["Battleship"]) < 4 or len(userShips["Cruiser"]) < 3 or len(userShips["Submarine"]) < 3 or len(userShips["Destroyer"]) < 2):
        if len(userShips["Destroyer"]) < 2:
            currentShip = "Destroyer"
            Length = 2
        elif len(userShips["Submarine"]) < 3:
            currentShip = "Submarine"
            Length = 3
        elif len(userShips["Cruiser"]) < 3:
            currentShip = "Cruiser"
            Length = 3
        elif len(userShips["Battleship"]) < 4:
            currentShip = "Battleship"
            Length = 4
        else:
            currentShip = "Carrier"
            Length = 5

        if len(userShips[currentShip]) == 0:
            shipRow = random.randint(1,boardSize)
            shipColumn = chr(random.randint(ord('a'), ord(maxLetter)))
            startCoord = (shipRow, shipColumn)

            if startCoord in userShips["Carrier"] or startCoord in userShips["Battleship"] or startCoord in userShips["Cruiser"] or startCoord in userShips["Submarine"] or startCoord in userShips["Destroyer"]:
                overlap = True
            else:
                overlap = False

            if overlap == False:
                userShips[currentShip].append(startCoord)
            shipDirection = random.randint(1, 2)

        else:
            shipRow, shipColumn = userShips[currentShip][-1]
            columnNumber = ord(shipColumn) - ord('a')

            if shipDirection == 1:
                extension = columnNumber + 1
                if extension < boardSize:
                    additionalCoord = (shipRow, chr(extension + ord('a')))
            else:
                extension = shipRow + 1
                if extension <= boardSize:
                    additionalCoord = (extension, shipColumn)

            if additionalCoord in userShips["Carrier"] or additionalCoord in userShips["Battleship"] or additionalCoord in userShips["Cruiser"] or additionalCoord in userShips["Submarine"] or additionalCoord in userShips["Destroyer"]:
                overlap = True
            else:
                overlap = False

            if overlap == True:
                userShips[currentShip].clear()
            else:
                userShips[currentShip].append(additionalCoord)

def checkHit(otherPlayerShips, otherPlayerBoard, otherPlayerShipsSunk, otherPlayer, currentPlayer, currentPlayerGuess, rowGuess, columnletter, currentPlayerCarrierHits, currentPlayerSubmarineHits, currentPlayerCruiserHits, currentPlayerBattleshipHits, currentPlayerDestroyerHits):
    columnNumber = ord(columnletter) - ord('a')

    if currentPlayerGuess in otherPlayerShips["Carrier"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships!")
        currentPlayerCarrierHits += 1 
        if currentPlayerCarrierHits == 5:
            print(f"{currentPlayer} sunk {otherPlayer}'s Carrier!")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["Carrier"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    elif currentPlayerGuess in otherPlayerShips["Battleship"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships")
        currentPlayerBattleshipHits += 1
        if currentPlayerBattleshipHits == 4:
            print(f"{currentPlayer} sunk {otherPlayer}'s Battleship!")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["Battleship"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    elif currentPlayerGuess in otherPlayerShips ["Cruiser"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships!")
        currentPlayerCruiserHits += 1
        if currentPlayerCruiserHits == 3:
            print(f"{currentPlayer} sunk {otherPlayer}'s Cruiser! ")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["Cruiser"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3


    elif currentPlayerGuess in otherPlayerShips["Submarine"]:
        print(f"{currentPlayer} hit one of the {otherPlayer}'s ships")
        currentPlayerSubmarineHits += 1
        if currentPlayerSubmarineHits == 3:
            print(f"{currentPlayer} sunk {otherPlayer}'s Submarine")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["Submarine"]:
                columnNumber = ord(column) - ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    elif currentPlayerGuess in otherPlayerShips["Destroyer"]:
        print(f"{currentPlayer} hit one of {otherPlayer}s ships!")
        otherPlayerBoard[rowGuess][columnNumber] == 2
        currentPlayerDestroyerHits += 1
        if currentPlayerDestroyerHits == 2:
            print(f"{currentPlayer} sunk {otherPlayer}'s destroyer")
            otherPlayerShipsSunk += 1
            for row, column in otherPlayerShips["Destroyer"]:
                columnNumber = ord(column)-ord('a')
                otherPlayerBoard[row][columnNumber] = 3

    else:
        print(f"{currentPlayer} missed!")

    return otherPlayerShipsSunk, currentPlayerCarrierHits, currentPlayerSubmarineHits, currentPlayerCruiserHits, currentPlayerBattleshipHits, currentPlayerDestroyerHits

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

def boardPrint(board):
    boardCounter = 1
    for row in board:
        print(board[boardCounter])
        boardCounter +=1

if __name__ == "__main__":
    print("--Welcome to Battleship--")

    boardSize = 10
           
    maxLetter = chr((boardSize-1) + ord('a'))

    playerBoard = {}
    createBoard(boardSize, playerBoard)
    shipPlacement(playerShips, boardSize, maxLetter)
    for ship in playerShips.values():
        for row, column in ship:
            columnNumber = ord(column) - ord('a')
            playerBoard[row][columnNumber] += 5
    print(f"player ships {playerShips}")

    computerBoard = {}
    createBoard(boardSize, computerBoard)
    shipPlacement(computerShips, boardSize, maxLetter)
    print(f"computer ships {computerShips}")

    print("\nStarting Computer Board")
    boardPrint(computerBoard)
    print("\nStarting Player Board")
    boardPrint(playerBoard)

    playerDestroyerHits = 0
    computerDestroyerHits = 0
    playerSubmarineHits = 0
    computerSubmarineHits = 0
    playerCruiserHits = 0
    computerCruiserHits = 0
    playerBattleshipHits = 0
    computerBattleshipHits = 0
    playerCarrierHits = 0
    computerCarrierHits = 0
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
        computerShipsSunk, playerCarrierHits, playerSubmarineHits, playerCruiserHits, playerBattleshipHits, playerDestroyerHits  = checkHit(computerShips, computerBoard, computerShipsSunk, "computer", "user", playerGuess, rowGuess, columnletter, playerCarrierHits, playerSubmarineHits, playerCruiserHits, playerBattleshipHits, playerDestroyerHits)
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

        playerShipsSunk, computerCarrierHits, computerSubmarineHits, computerCruiserHits, computerBattleshipHits, computerDestroyerHits = checkHit(playerShips, playerBoard, playerShipsSunk, "user", "computer", computerShot, compRowGuess, compColumnletter, computerCarrierHits, computerSubmarineHits, computerCruiserHits, computerBattleshipHits, computerDestroyerHits)
        
        if winChecker(playerShipsSunk, shipNumber) == True:
            print("The computer sank all of your ships")
            print("You lose")
            break

        print("\nUpdated Computer Board:")
        boardPrint(computerBoard)

        print("\nUpdated player Board:")
        boardPrint(playerBoard)

        attempts += 1
        
    print("\nFinal Computer Board:")
    boardPrint(computerBoard)

    print("\nFinal Player Board:")
    boardPrint(playerBoard)