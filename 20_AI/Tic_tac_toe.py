# Tic Tac Toe Game

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

#greet the user

def check_winner(board):
    """Checks if there is a winner or the game is a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

def tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"{current_player}'s turn. Enter row and column (0, 1, or 2):")

        try:
            row, col = map(int, input("Row and Column: ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two numbers between 0 and 2.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
