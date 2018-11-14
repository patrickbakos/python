import os

def grid_preview(grid):  # mindent felfedo palya
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()

def ship_placement(grid, row, column, direction, length):  # hajók lerakása
    if direction == 1:
        for k in range(length):
            grid[row + k][column] = "X"
    elif direction == 0:
        for k in range(length):
            grid[row][column + k] = "X"
    grid_preview(grid)
    return length

def out_of_grid(grid, row, column, direction = 0, length = 0):  # ne lehessen palyan kivulre rakni
    if direction == 1:
        print("lenggrid:", len(grid))
        print("row:", row)
        print("column:", column)
        if row < 0 or row >= len(grid) or row + length > len(grid) or column < 0 or column >= len(grid):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    elif direction == 0:
        print("lenggrid:", len(grid))
        print("row:", row)
        print("column:", column)
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid) or column + length > len(grid):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    else:
        print("lenggrid:", len(grid))
        print("row:", row)
        print("column:", column)
        all_good = 0
        print("Direction error! 1 is vertical, 0 is horizontal.")
    return all_good

def placement_check(grid, row, column, direction, length):  # mas hajohoz viszonyitva jo-e
    all_good = 1
    def ship_check(column_correction1, column_correction2, all_good=1):
        for j in i[column - column_correction1:column + column_correction2]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
        return all_good

    # vizszintes
    if direction == 0:
        if row == 0:
            for i in grid[row:row + 2]:
                if column == 0 and all_good == 1:
                    all_good = ship_check(0, length + 1)
                elif all_good == 1:  # column > 0
                    all_good = ship_check(1, length + 1)
        else:  # row > 0
            for i in grid[row - 1:row + 2]:
                if column == 0 and all_good == 1:
                    all_good = ship_check(0, length + 1)
                elif all_good == 1:  # column > 0
                    all_good = ship_check(1, length + 1)
    # fuggoleges
    if direction == 1:
        if row == 0:
            for i in grid[row:row + length + 1]:
                if column == 0 and all_good == 1:
                    all_good = ship_check(0, 2)
                elif all_good == 1:  # column > 0
                    all_good = ship_check(1, 2)
        else:  # row > 0
            for i in grid[row - 1:row + length + 1]:
                if column == 0 and all_good == 1:
                    all_good = ship_check(0, 2)
                elif all_good == 1:  # column > 0
                    all_good = ship_check(1, 2)
    return all_good

def ship_generation(player, ships, grid, life):
    for i in range(len(ships)):
        for k in range(ships[i]):
            length = i
            all_good = 0
            while all_good == 0:         
                print(player, "player:")
                try:
                    row_ship = int(input("\nRow of ship? \n")) - 1
                    column_ship = int(input("\nColumn of ship? \n")) - 1
                    direction = int(input("\nDirection of ship? (1 is vertical, 0 is horizontal.)\n"))
                except ValueError:
                    print("Please enter a valid parameter!\n")
                    continue
                all_good = out_of_grid(grid, row_ship, column_ship, direction, length)
                if all_good == 0:
                    continue
                all_good = placement_check(grid, row_ship, column_ship, direction, length)
                if all_good == 0:
                    continue
                life += ship_placement(grid, row_ship, column_ship, direction, length)
    os.system('cls')
    return (grid, life)
