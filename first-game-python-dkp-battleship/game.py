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

def shooting(grid, row, column):  # lövés
    hit = 0
    if grid[row][column] == "0":
        grid[row][column] = "#"
    elif grid[row][column] == "X":
        grid[row][column] = "H"
        hit = 1
    return hit