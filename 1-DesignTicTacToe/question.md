# Design Tic-Tac-Toe Game

## Problem Statement

Design a Tic-Tac-Toe game that supports two players (X and O) playing on a 3x3 grid. The game should handle moves, validate them, detect win/draw conditions, and support multiple concurrent games.

## Requirements

### Functional Requirements
1. Initialize a new game with two players
2. Players take turns making moves
3. Validate moves (prevent invalid moves like out of bounds, occupied cells, wrong turn)
4. Detect win condition after each move (horizontal, vertical, or diagonal)
5. Detect draw condition when board is full with no winner
6. Track game state (in progress, X won, O won, draw)
7. Support multiple concurrent games (optional)

### Non-Functional Requirements
- Low latency for move validation and win detection (O(1) preferred)
- Clean, extensible design
- Thread-safe design (if supporting multiple games)

## Constraints
- Board size: 3x3 (should be extensible to NxN)
- Two players only (X and O)
- Standard Tic-Tac-Toe rules apply

## Example

```
# Initialize game
player1 = Player("player1", "X")
player2 = Player("player2", "O")
game = Game(player1, player2)

# Make moves
game.make_move("player1", 0, 0)  # Returns 'SUCCESS'
game.make_move("player2", 1, 1)  # Returns 'SUCCESS'
game.make_move("player1", 0, 1)  # Returns 'SUCCESS'
game.make_move("player2", 1, 2)  # Returns 'SUCCESS'
game.make_move("player1", 0, 2)  # Returns 'SUCCESS', X wins (top row)

# Check status
game.get_game_status()  # Returns GameStatus.X_WON
```

## Expected Output

Design and implement:
1. **Player class**: Represents a player with ID and symbol
2. **Board class**: Manages the game board, validates moves, detects wins
3. **Game class**: Orchestrates game flow, manages turns, tracks state
4. **GameManager class** (optional): Manages multiple concurrent games

## Follow-up Questions (to ask interviewer)

1. **Should we support multiple concurrent games?**
   - **Answer**: Yes, for extensibility. We'll implement a GameManager class to handle multiple games.

2. **Do we need to persist game history?**
   - **Answer**: Yes, for replay feature. We'll maintain a moves_history list in the Game class.

3. **Should we support replay of games?**
   - **Answer**: Yes, we'll store move history to enable replay functionality. This can be implemented using the moves_history.

4. **Any requirement for time limits per move?**
   - **Answer**: Not required for MVP. Can be added later if needed.

5. **Do we need to support custom board sizes (NxN)?**
   - **Answer**: Start with 3x3, but design should be extensible to NxN. Board class accepts size parameter for future extension.
