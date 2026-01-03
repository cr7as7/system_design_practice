"""
Design Tic-Tac-Toe Game

This implementation includes:
- Board class for game board management
- Player class for player representation
- Game class for game logic and state management
- GameManager class for managing multiple games
"""

from enum import Enum
from typing import Optional, Tuple, List
import uuid


class GameStatus(Enum):
    """Enum for game status"""
    IN_PROGRESS = "IN_PROGRESS"
    X_WON = "X_WON"
    O_WON = "O_WON"
    DRAW = "DRAW"
    FINISHED = "FINISHED"


class Player:
    """Represents a player in the game"""
    
    def __init__(self, player_id: str, symbol: str):
        """
        Initialize a player
        
        Args:
            player_id: Unique identifier for the player
            symbol: 'X' or 'O'
        """
        if symbol not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")
        self.player_id = player_id
        self.symbol = symbol
    
    def __repr__(self):
        return f"Player(id={self.player_id}, symbol={self.symbol})"


class Board:
    """Represents the Tic-Tac-Toe board"""
    
    def __init__(self, size: int = 3):
        """
        Initialize an empty board
        
        Args:
            size: Size of the board (default 3 for 3x3)
        """
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]
        # For optimized win detection
        self.row_counts = [0] * size  # +1 for X, -1 for O
        self.col_counts = [0] * size
        self.diag_count = 0  # Main diagonal (0,0) to (2,2)
        self.anti_diag_count = 0  # Anti-diagonal (0,2) to (2,0)
    
    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """
        Place a symbol on the board
        
        Args:
            row: Row index (0-based)
            col: Column index (0-based)
            symbol: 'X' or 'O'
        
        Returns:
            True if move was successful, False otherwise
        """
        if not self.is_valid_move(row, col):
            return False
        
        self.board[row][col] = symbol
        
        # Update counts for win detection
        value = 1 if symbol == 'X' else -1
        self.row_counts[row] += value
        self.col_counts[col] += value
        
        if row == col:
            self.diag_count += value
        if row + col == self.size - 1:
            self.anti_diag_count += value
        
        return True
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is valid
        
        Args:
            row: Row index
            col: Column index
        
        Returns:
            True if move is valid, False otherwise
        """
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        return self.board[row][col] == ''
    
    def get_board_state(self) -> List[List[str]]:
        """
        Get current board state (returns a copy)
        
        Returns:
            2D list representing the board
        """
        return [row[:] for row in self.board]
    
    def check_winner(self) -> Optional[str]:
        """
        Check if there's a winner using optimized counting
        
        Returns:
            'X' if X wins, 'O' if O wins, None otherwise
        """
        # Check rows
        for count in self.row_counts:
            if count == self.size:
                return 'X'
            elif count == -self.size:
                return 'O'
        
        # Check columns
        for count in self.col_counts:
            if count == self.size:
                return 'X'
            elif count == -self.size:
                return 'O'
        
        # Check main diagonal
        if self.diag_count == self.size:
            return 'X'
        elif self.diag_count == -self.size:
            return 'O'
        
        # Check anti-diagonal
        if self.anti_diag_count == self.size:
            return 'X'
        elif self.anti_diag_count == -self.size:
            return 'O'
        
        return None
    
    def is_full(self) -> bool:
        """
        Check if board is full
        
        Returns:
            True if board is full, False otherwise
        """
        for row in self.board:
            if '' in row:
                return False
        return True
    
    def reset(self):
        """Reset the board to empty state"""
        self.board = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.row_counts = [0] * self.size
        self.col_counts = [0] * self.size
        self.diag_count = 0
        self.anti_diag_count = 0


class Game:
    """Represents a Tic-Tac-Toe game"""
    
    def __init__(self, player1: Player, player2: Player):
        """
        Initialize a new game
        
        Args:
            player1: First player (will play X)
            player2: Second player (will play O)
        """
        if player1.symbol == player2.symbol:
            raise ValueError("Players must have different symbols")
        
        self.game_id = str(uuid.uuid4())
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1  # X always starts
        self.status = GameStatus.IN_PROGRESS
        self.moves_history = []
    
    def make_move(self, player_id: str, row: int, col: int) -> str:
        """
        Make a move in the game
        
        Args:
            player_id: ID of the player making the move
            row: Row index (0-based)
            col: Column index (0-based)
        
        Returns:
            Status message: 'SUCCESS', 'INVALID_MOVE', 'NOT_YOUR_TURN', 'GAME_OVER', 'INVALID_PLAYER'
        """
        # Check if game is over
        if self.status != GameStatus.IN_PROGRESS:
            return 'GAME_OVER'
        
        # Validate player
        if player_id not in [self.player1.player_id, self.player2.player_id]:
            return 'INVALID_PLAYER'
        
        # Check if it's player's turn
        if player_id != self.current_player.player_id:
            return 'NOT_YOUR_TURN'
        
        # Validate move
        if not self.board.is_valid_move(row, col):
            return 'INVALID_MOVE'
        
        # Make the move
        symbol = self.current_player.symbol
        self.board.make_move(row, col, symbol)
        
        # Record move
        self.moves_history.append({
            'player_id': player_id,
            'symbol': symbol,
            'row': row,
            'col': col
        })
        
        # Check for winner
        winner = self.board.check_winner()
        if winner:
            self.status = GameStatus.X_WON if winner == 'X' else GameStatus.O_WON
            return 'SUCCESS'
        
        # Check for draw
        if self.board.is_full():
            self.status = GameStatus.DRAW
            return 'SUCCESS'
        
        # Switch turns
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        
        return 'SUCCESS'
    
    def get_game_status(self) -> GameStatus:
        """
        Get current game status
        
        Returns:
            Current GameStatus
        """
        return self.status
    
    def get_board_state(self) -> List[List[str]]:
        """
        Get current board state
        
        Returns:
            2D list representing the board
        """
        return self.board.get_board_state()
    
    def get_current_player(self) -> Player:
        """
        Get the player whose turn it is
        
        Returns:
            Current Player object
        """
        return self.current_player
    
    def get_moves_history(self) -> List[dict]:
        """
        Get history of all moves
        
        Returns:
            List of move dictionaries
        """
        return self.moves_history.copy()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board.reset()
        self.current_player = self.player1
        self.status = GameStatus.IN_PROGRESS
        self.moves_history = []
    
    def get_game_id(self) -> str:
        """Get the unique game ID"""
        return self.game_id


class GameManager:
    """Manages multiple Tic-Tac-Toe games"""
    
    def __init__(self):
        """Initialize the game manager"""
        self.games = {}  # game_id -> Game
    
    def create_game(self, player1_id: str, player2_id: str) -> str:
        """
        Create a new game
        
        Args:
            player1_id: ID of first player (will be X)
            player2_id: ID of second player (will be O)
        
        Returns:
            Game ID
        """
        player1 = Player(player1_id, 'X')
        player2 = Player(player2_id, 'O')
        game = Game(player1, player2)
        game_id = game.get_game_id()
        self.games[game_id] = game
        return game_id
    
    def get_game(self, game_id: str) -> Optional[Game]:
        """
        Get a game by ID
        
        Args:
            game_id: Game ID
        
        Returns:
            Game object or None if not found
        """
        return self.games.get(game_id)
    
    def make_move(self, game_id: str, player_id: str, row: int, col: int) -> str:
        """
        Make a move in a specific game
        
        Args:
            game_id: Game ID
            player_id: Player ID
            row: Row index
            col: Column index
        
        Returns:
            Status message
        """
        game = self.games.get(game_id)
        if not game:
            return 'GAME_NOT_FOUND'
        return game.make_move(player_id, row, col)
    
    def delete_game(self, game_id: str) -> bool:
        """
        Delete a game
        
        Args:
            game_id: Game ID
        
        Returns:
            True if deleted, False if not found
        """
        if game_id in self.games:
            del self.games[game_id]
            return True
        return False


# Example usage and testing
if __name__ == "__main__":
    print("=" * 50)
    print("Tic-Tac-Toe Game Design - Example Usage")
    print("=" * 50)
    
    # Example 1: Single game
    print("\n--- Example 1: Single Game ---")
    player1 = Player("player1", "X")
    player2 = Player("player2", "O")
    game = Game(player1, player2)
    
    print(f"Game ID: {game.get_game_id()}")
    print(f"Initial Status: {game.get_game_status().value}")
    
    # Simulate a game
    moves = [
        ("player1", 0, 0),  # X
        ("player2", 1, 1),  # O
        ("player1", 0, 1),  # X
        ("player2", 1, 2),  # O
        ("player1", 0, 2),  # X wins (top row)
    ]
    
    for player_id, row, col in moves:
        result = game.make_move(player_id, row, col)
        print(f"Move by {player_id} at ({row}, {col}): {result}")
        print(f"Board State: {game.get_board_state()}")
        print(f"Status: {game.get_game_status().value}")
        print()
    
    # Example 2: Draw game
    print("\n--- Example 2: Draw Game ---")
    game2 = Game(Player("p1", "X"), Player("p2", "O"))
    draw_moves = [
        ("p1", 0, 0), ("p2", 0, 1), ("p1", 0, 2),
        ("p2", 1, 0), ("p1", 1, 1), ("p2", 1, 2),
        ("p1", 2, 1), ("p2", 2, 0), ("p1", 2, 2),
    ]
    
    for player_id, row, col in draw_moves:
        result = game2.make_move(player_id, row, col)
        print(f"Move by {player_id} at ({row}, {col}): {result}")
        if game2.get_game_status() != GameStatus.IN_PROGRESS:
            break
    
    print(f"Final Status: {game2.get_game_status().value}")
    print(f"Final Board: {game2.get_board_state()}")
    
    # Example 3: Game Manager (multiple games)
    print("\n--- Example 3: Game Manager ---")
    manager = GameManager()
    game_id1 = manager.create_game("alice", "bob")
    game_id2 = manager.create_game("charlie", "diana")
    
    print(f"Created Game 1: {game_id1}")
    print(f"Created Game 2: {game_id2}")
    
    # Make moves in different games
    manager.make_move(game_id1, "alice", 0, 0)
    manager.make_move(game_id2, "charlie", 1, 1)
    
    game1 = manager.get_game(game_id1)
    game2 = manager.get_game(game_id2)
    
    print(f"Game 1 Status: {game1.get_game_status().value}")
    print(f"Game 2 Status: {game2.get_game_status().value}")
    
    # Example 4: Edge cases
    print("\n--- Example 4: Edge Cases ---")
    game3 = Game(Player("x_player", "X"), Player("o_player", "O"))
    
    # Invalid move (out of bounds)
    print(f"Move out of bounds: {game3.make_move('x_player', 5, 5)}")
    
    # Wrong player turn
    game3.make_move("x_player", 0, 0)
    print(f"Wrong player turn: {game3.make_move('x_player', 1, 1)}")
    
    # Move to occupied cell
    print(f"Occupied cell: {game3.make_move('o_player', 0, 0)}")
    
    print("\n" + "=" * 50)

