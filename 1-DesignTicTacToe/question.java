/**
 * Design Tic-Tac-Toe Game - Skeleton Code for Practice
 * 
 * Fill in the TODO sections to complete the implementation.
 * This is the structure you should implement in an interview.
 */

import java.util.*;

enum GameStatus {
    // TODO: Define enum values: IN_PROGRESS, X_WON, O_WON, DRAW, FINISHED
    // TODO: Add constructor that takes a String value
    // TODO: Add getValue() method to return the string value
}

class Player {
    // TODO: Add private fields: playerId (String), symbol (char)
    
    public Player(String playerId, char symbol) {
        // TODO: Validate symbol is 'X' or 'O', throw IllegalArgumentException if not
        // TODO: Initialize playerId and symbol
    }
    
    public String getPlayerId() {
        // TODO: Return playerId
        return null;
    }
    
    public char getSymbol() {
        // TODO: Return symbol
        return '\0';
    }
    
    @Override
    public String toString() {
        // TODO: Return string like "Player(id=player1, symbol=X)"
        return "";
    }
}

class Board {
    // TODO: Add private fields:
    //   - size (int)
    //   - board (char[][])
    //   - rowCounts (int[])
    //   - colCounts (int[])
    //   - diagCount (int)
    //   - antiDiagCount (int)
    
    public Board() {
        // TODO: Call this(3) to use default size
    }
    
    public Board(int size) {
        // TODO: Initialize size
        // TODO: Initialize board as char[size][size] (empty cells are '\0')
        // TODO: Initialize rowCounts and colCounts as int[size]
        // TODO: Initialize diagCount and antiDiagCount to 0
    }
    
    public boolean makeMove(int row, int col, char symbol) {
        // TODO: Check if move is valid using isValidMove()
        // TODO: If valid:
        //   - Set board[row][col] = symbol
        //   - Calculate value: 1 for 'X', -1 for 'O'
        //   - Update rowCounts[row] += value
        //   - Update colCounts[col] += value
        //   - If row == col, update diagCount += value
        //   - If row + col == size - 1, update antiDiagCount += value
        // TODO: Return true if successful, false otherwise
        return false;
    }
    
    public boolean isValidMove(int row, int col) {
        // TODO: Check bounds: row >= 0 && row < size && col >= 0 && col < size
        // TODO: Check if board[row][col] == '\0' (empty)
        // TODO: Return true if valid, false otherwise
        return false;
    }
    
    public char[][] getBoardState() {
        // TODO: Create a deep copy of board and return it
        // TODO: Use System.arraycopy or manual copying
        return null;
    }
    
    public Character checkWinner() {
        // TODO: Check rowCounts: if any count == size return 'X', if == -size return 'O'
        // TODO: Check colCounts: if any count == size return 'X', if == -size return 'O'
        // TODO: Check diagCount: if == size return 'X', if == -size return 'O'
        // TODO: Check antiDiagCount: if == size return 'X', if == -size return 'O'
        // TODO: Return null if no winner
        return null;
    }
    
    public boolean isFull() {
        // TODO: Check if all cells in board are non-empty (not '\0')
        // TODO: Return true if full, false otherwise
        return false;
    }
    
    public void reset() {
        // TODO: Reset board to new char[size][size]
        // TODO: Reset rowCounts and colCounts to new int[size]
        // TODO: Reset diagCount and antiDiagCount to 0
    }
}

class Game {
    // TODO: Add private fields:
    //   - gameId (String)
    //   - board (Board)
    //   - player1, player2 (Player)
    //   - currentPlayer (Player)
    //   - status (GameStatus)
    //   - movesHistory (List<Map<String, Object>>)
    
    public Game(Player player1, Player player2) {
        // TODO: Validate players have different symbols, throw exception if same
        // TODO: Generate gameId using UUID.randomUUID().toString()
        // TODO: Create new Board()
        // TODO: Initialize player1, player2, currentPlayer = player1
        // TODO: Set status = GameStatus.IN_PROGRESS
        // TODO: Initialize movesHistory as new ArrayList<>()
    }
    
    public String makeMove(String playerId, int row, int col) {
        // TODO: Check if status != IN_PROGRESS → return "GAME_OVER"
        // TODO: Validate playerId → return "INVALID_PLAYER" if not valid
        // TODO: Check if it's player's turn → return "NOT_YOUR_TURN" if not
        // TODO: Validate move → return "INVALID_MOVE" if not valid
        // TODO: Make the move using board.makeMove()
        // TODO: Record move in movesHistory (HashMap with player_id, symbol, row, col)
        // TODO: Check for winner → update status and return "SUCCESS" if winner
        // TODO: Check if board is full → update status to DRAW and return "SUCCESS"
        // TODO: Switch currentPlayer and return "SUCCESS"
        return "";
    }
    
    public GameStatus getGameStatus() {
        // TODO: Return status
        return null;
    }
    
    public char[][] getBoardState() {
        // TODO: Return board.getBoardState()
        return null;
    }
    
    public Player getCurrentPlayer() {
        // TODO: Return currentPlayer
        return null;
    }
    
    public List<Map<String, Object>> getMovesHistory() {
        // TODO: Return new ArrayList<>(movesHistory) (copy)
        return null;
    }
    
    public void resetGame() {
        // TODO: Call board.reset()
        // TODO: Set currentPlayer = player1
        // TODO: Set status = GameStatus.IN_PROGRESS
        // TODO: Clear movesHistory
    }
    
    public String getGameId() {
        // TODO: Return gameId
        return "";
    }
}

class GameManager {
    // TODO: Add private field: games (Map<String, Game>)
    
    public GameManager() {
        // TODO: Initialize games as new HashMap<>()
    }
    
    public String createGame(String player1Id, String player2Id) {
        // TODO: Create Player instances (player1 with 'X', player2 with 'O')
        // TODO: Create new Game
        // TODO: Get gameId from game
        // TODO: Store game in games map
        // TODO: Return gameId
        return "";
    }
    
    public Game getGame(String gameId) {
        // TODO: Return game from games map, or null if not found
        return null;
    }
    
    public String makeMove(String gameId, String playerId, int row, int col) {
        // TODO: Get game from games map
        // TODO: If null, return "GAME_NOT_FOUND"
        // TODO: Otherwise, return game.makeMove(playerId, row, col)
        return "";
    }
    
    public boolean deleteGame(String gameId) {
        // TODO: Remove game from games map
        // TODO: Return true if removed (games.remove() != null), false otherwise
        return false;
    }
}

// Example usage (commented out for practice)
// public class TicTacToe {
//     public static void main(String[] args) {
//         Player player1 = new Player("player1", 'X');
//         Player player2 = new Player("player2", 'O');
//         Game game = new Game(player1, player2);
//         
//         System.out.println("Game ID: " + game.getGameId());
//         System.out.println("Status: " + game.getGameStatus().getValue());
//         
//         String result = game.makeMove("player1", 0, 0);
//         System.out.println("Move result: " + result);
//     }
// }

