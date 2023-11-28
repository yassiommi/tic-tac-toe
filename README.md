# Tic-Tac-Toe Game with Minimax Algorithm

This project contains an implementation of the classic Tic-Tac-Toe game where a player can play against an AI opponent that uses the Minimax algorithm to make its moves. The game is implemented in Python and includes text-based visualization of the game board.

## Overview

### Tic-Tac-Toe Game Rules

Tic-Tac-Toe is a two-player game played on a 3x3 grid. Players take turns placing their marks (X or O) on an empty cell. The player who succeeds in placing their marks in a horizontal, vertical, or diagonal row wins the game.

### Minimax Algorithm

The AI player in this implementation uses the Minimax algorithm to make optimal moves. Minimax is a decision-making algorithm used in two-player games where the goal is to maximize the AI player's score while minimizing the opponent's score. It evaluates all possible moves and selects the best move based on a heuristic score.


## How to Play

1. **Run the Program:** run `python main.py` in the terminal.
2. **Game Start:** The game starts with an empty 3x3 grid displayed in the console.
3. **Player's Turn:** Enter row and column numbers (0-2) to place your mark (O) on the grid when prompted.
4. **AI's Turn:** The AI (X) will make its move using the Minimax algorithm.
5. **Game Continues:** The game continues until a player wins or the board is full.
6. **Game Outcome:** The game will announce the winner or declare a tie.

## Sample Usage

A sample run:

```
Welcome to Tic-Tac-Toe!
  |   |  
-----------
  |   |  
-----------
  |   |  
-----------
Enter the row number (0-2): 0
Enter the column number (0-2): 1
  | O |  
-----------
  |   |  
-----------
  |   |  
-----------
AI's move:
X | O |  
-----------
  |   |  
-----------
  |   |  
-----------
Enter the row number (0-2): 1
Enter the column number (0-2): 1
X | O |  
-----------
  | O |  
-----------
  |   |  
-----------
AI's move:
X | O |  
-----------
  | O |  
-----------
  | X |  
-----------
Enter the row number (0-2): 2
Enter the column number (0-2): 1
Invalid move! Try again.
Enter the row number (0-2): 2
Enter the column number (0-2): 0
X | O |  
-----------
  | O |  
-----------
O | X |  
-----------
AI's move:
X | O | X
-----------
  | O |  
-----------
O | X |  
-----------
Enter the row number (0-2): 1
Enter the column number (0-2): 0
X | O | X
-----------
O | O |  
-----------
O | X |  
-----------
AI's move:
X | O | X
-----------
O | O | X
-----------
O | X |  
-----------
Enter the row number (0-2): 2
Enter the column number (0-2): 2
X | O | X
-----------
O | O | X
-----------
O | X | O
-----------
It's a tie!
```
