import copy
import os
import pregame
import game
import generator
os.system('cls')


def main():
    grid1, grid2, ships, turn, life1, life2 = generator.pre_data()
    grid1, life1 = pregame.ship_generation("First player", ships, grid1, life1)
    grid2, life2 = pregame.ship_generation("Second player", ships, grid2, life2)
    while life1 > 0 and life2 > 0 and turn > 0:
        game.print_all(life1, life2, grid1, grid2, turn)
        life2 = game.shooting("First player", grid1, life2)
        game.print_all(life1, life2, grid1, grid2, turn)
        life1 = game.shooting("Second player", grid2, life1)
        turn -= 1
    game.print_all(life1, life2, grid1, grid2, turn)

    if life2 == 0:  # win conditions
        print("\nFirst player wins!")
    elif life1 == 0:
        print("\nSecond player wins!")
    elif turn == 0:
        print("\nGame fucking over, mate!")


if __name__ == "__main__":
    main()
