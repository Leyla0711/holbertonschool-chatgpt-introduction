#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks for a winner in the game."""
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Checks if the game is a draw (board is full with no winner)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize empty board
    player = "X"  # Starting player

    while True:
        print_board(board)
        
        # Ask for row input with validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row < 0 or row > 2:
                    print("Invalid row. Please enter a row between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

        # Ask for column input with validation
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col < 0 or col > 2:
                    print("Invalid column. Please enter a column between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

        # Check if the spot is taken
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue  # Skip to the next iteration of the loop to ask for new inputs

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

