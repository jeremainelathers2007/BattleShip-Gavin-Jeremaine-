import random

if __name__ == "__main__":
    letterToNumber = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9}
    numberToLetter = {0:"a", 1:"b",2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j"}
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
    for e in range(boardSize):
        usableLetters.append(numberToLetter[e])
    ShipNumber = 2
    ShipLength = ()
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
                    columnNumber = letterToNumber[bigShipColumn]
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
                        additionalColumn = numberToLetter[extension]
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
                    columnNumber = letterToNumber[bigShipColumn]
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
                        additionalColumn = numberToLetter[extension]
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
        
    
    playerGuesses = []
    computerGuesses = []
    allcomputerShots = []
    allplayerShots = []
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
                    columnGuess = letterToNumber[columnletter]
                    break
                else:
                    print(f"Please enter one of the following:{usableLetters}")
            if (rowGuess, columnGuess) not in playerGuesses:
                playerGuesses.append((rowGuess, columnGuess))
                computerBoard[rowGuess][columnGuess] += 1
                break
            else:
                print("Coordinate already guessed, try again")

        if (rowGuess, columnGuess) == computerShipCoord:
            computerBoard[rowGuess][columnGuess] += 1
            print("Congrats you sunk a ship!")
            playerShipsSunk += 1
        else:
            print("You missed!")
        
        letterToNumber = 0
        print(f"Computer Attempt #{attempts}")
        while True:
            compRowGuess = random.randint(1, boardSize)
            compColumnletter = random.choice(usableLetters)
            computerShot = (compRowGuess, compColumnletter)
            
            if computerShot not in computerGuesses:
                print(f"The computer hit ({compRowGuess},{compColumnletter})")
                computerGuesses.append(computerShot)
                columnConverter = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9}
                letterToNumber = columnConverter[compColumnletter]
                playerBoard[compRowGuess][letterToNumber] +=1
                break
            
        # if computerShot == playerShipCoord:
        #     print("The computer sunk your ship")
        #     computerShipsSunk += 1
        # if computerShot != playerShipCoord:
        #     print("The computer missed")
        for allcomputerShots in range(shipSize):
            if computerGuesses == "dinghy":
                print("The computer sank one of dinghy ships!")
            if computerGuesses == "Destroyer":
                print("The computer sunk a destroyer!")
            if allcomputerShots == allShips:
                print("The computer sank all of your ships")

        
        for allplayerShots in range(shipSize):
            if playerGuesses == "dingehy":
                print("You sunk one of the computer's dinghy's")
            if playerGuesses == "Destroyer":
                print("You sank one of the computer's Destroyer's")
            if allplayerShots == allShips:
                print("You sunk all of the computer's ships!")
        
        
        updatedCompCounter = 1
        updatedPlayerCounter = 1
        print("\nUpdated Computer Board:")
        for row in range(boardSize):
            print(computerBoard[updatedCompCounter])
            updatedCompCounter +=1
        ghghhg
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
        # if attempts == 5:
        #     print("You failed to sink all the ships.")
        
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