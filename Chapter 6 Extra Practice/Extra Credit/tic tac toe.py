#! /usr/bin/env python3

NUMBER_OF_ROWS = 3
NUMBER_OF_COLUMNS = 3


def display_title():
    print("Welcome to Tic Tac Toe\n")


def make_move(board, player):

    while True:

        row = int(input("Pick a row (1, 2, 3): "))
        column = int(input("Pick a column (1, 2, 3): "))

        if (row < 1 or row > NUMBER_OF_ROWS) and \
                (column < 1 or column > NUMBER_OF_COLUMNS):
            print("Invalid row and column. Try again. ")
        elif row < 1 or row > NUMBER_OF_ROWS:
            print("Invalid row. Try again. ")
        elif column < 1 or column > NUMBER_OF_COLUMNS:
            print("Invalid column. Try again. ")
        elif board[row - 1][column - 1] != " ":
            print("Spot already taken. Try again. ")
        else:
            board[row - 1][column - 1] = player
            break


def display_board(board):

    for row in board:
        print("+---+---+---+")
        print("|", end=" ")
        for column in row:
            print(column, end=" | ")
        print()
    print("+---+---+---+")


def switch_player(player):
    if player == 'X':
        return 'O'
    return 'X'


def is_winner(board, player):
    # Check rows
    for row in board:
        if (row[0] == player) and (row[1] == player) and (row[2] == player):
            return True

    # Check columns
    for j in range(NUMBER_OF_COLUMNS):
        if (board[0][j] == player) and (board[1][j] == player) and \
                (board[2][j] == player):
            return True

    # Check diagonals

    # From left to right
    for j in range(1):
        if (board[0][j] == player) and (board[1][j + 1] == player) and \
                (board[2][j + 2] == player):
            return True

    # From right to left
    for j in range(1):
        if (board[0][j + 2] == player) and (board[1][j + 1] == player) and \
                (board[2][j] == player):
            return True
    
    return False


def main():

    display_title()

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    player1 = 'X'
    player2 = 'O'

    turn_count = 0

    display_board(board)

    current_player = player1

    while turn_count < 9:

        print(f"\n{current_player}'s turn")

        make_move(board, current_player)

        print()

        display_board(board)

        if is_winner(board, current_player):
            print(f"\n{current_player} wins! ")
            break
        elif turn_count == 8 and not is_winner(board, current_player):
            print("\nIt's a tie! ")
            break

        current_player = switch_player(current_player)

        turn_count += 1

    print("\nGame over!")


if __name__ == "__main__":
    main()
