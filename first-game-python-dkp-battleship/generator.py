import copy

def pre_data():
    # ITT KEZDODIK##################################
    print('\nWelcome to DKP Battleship Game!\n')
    row = 0
    while 5 > row or row > 9:
        try:
            row = int(input('Size of the grid? (5-9) \n'))
            if 5 > row or row > 9:
                print("\nThe grid must be between 5 and 9!")
        except ValueError:
            print("Please enter a valid parameter!\n")

    life1 = 0  # erteket kell kapniuk, mert kesobb csak +=vel szerepel
    life2 = 0
    turn = 20

    # hajok kiosztasa. Indexek jelolik a hajok hosszat(length), ertekek pedig a darabszamot
    ships5 = (0, 0, 2)
    ships6 = (0, 0, 2, 1)
    ships7 = (0, 0, 2, 2)
    ships8 = (0, 0, 3, 2)
    ships9 = (0, 0, 2, 2, 0, 1)

    # ships praktikus hasznalhatosaga a jovoben
    if row == 5:
        ships = ships5
    elif row == 6:
        ships = ships6
    elif row == 7:
        ships = ships7
    elif row == 8:
        ships = ships7
    elif row == 9:
        ships = ships9

    # palyak generalasa
    grid1 = ["0"] * row
    for i in range(row):
        grid1[i] = ["0"] * row
    grid2 = copy.deepcopy(grid1)
    return (grid1, grid2, ships, turn, life1, life2)