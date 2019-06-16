#!/usr/bin/env python3

# Change drawing here, not in the implementation!!!
player_one = " X "
player_two = " O "
empty_cell = "   "
sep = "|"
border = "+---+---+---+"
winning_conditions = [
    # Horizontal win conditions
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    # Vertical win condtions
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    # Diagonal win condtitions
    [0, 4, 8],
    [2, 4, 6]]


# Resets the game settings, making it possible to play more than one game
# in one call of the program
def reset_game():
    global playing
    playing = True
    global turns
    turns = 1
    global cells
    cells = [empty_cell for i in range(9)]


# Draws up the board using global variables
def draw_board():
    for i in range(9):
        if i % 3 == 0:
            if i != 0:
                print(sep)
            print(border)
        print(sep + cells[i], end="")
    print(sep)
    print(border)


# This function takes the input from the user, validates it and 
# notes the action onto the game board (if the input is correct)
def process_turn(player):
    # Try to get the input from the user and proceed
    # if everything is okay. Otherwise return false for 
    # turn failure
    try:
        chosen_cell = int(input("{} choose: ".format(player)))
    except ValueError:
        print("Please type in a natrual int")
        return False

    if chosen_cell < 1 or chosen_cell > 9:
        print("Please use a number within the range of 1 to 9 (including those)")
        return False
    if cells[chosen_cell - 1] != empty_cell:
        print("This cell has already been used, try another one")
        return False

    # If all the checks pass, we put the player's sign in the chosen cell
    cells[chosen_cell - 1] = player
    return True


# This function checks the board for any winners, and returns True if there is a winner
# and returns False if there are no winners. Conditions for winning are in the winning_conditions var
def check_winner():
    global playing

    for condition in winning_conditions:
        row_set = set([cells[cell_value] for cell_value in condition])
        if len(row_set) == 1 and empty_cell not in row_set:
            winner = player_one if turns % 2 == 1 else player_two
            print("Winner is" + winner)
            playing = False


# Main game loop
def play():
    global playing
    global turns

    while True:
        if playing:
            if turns >= 10:
                playing = False
                continue
            if turns % 2 == 1:
                if not process_turn(player_one):
                    continue
            else:
                if not process_turn(player_two):
                    continue
            draw_board()
            check_winner()
            turns += 1
        # Ask the user if they want to play again, otherwise... go to hell
        else:
            if input("Do you want to play again? (y/n)").lower() == "y":
                reset_game()
                playing = True
                turns = 1
                draw_board()
                continue
            break

if __name__ == "__main__":
    reset_game()
    draw_board()
    play()
