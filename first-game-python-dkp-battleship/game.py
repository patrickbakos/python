import os
import pregame


def fog_of_war(grid):  # játék közben lathato palya
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "H":
                print(grid[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def print_all(life1, life2, grid1, grid2, turn):  # játékkép printelése
    print("\nFirst players life:", life1)
    print("Second players life:", life2)
    print("Turns left:", turn)
    print("\nFirst player:")
    fog_of_war(grid1)
    print("\nSecond player:")
    fog_of_war(grid2)
    print()


def shooting_hits(grid, row, column):  # lövés
    hit = 0
    if grid[row][column] == "0":
        grid[row][column] = "#"
    elif grid[row][column] == "X":
        grid[row][column] = "H"
        hit = 1
    return hit


def shooting(player_name, grid, life):
    all_good = 0
    while all_good == 0:
        print("\n{} shoots:\n".format(player_name))
        try:
            row_ship = int(input("Row of target?\n")) - 1
            column_ship = int(input("Column of target?\n")) - 1
        except ValueError:
            print("\nPlease enter a valid parameter!\n")
            continue
        all_good = pregame.out_of_grid(grid, row_ship, column_ship)
        if all_good == 0:
            continue
        life = life - shooting_hits(grid, row_ship, column_ship)
        os.system('cls')
        return life
