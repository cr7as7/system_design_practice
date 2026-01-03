# Design Tic-Tac-Toe Game - Approach

## Step 1: Understand Requirements

### Problem Analysis
- **Two players**: X and O playing on a 3x3 grid
- **Turn-based**: Players alternate turns
- **Win detection**: Check if a player has won (horizontal, vertical, or diagonal line)
- **Draw detection**: Game ends in draw when board is full with no winner
- **Move validation**: Prevent invalid moves (out of bounds, occupied cells, wrong turn)

### Questions to Clarify (if in interview)
1. Should we support multiple concurrent games? → Yes, for extensibility
2. Do we need to persist game history? → Yes, for replay feature
3. Any time limits? → Not required for MVP
4. Custom board sizes? → Start with 3x3, can extend later

---

## Step 2: Identify Core Components

Break down the problem into logical components:

1. **Board**: Manages the 3x3 grid state
2. **Player**: Represents a player with ID and symbol
3. **Game**: Orchestrates game flow, manages turns, tracks state
4. **GameManager**: (Optional) Manages multiple concurrent games

---

## Step 3: Design Classes

### Class 1: Player
**Purpose**: Simple data holder for player information

**Attributes**:
- `player_id`: Unique identifier
- `symbol`: 'X' or 'O'

**Methods**:
- Constructor with validation

**Design Decision**: Keep it simple, just stores data.

---

### Class 2: Board
**Purpose**: Manages the game board state and validates moves

**Attributes**:
- `board`: 2D array representing the grid
- `row_counts`: Array to track row sums (for optimized win detection)
- `col_counts`: Array to track column sums
- `diag_count`: Main diagonal count
- `anti_diag_count`: Anti-diagonal count

**Methods**:
- `make_move(row, col, symbol)`: Place a symbol on the board
- `is_valid_move(row, col)`: Check if move is valid
- `check_winner()`: Check if there's a winner
- `is_full()`: Check if board is full
- `get_board_state()`: Return current board state
- `reset()`: Reset board to initial state

**Key Design Decision**: 
- Use count-based win detection instead of checking all 8 combinations
- Maintain running counts: +1 for X, -1 for O
- If any count reaches 3 or -3, we have a winner
- **Time Complexity**: O(1) for win detection
- **Space Complexity**: O(n) where n=3

---

### Class 3: Game
**Purpose**: Orchestrates the game flow and manages game state

**Attributes**:
- `game_id`: Unique game identifier
- `board`: Board instance
- `player1`, `player2`: Player instances
- `current_player`: Whose turn it is
- `status`: Current game status (IN_PROGRESS, X_WON, O_WON, DRAW)
- `moves_history`: List of all moves made

**Methods**:
- `make_move(player_id, row, col)`: Process a move
- `get_game_status()`: Get current status
- `get_board_state()`: Get board state
- `get_current_player()`: Get whose turn it is
- `get_moves_history()`: Get move history
- `reset_game()`: Reset game

**Key Design Decisions**:
- Return status strings for move operations ('SUCCESS', 'INVALID_MOVE', etc.)
- X always starts first
- Switch turns after successful move
- Check win/draw after each move

---

### Class 4: GameManager (Optional)
**Purpose**: Manages multiple concurrent games

**Attributes**:
- `games`: Dictionary mapping game_id to Game

**Methods**:
- `create_game(player1_id, player2_id)`: Create new game
- `get_game(game_id)`: Retrieve game
- `make_move(game_id, player_id, row, col)`: Make move in specific game
- `delete_game(game_id)`: Delete game

---

## Step 4: Algorithm Design

### Win Detection Algorithm

**Option 1: Naive Approach**
```
After each move, check all 8 winning combinations:
- 3 rows
- 3 columns
- 2 diagonals
Time: O(1) but checks 8 combinations = 8 checks
```

**Option 2: Optimized Count-Based Approach** (Chosen)
```
Maintain running counts:
- For each row: row_counts[i]
- For each column: col_counts[i]
- Main diagonal: diag_count
- Anti-diagonal: anti_diag_count

On each move:
- X move: increment by 1
- O move: decrement by 1
- Check if any count == 3 (X wins) or == -3 (O wins)

Time: O(1) with only 4-6 checks
Space: O(n) where n=3
```

**Why Option 2?**
- More efficient for larger boards (if extended to NxN)
- Cleaner code
- Same time complexity, but fewer actual checks

---

## Step 5: Edge Cases & Error Handling

1. **Invalid Move - Out of Bounds**
   - Check: `row < 0 || row >= size || col < 0 || col >= size`
   - Return: `'INVALID_MOVE'`

2. **Invalid Move - Cell Already Occupied**
   - Check: `board[row][col] != ''`
   - Return: `'INVALID_MOVE'`

3. **Wrong Player Turn**
   - Check: `player_id != current_player.player_id`
   - Return: `'NOT_YOUR_TURN'`

4. **Move After Game Over**
   - Check: `status != IN_PROGRESS`
   - Return: `'GAME_OVER'`

5. **Invalid Player ID**
   - Check: `player_id not in [player1.id, player2.id]`
   - Return: `'INVALID_PLAYER'`

6. **Draw Condition**
   - Check: `board.is_full() && no winner`
   - Status: `DRAW`

---

## Step 6: Implementation Order

1. **Player class** (simplest, no dependencies)
2. **Board class** (core logic, independent)
3. **Game class** (uses Player and Board)
4. **GameManager class** (uses Game)

This order allows testing each component independently.

---

## Step 7: Time & Space Complexity

### Time Complexity
- `make_move()`: O(1) - constant time validation and win check
- `check_winner()`: O(1) - checks 4-6 counts
- `is_valid_move()`: O(1) - bounds check and cell check
- `is_full()`: O(n²) where n=3 → O(9) = O(1)

### Space Complexity
- Board storage: O(n²) where n=3 → O(1) for fixed 3x3
- Count arrays: O(n) where n=3 → O(1)
- Move history: O(m) where m = number of moves (max 9)
- **Overall**: O(1) for fixed 3x3 board

---

## Step 8: Testing Strategy

1. **Valid Game Flow**
   - Complete a game with X winning
   - Complete a game with O winning
   - Complete a draw game

2. **Win Scenarios**
   - Win by row
   - Win by column
   - Win by main diagonal
   - Win by anti-diagonal

3. **Edge Cases**
   - Invalid moves (all types)
   - Wrong player turn
   - Move after game over
   - Multiple games concurrently

4. **Edge Cases in Win Detection**
   - Win on last move (9th move)
   - Draw on last move (9th move, no winner)

---

## Step 9: Extensions (If Asked)

1. **NxN Board**: Extend Board class to accept size parameter
2. **AI Player**: Add minimax algorithm
3. **Tournament Mode**: Multiple games in series
4. **Statistics**: Track win/loss records
5. **Replay System**: Replay games from move history
6. **Time Limits**: Add timer per move
7. **Spectator Mode**: Allow watching ongoing games

---

## Detailed "Why" Explanations

### Why Separate Classes (Player, Board, Game, GameManager)?

**Why this approach?**
- **Separation of Concerns**: Each class has a single, clear responsibility
  - Player: Just stores player data
  - Board: Manages board state and win detection logic
  - Game: Orchestrates game flow and rules
  - GameManager: Manages multiple games
- **Testability**: Each class can be tested independently
- **Maintainability**: Changes to one component don't affect others
- **Reusability**: Board class can be reused for different game types

**Why not a single class?**
- A single TicTacToe class would violate Single Responsibility Principle
- Harder to test individual components
- Difficult to extend (e.g., adding AI player, tournament mode)
- Code becomes harder to read and maintain

**Trade-offs**:
- More files/classes to manage
- Slightly more overhead in method calls
- But benefits in clarity, testability, and extensibility far outweigh costs

---

### Why Count-Based Win Detection?

**Why this approach?**
- **Efficiency**: O(1) time complexity for win detection
- **Scalability**: Works efficiently even for NxN boards
- **Simplicity**: Cleaner code than checking all combinations
- **Performance**: Only checks 4-6 conditions (rows, cols, diagonals) instead of 8+ combinations

**Why not check all combinations after each move?**
- **Naive approach**: Check all 8 winning combinations (3 rows, 3 cols, 2 diagonals)
  - Time: Still O(1) but more checks (8+ comparisons)
  - Code: More verbose, harder to maintain
  - Not scalable: For NxN, would need to check 2N+2 combinations
- **Brute force**: Check entire board state
  - Time: O(n²) - very inefficient
  - Unnecessary: Only need to check lines affected by the move

**Why not use bit manipulation?**
- Bit manipulation could work but:
  - Less readable code
  - More complex to understand and maintain
  - Only works for small boards (up to certain size)
  - Count-based approach is clearer and equally efficient

**Trade-offs**:
- Uses extra space (O(n) for count arrays)
- But provides O(1) win detection with cleaner code
- Space cost is minimal (only 3+3+2 = 8 integers for 3x3 board)

---

### Why Use Enum for GameStatus?

**Why this approach?**
- **Type Safety**: Prevents invalid status values
- **Readability**: `GameStatus.X_WON` is clearer than magic strings like `"X_WON"`
- **Maintainability**: Centralized status definitions
- **IDE Support**: Autocomplete and refactoring support

**Why not use strings?**
- **Type Safety**: Strings can have typos (`"X_WON"` vs `"XWON"`)
- **No Validation**: Any string is accepted, even invalid ones
- **Refactoring**: Hard to rename status values across codebase
- **Performance**: Slight overhead in string comparisons (minimal but unnecessary)

**Why not use integers?**
- **Readability**: `status = 1` is unclear compared to `status = GameStatus.X_WON`
- **Magic Numbers**: Hard to remember what each number means
- **No Type Safety**: Any integer can be assigned

**Trade-offs**:
- Slightly more verbose than strings
- But provides type safety and better code quality

---

### Why Store Move History?

**Why this approach?**
- **Replay Feature**: Can replay games move by move
- **Debugging**: Helps identify issues in game logic
- **Analytics**: Can analyze player strategies
- **Undo Feature**: Can implement undo if needed
- **Audit Trail**: Record of all moves for disputes

**Why not store just final state?**
- **Loss of Information**: Cannot reconstruct game progression
- **No Replay**: Cannot show how game unfolded
- **Limited Debugging**: Hard to trace issues

**Trade-offs**:
- Uses O(m) space where m = number of moves (max 9 for 3x3)
- But provides valuable features and debugging capability
- Space cost is minimal (9 moves * small dict = negligible)

---

### Why Return Status Strings from make_move()?

**Why this approach?**
- **Clear Feedback**: Caller knows exactly what happened
- **Error Handling**: Easy to check for errors and handle appropriately
- **Debugging**: Status messages help debug issues
- **API Design**: Common pattern in game APIs

**Why not use exceptions?**
- **Control Flow**: Exceptions should be for exceptional cases, not normal flow
- **Performance**: Exceptions have overhead for expected cases like invalid moves
- **Readability**: Status strings are clearer for expected outcomes

**Why not use boolean (true/false)?**
- **Limited Information**: Doesn't tell why move failed
- **Error Handling**: Caller needs to guess the reason
- **Debugging**: Hard to debug without knowing specific error

**Trade-offs**:
- More string comparisons (minimal performance cost)
- But provides better error handling and debugging
- Standard pattern in game development APIs

---

### Why X Always Starts First?

**Why this approach?**
- **Convention**: Standard Tic-Tac-Toe rule
- **Simplicity**: No need to decide who starts
- **Consistency**: Same behavior every game

**Why not random start?**
- **Complexity**: Need random number generation
- **Fairness**: Not necessary for this problem
- **Consistency**: Random starts make testing harder

**Trade-offs**:
- Less flexible (always X first)
- But simpler and follows standard rules
- Can be extended later if needed

---

### Why Use UUID for Game IDs?

**Why this approach?**
- **Uniqueness**: Guarantees unique IDs across all games
- **Security**: Hard to guess (unlike sequential IDs)
- **Distributed Systems**: Works across multiple servers
- **No Collision**: Extremely low probability of duplicates

**Why not use sequential integers?**
- **Collision Risk**: Need to track last used ID
- **Security**: Predictable IDs (1, 2, 3...)
- **Scalability**: Difficult in distributed systems
- **Concurrency**: Need locking to generate unique sequential IDs

**Why not use player IDs?**
- **Multiple Games**: Same players can play multiple games
- **Uniqueness**: Not guaranteed to be unique
- **Not Descriptive**: Doesn't identify a specific game instance

**Trade-offs**:
- UUIDs are longer strings (36 chars)
- But provide uniqueness and security
- Standard practice in distributed systems

---

### Why Separate Board Class from Game Class?

**Why this approach?**
- **Single Responsibility**: Board manages state, Game manages rules
- **Reusability**: Board can be used in other contexts
- **Testability**: Board logic can be tested independently
- **Clear Separation**: Win detection logic separate from game flow logic

**Why not combine into Game class?**
- **Violates SRP**: Game class would handle both board state and game rules
- **Tight Coupling**: Hard to change board implementation without affecting game
- **Testing**: Harder to test board logic in isolation
- **Reusability**: Cannot reuse board logic elsewhere

**Trade-offs**:
- One more class to manage
- But provides better separation and testability
- Standard OOP design principle

---

### Why Use Dictionary/Map for GameManager?

**Why this approach?**
- **Fast Lookup**: O(1) average case lookup by game_id
- **Easy Management**: Simple add/remove operations
- **Standard Pattern**: Common pattern for managing collections by ID

**Why not use List/Array?**
- **Lookup Time**: O(n) to find game by ID
- **Inefficient**: Need to search through all games
- **Not Scalable**: Performance degrades with more games

**Why not use Database?**
- **Overkill**: For in-memory game management, database is unnecessary
- **Latency**: Database access is slower than in-memory
- **Complexity**: Adds database dependencies and setup

**Trade-offs**:
- Uses O(g) space where g = number of games
- But provides O(1) lookup performance
- Standard choice for this use case

---

## Key Takeaways

1. **Start Simple**: Basic game with two players first
2. **Optimize Win Detection**: Use count-based approach for O(1) complexity
3. **Handle Edge Cases**: Invalid moves, wrong turns, game over states
4. **Clean Separation**: Each class has clear responsibility
5. **Extensible Design**: Easy to add features like AI, tournaments, etc.
6. **Type Safety**: Use enums instead of strings for status
7. **Error Handling**: Return clear status messages instead of exceptions
8. **Performance**: Choose data structures (maps, arrays) for O(1) operations
