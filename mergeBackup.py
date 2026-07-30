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
                lastCoord = startCoord

        else:
            shipRow, shipColumn = lastCoord
            columnNumber = ord(shipColumn) - ord('a')

            shipDirection = random.randint(1, 2)
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
                lastCoord = additionalCoord