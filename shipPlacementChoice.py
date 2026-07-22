    # while True:
    #     placementQ = input("Do you want to place your own ships or have them randomly placed? ")
    #     if placementQ == "place" or placementQ == "random":
    #         break
    #     else:
    #         print("Try saying 'place' to place your own ships or 'random' to have them placed for you. ")
    
    # shipLocations = []
    # if placementQ == "random":
    #     for d in range(boardSize//2):
    #         while True:
    #             shipRow = random.randint(1, boardSize)
    #             shipColumn = random.choice(usableLetters)
    #             shipCoord = (shipRow, shipColumn)
    #             if shipCoord not in shipLocations:
    #                 shipLocations.append(shipCoord)
    #                 break
    #     print(shipLocations)

    # if placementQ == "place":
    #     for d in range(boardSize//2):
    #         while True:
    #             while True:
    #                 shipRow = int(input(f"What row do you want the ship to be on (1-{boardSize}: )"))
    #                 if 1<=shipRow<=boardSize:
    #                     break
    #                 else:
    #                     print("Try a valid integer in the range")
    #             while True:
    #                 shipColumn = input(f"What column do you want to place your ship on {usableLetters}: ")
    #                 if shipColumn in usableLetters:
    #                     break
    #                 else:
    #                     print("Try a valid letter.")
    #             shipCoord = (shipRow, shipColumn)
    #             if shipCoord not in shipLocations:
    #                 shipLocations.append(shipCoord)
    #                 break
    #     print(shipLocations)