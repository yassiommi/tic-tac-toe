import copy
import numpy as np

# Constants for the board size
ROWS = COLS = 3
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

# Function to check if the board is full
def is_board_full(board):
    return not any(EMPTY in row for row in board)

# Function to check for a winning condition
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return EMPTY

# Function to visualize the Tic-Tac-Toe board
def visualize_board(board):
    for row in board:
        print(" | ".join(["X" if cell == PLAYER_X else "O" if cell == PLAYER_O else " " for cell in row]))
        print("-" * (COLS * 4 - 1))

#   perform the AI move using the Minimax algorithm
def ai_move(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner != EMPTY:
        return 10 - depth if winner == PLAYER_X else -10 + depth, None

    if is_board_full(board):
        return 0, None

    if is_maximizing:
        best_score = -np.inf
        best_move = None

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score, _ = ai_move(board, depth + 1, False)
                    board[i][j] = EMPTY

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_score, best_move
    else:
        best_score = np.inf
        best_move = None

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score, _ = ai_move(board, depth + 1, True)
                    board[i][j] = EMPTY

                    if score < best_score:
                        best_score = score
                        best_move = (i, j)

        return best_score, best_move

#  play the game
def play_game():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    visualize_board(board)

    while not game_over:
        # Player's move
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))

        if board[row][col] != EMPTY or row < 0 or row >= ROWS or col < 0 or col >= COLS:
            print("Invalid move! Try again.")
            continue

        board[row][col] = PLAYER_O
        visualize_board(board)

        winner = check_winner(board)
        if winner == PLAYER_O:
            print("Congratulations! You win!")
            game_over = True
            continue
        elif is_board_full(board):
            print("It's a tie!")
            game_over = True
            continue

        # AI's move
        score, best_move = ai_move(board, 0, True)
        board[best_move[0]][best_move[1]] = PLAYER_X
        print("AI's move:")
        visualize_board(board)

        winner = check_winner(board)
        if winner == PLAYER_X:
            print("AI wins!")
            game_over = True
        elif is_board_full(board):
            print("It's a tie!")
            game_over = True

if __name__ == "__main__":
    play_game()
