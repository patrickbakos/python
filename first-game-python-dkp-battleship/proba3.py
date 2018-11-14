import copy

ships5 = (0, 0, 2)
ships6 = (0, 0, 2, 1)
ships7 = (0, 0, 2, 2)
ships8 = (0, 0, 3, 2)
ships9 = (0, 0, 2, 2, 0, 1)

row = 5
column = row

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
grid1 = [0] * row
for i in range(row):
    grid1[i] = [0] * column
grid2 = copy.deepcopy(grid1)

def out_of_grid(grid, row, column, direction, length):  # ne lehessen palyan kivulre rakni
    if direction == 1:
        if row < 0 or row > len(grid) or row + length > len(grid) or column < 0 or column > len(grid):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    elif direction == 0:
        if row < 0 or row > len(grid) or column < 0 or column > len(grid) or column + length > len(grid):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    else:
        all_good = 0
        print("Direction error! 1 is vertical, 0 is horizontal.")
    return all_good

print(out_of_grid(grid1, 1, 5, 1, 1))