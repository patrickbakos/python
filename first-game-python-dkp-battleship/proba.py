import copy
row = 5
grid1 = ["0"] * row
for i in range(row):
    grid1[i] = ["0"] * row
grid2 = copy.deepcopy(grid1)
grid = grid1
length = 1
print(grid1)
print(grid2)

direction = 1
row  = 6
column = row
print(len(grid))

if direction == 1:
    if row < 0 or row > len(grid) or row + length > len(grid) or column < 0 or column > len(grid):
        all_good = 0
        print("Please enter valid parameters1!\n")
    else:
        all_good = 1
elif direction == 0:
    if row < 0 or row > len(grid) or column < 0 or column > len(grid) or column + length > len(grid):
        all_good = 0
        print("Please enter valid parameters0!\n")
    else:
        all_good = 1
else:
    all_good = 0
    print("Direction error! 1 is vertical, 0 is horizontal.")