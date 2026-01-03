/**
 * Design Tic-Tac-Toe Game - Java Implementation (Reference)
 * 
 * Key differences from Python:
 * 1. Strong typing with explicit type declarations
 * 2. Public/private access modifiers
 * 3. Getter/setter methods pattern
 * 4. No default parameters (use method overloading)
 * 5. Enum with explicit constructors
 * 6. ArrayList instead of list
 * 7. HashMap instead of dict
 */

import java.util.*;

enum GameStatus {
    IN_PROGRESS("IN_PROGRESS"),
    X_WON("X_WON"),
    O_WON("O_WON"),
    DRAW("DRAW"),
    FINISHED("FINISHED");
    
    private final String value;
    
    GameStatus(String value) {
        this.value = value;
    }
    
    public String getValue() {
        return value;
    }
}

class Player {
    private String playerId;
    private char symbol;
    
    public Player(String playerId, char symbol) {
        if (symbol != 'X' && symbol != 'O') {
            throw new IllegalArgumentException("Symbol must be 'X' or 'O'");
        }
        this.playerId = playerId;
        this.symbol = symbol;
    }
    
    public String getPlayerId() {
        return playerId;
    }
    
    public char getSymbol() {
        return symbol;
    }
    
    @Override
    public String toString() {
        return "Player(id=" + playerId + ", symbol=" + symbol + ")";
    }
}

class Board {
    private int size;
    private char[][] board;
    private int[] rowCounts;
    private int[] colCounts;
    private int diagCount;
    private int antiDiagCount;
    
    public Board() {
        this(3);
    }
    
    public Board(int size) {
        this.size = size;
        this.board = new char[size][size];
        this.rowCounts = new int[size];
        this.colCounts = new int[size];
        this.diagCount = 0;
        this.antiDiagCount = 0;
    }
    
    public boolean makeMove(int row, int col, char symbol) {
        if (!isValidMove(row, col)) {
            return false;
        }
        
        board[row][col] = symbol;
        
        // Update counts for win detection
        int value = (symbol == 'X') ? 1 : -1;
        rowCounts[row] += value;
        colCounts[col] += value;
        
        if (row == col) {
            diagCount += value;
        }
        if (row + col == size - 1) {
            antiDiagCount += value;
        }
        
        return true;
    }
    
    public boolean isValidMove(int row, int col) {
        if (row < 0 || row >= size || col < 0 || col >= size) {
            return false;
        }
        return board[row][col] == '\0'; // '\0' represents empty in Java
    }
    
    public char[][] getBoardState() {
        char[][] copy = new char[size][size];
        for (int i = 0; i < size; i++) {
            System.arraycopy(board[i], 0, copy[i], 0, size);
        }
        return copy;
    }
    
    public Character checkWinner() {
        // Check rows
        for (int count : rowCounts) {
            if (count == size) return 'X';
            if (count == -size) return 'O';
        }
        
        // Check columns
        for (int count : colCounts) {
            if (count == size) return 'X';
            if (count == -size) return 'O';
        }
        
        // Check diagonals
        if (diagCount == size) return 'X';
        if (diagCount == -size) return 'O';
        if (antiDiagCount == size) return 'X';
        if (antiDiagCount == -size) return 'O';
        
        return null;
    }
    
    public boolean isFull() {
        for (char[] row : board) {
            for (char cell : row) {
                if (cell == '\0') {
                    return false;
                }
            }
        }
        return true;
    }
    
    public void reset() {
        board = new char[size][size];
        rowCounts = new int[size];
        colCounts = new int[size];
        diagCount = 0;
        antiDiagCount = 0;
    }
}

class Game {
    private String gameId;
    private Board board;
    private Player player1;
    private Player player2;
    private Player currentPlayer;
    private GameStatus status;
    private List<Map<String, Object>> movesHistory;
    
    public Game(Player player1, Player player2) {
        if (player1.getSymbol() == player2.getSymbol()) {
            throw new IllegalArgumentException("Players must have different symbols");
        }
        
        this.gameId = UUID.randomUUID().toString();
        this.board = new Board();
        this.player1 = player1;
        this.player2 = player2;
        this.currentPlayer = player1;
        this.status = GameStatus.IN_PROGRESS;
        this.movesHistory = new ArrayList<>();
    }
    
    public String makeMove(String playerId, int row, int col) {
        // Check if game is over
        if (status != GameStatus.IN_PROGRESS) {
            return "GAME_OVER";
        }
        
        // Validate player
        if (!playerId.equals(player1.getPlayerId()) && !playerId.equals(player2.getPlayerId())) {
            return "INVALID_PLAYER";
        }
        
        // Check if it's player's turn
        if (!playerId.equals(currentPlayer.getPlayerId())) {
            return "NOT_YOUR_TURN";
        }
        
        // Validate move
        if (!board.isValidMove(row, col)) {
            return "INVALID_MOVE";
        }
        
        // Make the move
        char symbol = currentPlayer.getSymbol();
        board.makeMove(row, col, symbol);
        
        // Record move
        Map<String, Object> move = new HashMap<>();
        move.put("player_id", playerId);
        move.put("symbol", String.valueOf(symbol));
        move.put("row", row);
        move.put("col", col);
        movesHistory.add(move);
        
        // Check for winner
        Character winner = board.checkWinner();
        if (winner != null) {
            status = (winner == 'X') ? GameStatus.X_WON : GameStatus.O_WON;
            return "SUCCESS";
        }
        
        // Check for draw
        if (board.isFull()) {
            status = GameStatus.DRAW;
            return "SUCCESS";
        }
        
        // Switch turns
        currentPlayer = (currentPlayer == player1) ? player2 : player1;
        
        return "SUCCESS";
    }
    
    public GameStatus getGameStatus() {
        return status;
    }
    
    public char[][] getBoardState() {
        return board.getBoardState();
    }
    
    public Player getCurrentPlayer() {
        return currentPlayer;
    }
    
    public List<Map<String, Object>> getMovesHistory() {
        return new ArrayList<>(movesHistory); // Return copy
    }
    
    public void resetGame() {
        board.reset();
        currentPlayer = player1;
        status = GameStatus.IN_PROGRESS;
        movesHistory.clear();
    }
    
    public String getGameId() {
        return gameId;
    }
}

class GameManager {
    private Map<String, Game> games;
    
    public GameManager() {
        this.games = new HashMap<>();
    }
    
    public String createGame(String player1Id, String player2Id) {
        Player player1 = new Player(player1Id, 'X');
        Player player2 = new Player(player2Id, 'O');
        Game game = new Game(player1, player2);
        String gameId = game.getGameId();
        games.put(gameId, game);
        return gameId;
    }
    
    public Game getGame(String gameId) {
        return games.get(gameId);
    }
    
    public String makeMove(String gameId, String playerId, int row, int col) {
        Game game = games.get(gameId);
        if (game == null) {
            return "GAME_NOT_FOUND";
        }
        return game.makeMove(playerId, row, col);
    }
    
    public boolean deleteGame(String gameId) {
        return games.remove(gameId) != null;
    }
}

// Example usage
public class TicTacToe {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("Tic-Tac-Toe Game Design - Java Example");
        System.out.println("==================================================");
        
        // Example 1: Single game
        System.out.println("\n--- Example 1: Single Game ---");
        Player player1 = new Player("player1", 'X');
        Player player2 = new Player("player2", 'O');
        Game game = new Game(player1, player2);
        
        System.out.println("Game ID: " + game.getGameId());
        System.out.println("Initial Status: " + game.getGameStatus().getValue());
        
        // Make moves
        String result1 = game.makeMove("player1", 0, 0);
        System.out.println("Move by player1 at (0, 0): " + result1);
        System.out.println("Status: " + game.getGameStatus().getValue());
        
        String result2 = game.makeMove("player2", 1, 1);
        System.out.println("Move by player2 at (1, 1): " + result2);
        System.out.println("Status: " + game.getGameStatus().getValue());
    }
}

