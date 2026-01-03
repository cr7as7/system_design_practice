/**
 * Design Tic-Tac-Toe Game - Skeleton Code for Practice
 * 
 * Fill in the TODO sections to complete the implementation.
 * This is the structure you should implement in an interview.
 */

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <random>

using namespace std;

enum class GameStatus {
    // TODO: Define enum values: IN_PROGRESS, X_WON, O_WON, DRAW, FINISHED
};

string gameStatusToString(GameStatus status) {
    // TODO: Implement switch statement to convert GameStatus to string
    // TODO: Return "IN_PROGRESS", "X_WON", "O_WON", "DRAW", "FINISHED"
    return "";
}

class Player {
private:
    // TODO: Add private fields: playerId (string), symbol (char)

public:
    Player(const string& playerId, char symbol) {
        // TODO: Validate symbol is 'X' or 'O', throw invalid_argument if not
        // TODO: Initialize playerId and symbol
    }
    
    string getPlayerId() const {
        // TODO: Return playerId
        return "";
    }
    
    char getSymbol() const {
        // TODO: Return symbol
        return '\0';
    }
    
    string toString() const {
        // TODO: Return string like "Player(id=player1, symbol=X)"
        return "";
    }
};

class Board {
private:
    // TODO: Add private fields:
    //   - size (int)
    //   - board (vector<vector<char>>)
    //   - rowCounts (vector<int>)
    //   - colCounts (vector<int>)
    //   - diagCount (int)
    //   - antiDiagCount (int)

public:
    Board() : Board(3) {}
    
    Board(int size) {
        // TODO: Initialize size
        // TODO: Initialize board as vector<vector<char>>(size, vector<char>(size, '\0'))
        // TODO: Initialize rowCounts and colCounts as vector<int>(size, 0)
        // TODO: Initialize diagCount and antiDiagCount to 0
    }
    
    bool makeMove(int row, int col, char symbol) {
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
    
    bool isValidMove(int row, int col) const {
        // TODO: Check bounds: row >= 0 && row < size && col >= 0 && col < size
        // TODO: Check if board[row][col] == '\0' (empty)
        // TODO: Return true if valid, false otherwise
        return false;
    }
    
    vector<vector<char>> getBoardState() const {
        // TODO: Return board (returns copy by value)
        return vector<vector<char>>();
    }
    
    char checkWinner() const {
        // TODO: Check rowCounts: if any count == size return 'X', if == -size return 'O'
        // TODO: Check colCounts: if any count == size return 'X', if == -size return 'O'
        // TODO: Check diagCount: if == size return 'X', if == -size return 'O'
        // TODO: Check antiDiagCount: if == size return 'X', if == -size return 'O'
        // TODO: Return '\0' if no winner
        return '\0';
    }
    
    bool isFull() const {
        // TODO: Check if all cells in board are non-empty (not '\0')
        // TODO: Return true if full, false otherwise
        return false;
    }
    
    void reset() {
        // TODO: Reset board to vector<vector<char>>(size, vector<char>(size, '\0'))
        // TODO: Reset rowCounts and colCounts to vector<int>(size, 0)
        // TODO: Reset diagCount and antiDiagCount to 0
    }
};

struct Move {
    // TODO: Add fields: playerId (string), symbol (char), row (int), col (int)
};

class Game {
private:
    // TODO: Add private fields:
    //   - gameId (string)
    //   - board (Board)
    //   - player1, player2 (Player*)
    //   - currentPlayer (Player*)
    //   - status (GameStatus)
    //   - movesHistory (vector<Move>)
    
    string generateUUID() {
        // TODO: Generate UUID string (can use random number generation)
        // TODO: Format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        return "";
    }

public:
    Game(Player* p1, Player* p2) {
        // TODO: Validate players have different symbols, throw exception if same
        // TODO: Generate gameId using generateUUID()
        // TODO: Create new Board()
        // TODO: Initialize player1, player2, currentPlayer = p1
        // TODO: Set status = GameStatus::IN_PROGRESS
    }
    
    ~Game() {
        // TODO: Clean up if using dynamic allocation (optional)
    }
    
    string makeMove(const string& playerId, int row, int col) {
        // TODO: Check if status != IN_PROGRESS → return "GAME_OVER"
        // TODO: Validate playerId → return "INVALID_PLAYER" if not valid
        // TODO: Check if it's player's turn → return "NOT_YOUR_TURN" if not
        // TODO: Validate move → return "INVALID_MOVE" if not valid
        // TODO: Make the move using board.makeMove()
        // TODO: Record move in movesHistory (create Move struct)
        // TODO: Check for winner → update status and return "SUCCESS" if winner
        // TODO: Check if board is full → update status to DRAW and return "SUCCESS"
        // TODO: Switch currentPlayer and return "SUCCESS"
        return "";
    }
    
    GameStatus getGameStatus() const {
        // TODO: Return status
        return GameStatus::IN_PROGRESS;
    }
    
    vector<vector<char>> getBoardState() const {
        // TODO: Return board.getBoardState()
        return vector<vector<char>>();
    }
    
    Player* getCurrentPlayer() const {
        // TODO: Return currentPlayer
        return nullptr;
    }
    
    vector<Move> getMovesHistory() const {
        // TODO: Return movesHistory
        return vector<Move>();
    }
    
    void resetGame() {
        // TODO: Call board.reset()
        // TODO: Set currentPlayer = player1
        // TODO: Set status = GameStatus::IN_PROGRESS
        // TODO: Clear movesHistory
    }
    
    string getGameId() const {
        // TODO: Return gameId
        return "";
    }
};

class GameManager {
private:
    // TODO: Add private field: games (map<string, Game*>)

public:
    ~GameManager() {
        // TODO: Clean up all games (delete each Game*)
    }
    
    string createGame(const string& player1Id, const string& player2Id) {
        // TODO: Create Player instances using new (player1 with 'X', player2 with 'O')
        // TODO: Create new Game using new
        // TODO: Get gameId from game
        // TODO: Store game in games map
        // TODO: Return gameId
        return "";
    }
    
    Game* getGame(const string& gameId) {
        // TODO: Find game in games map
        // TODO: Return game if found, nullptr if not found
        return nullptr;
    }
    
    string makeMove(const string& gameId, const string& playerId, int row, int col) {
        // TODO: Get game from games map
        // TODO: If nullptr, return "GAME_NOT_FOUND"
        // TODO: Otherwise, return game->makeMove(playerId, row, col)
        return "";
    }
    
    bool deleteGame(const string& gameId) {
        // TODO: Find game in games map
        // TODO: If found: delete game, erase from map, return true
        // TODO: Otherwise return false
        return false;
    }
};

// Example usage (commented out for practice)
// int main() {
//     Player player1("player1", 'X');
//     Player player2("player2", 'O');
//     Game game(&player1, &player2);
//     
//     cout << "Game ID: " << game.getGameId() << endl;
//     cout << "Status: " << gameStatusToString(game.getGameStatus()) << endl;
//     
//     string result = game.makeMove("player1", 0, 0);
//     cout << "Move result: " << result << endl;
//     
//     return 0;
// }

