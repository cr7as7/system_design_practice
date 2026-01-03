"""
Design Tic-Tac-Toe Game - Skeleton Code for Practice

Fill in the TODO sections to complete the implementation.
This is the structure you should implement in an interview.
"""

from enum import Enum
from typing import Optional, Tuple, List
import uuid


class GameStatus(Enum):
    """Enum for game status"""
    # TODO: Define enum values: IN_PROGRESS, X_WON, O_WON, DRAW, FINISHED
    pass


class Player:
    """Represents a player in the game"""
    
    def __init__(self, player_id: str, symbol: str):
        """
        Initialize a player
        
        TODO:
        - Validate that symbol is 'X' or 'O'
        - Raise ValueError if symbol is invalid
        - Store player_id and symbol as instance variables
        """
        # TODO: Add validation and initialization
        pass
    
    def __repr__(self):
        """
        TODO: Return string representation like "Player(id=player1, symbol=X)"
        """
        pass


class Board:
    """Represents the Tic-Tac-Toe board"""
    
    def __init__(self, size: int = 3):
        """
        Initialize an empty board
        
        TODO:
        - Store size as instance variable
        - Initialize board as 2D list of empty strings (size x size)
        - Initialize row_counts, col_counts arrays (for optimized win detection)
        - Initialize diag_count and anti_diag_count to 0
        """
        # TODO: Initialize board and count arrays
        pass
    
    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """
        Place a symbol on the board
        
        TODO:
        - Check if move is valid using is_valid_move()
        - If valid: place symbol on board[row][col]
        - Update counts: +1 for X, -1 for O
          - Update row_counts[row]
          - Update col_counts[col]
          - Update diag_count if row == col (main diagonal)
          - Update anti_diag_count if row + col == size - 1 (anti-diagonal)
        - Return True if successful, False otherwise
        """
        # TODO: Implement move logic
        pass
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is valid
        
        TODO:
        - Check if row and col are within bounds (0 to size-1)
        - Check if board[row][col] is empty (empty string)
        - Return True if valid, False otherwise
        """
        # TODO: Implement validation logic
        pass
    
    def get_board_state(self) -> List[List[str]]:
        """
        Get current board state (returns a copy)
        
        TODO:
        - Return a deep copy of the board (use list comprehension with slicing)
        """
        # TODO: Return copy of board
        pass
    
    def check_winner(self) -> Optional[str]:
        """
        Check if there's a winner using optimized counting
        
        TODO:
        - Check row_counts: if any count == size, X wins; if == -size, O wins
        - Check col_counts: if any count == size, X wins; if == -size, O wins
        - Check diag_count: if == size, X wins; if == -size, O wins
        - Check anti_diag_count: if == size, X wins; if == -size, O wins
        - Return 'X' if X wins, 'O' if O wins, None otherwise
        """
        # TODO: Implement win detection using counts
        pass
    
    def is_full(self) -> bool:
        """
        Check if board is full
        
        TODO:
        - Check if all cells in board are non-empty
        - Return True if full, False otherwise
        """
        # TODO: Check if board is full
        pass
    
    def reset(self):
        """
        Reset the board to empty state
        
        TODO:
        - Reset board to empty 2D list
        - Reset all counts to 0
        """
        # TODO: Reset board and counts
        pass


class Game:
    """Represents a Tic-Tac-Toe game"""
    
    def __init__(self, player1: Player, player2: Player):
        """
        Initialize a new game
        
        TODO:
        - Validate that players have different symbols
        - Generate unique game_id using uuid.uuid4()
        - Create a new Board instance
        - Store player1, player2
        - Set current_player to player1 (X always starts)
        - Set status to GameStatus.IN_PROGRESS
        - Initialize moves_history as empty list
        """
        # TODO: Initialize game state
        pass
    
    def make_move(self, player_id: str, row: int, col: int) -> str:
        """
        Make a move in the game
        
        TODO:
        - Check if game is over (status != IN_PROGRESS) → return 'GAME_OVER'
        - Validate player_id is one of the game players → return 'INVALID_PLAYER' if not
        - Check if it's player's turn → return 'NOT_YOUR_TURN' if not
        - Validate move using board.is_valid_move() → return 'INVALID_MOVE' if not
        - Make the move using board.make_move()
        - Record move in moves_history (dict with player_id, symbol, row, col)
        - Check for winner using board.check_winner()
          - If winner exists, update status (X_WON or O_WON) and return 'SUCCESS'
        - Check if board is full → update status to DRAW and return 'SUCCESS'
        - Switch current_player and return 'SUCCESS'
        """
        # TODO: Implement move logic with all validations
        pass
    
    def get_game_status(self) -> GameStatus:
        """Get current game status"""
        # TODO: Return current status
        pass
    
    def get_board_state(self) -> List[List[str]]:
        """Get current board state"""
        # TODO: Return board state
        pass
    
    def get_current_player(self) -> Player:
        """Get the player whose turn it is"""
        # TODO: Return current player
        pass
    
    def get_moves_history(self) -> List[dict]:
        """Get history of all moves"""
        # TODO: Return copy of moves_history
        pass
    
    def reset_game(self):
        """Reset the game to initial state"""
        # TODO: Reset board, current_player, status, moves_history
        pass
    
    def get_game_id(self) -> str:
        """Get the unique game ID"""
        # TODO: Return game_id
        pass


class GameManager:
    """Manages multiple Tic-Tac-Toe games"""
    
    def __init__(self):
        """Initialize the game manager"""
        # TODO: Initialize games dictionary (game_id -> Game)
        pass
    
    def create_game(self, player1_id: str, player2_id: str) -> str:
        """
        Create a new game
        
        TODO:
        - Create Player instances for player1 (X) and player2 (O)
        - Create a new Game instance
        - Get game_id from game
        - Store game in games dictionary
        - Return game_id
        """
        # TODO: Implement game creation
        pass
    
    def get_game(self, game_id: str) -> Optional[Game]:
        """Get a game by ID"""
        # TODO: Return game from games dictionary, or None if not found
        pass
    
    def make_move(self, game_id: str, player_id: str, row: int, col: int) -> str:
        """
        Make a move in a specific game
        
        TODO:
        - Get game from games dictionary
        - If game not found, return 'GAME_NOT_FOUND'
        - Otherwise, call game.make_move() and return result
        """
        # TODO: Implement move delegation
        pass
    
    def delete_game(self, game_id: str) -> bool:
        """
        Delete a game
        
        TODO:
        - Remove game from games dictionary if it exists
        - Return True if deleted, False if not found
        """
        # TODO: Implement game deletion
        pass


# Example usage (commented out for practice)
# if __name__ == "__main__":
#     player1 = Player("player1", "X")
#     player2 = Player("player2", "O")
#     game = Game(player1, player2)
#     
#     print(f"Game ID: {game.get_game_id()}")
#     print(f"Status: {game.get_game_status().value}")
#     
#     result = game.make_move("player1", 0, 0)
#     print(f"Move result: {result}")

