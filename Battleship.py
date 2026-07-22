#Names: Gavin and Jeremaine

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
    
    usableLetters = []
    for f in range(boardSize):
        usableLetters.append(chr(f + ord('a')))
    
    playerBoard = {}
    boardCounter = 1
    for c in range(boardSize):
        columns = []
        for f in range(boardSize):
            columns.append(0)
        playerBoard[boardCounter] = columns
        boardCounter +=1
    
    playerShips = {}
    allPlayerCoords = []
    shipNumber = 2
    shipSize = [1,2]
    computerShips = {}
    allComputerCoords = []

    vOrH = ["horizontal", "vertical"]
    uOrD = ["up", "down"]
    lOrR = ["left", "right"]

    for ship in range(shipNumber):
        if shipSize[ship] == 1:
            while True:
                playerShipRow = random.randint(1, boardSize)
                playerShipColumn = random.choice(usableLetters)
                single = (playerShipRow, playerShipColumn)
                if single not in allPlayerCoords:
                    playerShips["dinghy"] = single
                    allPlayerCoords.append(single)
                    break

        if shipSize[ship] > 1:
            while True:
                biggerShip = []
                bigShipRow = random.randint(1, boardSize)
                bigShipColumn = random.choice(usableLetters)
                startCoord = (bigShipRow, bigShipColumn)
                if startCoord not in allPlayerCoords:
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
                        if additionalCoord not in allPlayerCoords:
                            biggerShip.append(additionalCoord)
                            allPlayerCoords.append(additionalCoord)
                            allPlayerCoords.append(startCoord)
                            if shipSize[1] == 2:
                                playerShips["destroyer"] = biggerShip

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
                        if additionalCoord not in allPlayerCoords:
                            biggerShip.append(additionalCoord)
                            allPlayerCoords.append(additionalCoord)
                            allPlayerCoords.append(startCoord)
                            if shipSize[1] == 2:
                                playerShips["destroyer"] = biggerShip
                
                if len(biggerShip) == 2:
                    break

    print(f"player ships {playerShips}")

    for ship in range(shipNumber):
        if shipSize[ship] == 1:
            while True:
                computerShipRow = random.randint(1, boardSize)
                computerShipColumn = random.choice(usableLetters)
                single = (computerShipRow, computerShipColumn)
                if single not in allComputerCoords:
                    computerShips["dinghy"] = single
                    allComputerCoords.append(single)
                    break

        if shipSize[ship] > 1:
            while True:
                biggerShip = []
                bigShipRow = random.randint(1, boardSize)
                bigShipColumn = random.choice(usableLetters)
                startCoord = (bigShipRow, bigShipColumn)
                if startCoord not in allComputerCoords:
                    biggerShip.append(startCoord)
                shipDirection = random.choice(vOrH)
            
                if shipDirection == "horizontal":
                    columnNumber = ord(bigShipColumn) - ord('a')
                    if columnNumber == 0:
                        directionH = "right"
                    elif columnNumber == boardSize:
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
                        if additionalCoord not in allComputerCoords:
                            biggerShip.append(additionalCoord)
                            allComputerCoords.append(startCoord)
                            allComputerCoords.append(additionalCoord)
                            if shipSize[1] == 2:
                                computerShips["destroyer"] = biggerShip
                    if len(biggerShip) == 2:
                        break
                
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
                        if additionalCoord not in allComputerCoords:
                            biggerShip.append(additionalCoord)
                            allComputerCoords.append(startCoord)
                            allComputerCoords.append(additionalCoord)
                            if shipSize[1] == 2:
                                computerShips["destroyer"] = biggerShip
                    if len(biggerShip) == 2:
                        break

    print(f"computer ships {computerShips}")

    computerBoard = {}
    boardCounter = 1
    for c in range(boardSize):
        columns = []
        for f in range(boardSize):
            columns.append(0)
        computerBoard[boardCounter] = columns
        boardCounter +=1

    for g in range(len(allPlayerCoords)):
        row = allPlayerCoords[g][0]
        columnLetter = allPlayerCoords[g][1]
        columnnumber = ord(columnLetter) - ord('a')
        playerBoard[row][columnnumber] = 5
    
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
                    columnNumber = ord(columnletter) - ord('a')
                    break
                else:
                    print(f"Please enter one of the following:{usableLetters}")
            if (rowGuess, columnNumber) not in playerGuesses:
                playerGuesses.append((rowGuess, columnNumber))
                computerBoard[rowGuess][columnNumber] += 1
                break
            else:
                print("Coordinate already guessed, try again")

        if (rowGuess, columnNumber) == computerShipsSunk:
            computerBoard[rowGuess][columnNumber] += 1
            print("Congrats you sunk a ship!")
            playerShipsSunk += 1
        else:
            print("You missed!")
        
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
                break
            
        # if computerShot == playerShipCoord:
        #     print("The computer sunk your ship")
        #     computerShipsSunk += 1
        # if computerShot != playerShipCoord:
        #     print("The computer missed")
        
            if computerDinghyHits == 1:
                print("The computer sank one of dinghy ships!")
                computerDinghyHits.append((rowGuess,columnletter))
            if computerDestroyerHits ==2:
                print("The computer sunk a destroyer!")
                computerDestroyerHits.append((rowGuess,columnletter))
            if playerShipsSunk == ShipNumber:
                print("The computer sank all of your ships")

        
        
            if playerDinghyHits == 1:
                print("You sunk one of the computer's dinghy's")
                playerDinghyHits.append(rowGuess,columnletter)
            if playerDestroyerHits == 2:
                print("You sank one of the computer's Destroyer's")
                playerDestroyerHits.append(rowGuess,columnletter)
            if computerShipsSunk == ShipNumber:
                print("You sunk all of the computer's ships!")
        
        
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
            print("You sunk all the ships!")
            break
        if computerShipsSunk == (2):
            print("The computer Sunk all the ships.")
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