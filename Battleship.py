import random
def battleship_coordinates(grid):
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]
    row4 = grid[3]

if __name__ == "__main__":
    print("-- Welcome To BattleShip --")
    rows = [1,2,3,4]
    columns = ["A","B","C","D"]
    grid = [["0" for _ in range(len(columns))] for _ in range(len(rows))]
    print("  " + " ".join(columns))
    for i, row_data in enumerate(grid):
        print(f"{rows[i]} " + " ".join(row_data))
    columns = ["a", "b", "c", "d"]
    shipRow = random.randint(1, 4)
    shipColumn = random.choice(columns)


    while True:
        try:
            rowGuess = int(input("\nPlease enter a row(1-4): "))
            break
        except:
            print("Enter a number 1-4")
    while True:
        columnGuess = input("\nPlease enter a column(a, b, c, d)").strip() .lower()
        if columnGuess == "a" or columnGuess == "b" or columnGuess == "c" or columnGuess == "d":
            break
        else:
            print("Please enter one of the following: a, b, c, d")
    
    print(f"{columnGuess}, {rowGuess}")
    print(f"{shipColumn}, {shipRow}")
    

        