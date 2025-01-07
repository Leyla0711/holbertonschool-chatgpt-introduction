#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        
        # Get valid input for row
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                if row not in [0, 1, 2]:
                    print("Invalid row. Please enter a number between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # Get valid input for column
        while True:
            try:
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if col not in [0, 1, 2]:
                    print("Invalid column. Please enter a number between 0 and 2.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        if board[row][col] == " ":
            board[row][col] = player
            # Switch player after a valid move
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
    
    print_board(board)
    # Print the correct winner
    winner = "O" if player == "X" else "X"
    print(f"Player {winner} wins!")

tic_tac_toe()

