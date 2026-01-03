/**
 * Design Tic-Tac-Toe Game - C++ Implementation (Reference)
 * 
 * Key differences from Python:
 * 1. Explicit memory management (no garbage collection)
 * 2. Strong typing with explicit type declarations
 * 3. Public/private/protected access modifiers
 * 4. Header files for declarations
 * 5. Pointers and references
 * 6. STL containers (vector, map, etc.)
 * 7. No default parameters in same way
 * 8. Manual string handling (std::string)
 * 9. Enum class for type safety
 */

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <uuid/uuid.h>
#include <sstream>
#include <iomanip>
#include <random>

using namespace std;

enum class GameStatus {
    IN_PROGRESS,
    X_WON,
    O_WON,
    DRAW,
    FINISHED
};

string gameStatusToString(GameStatus status) {
    switch(status) {
        case GameStatus::IN_PROGRESS: return "IN_PROGRESS";
        case GameStatus::X_WON: return "X_WON";
        case GameStatus::O_WON: return "O_WON";
        case GameStatus::DRAW: return "DRAW";
        case GameStatus::FINISHED: return "FINISHED";
        default: return "UNKNOWN";
    }
}

class Player {
private:
    string playerId;
    char symbol;

public:
    Player(const string& playerId, char symbol) {
        if (symbol != 'X' && symbol != 'O') {
            throw invalid_argument("Symbol must be 'X' or 'O'");
        }
        this->playerId = playerId;
        this->symbol = symbol;
    }
    
    string getPlayerId() const {
        return playerId;
    }
    
    char getSymbol() const {
        return symbol;
    }
    
    string toString() const {
        return "Player(id=" + playerId + ", symbol=" + symbol + ")";
    }
};

class Board {
private:
    int size;
    vector<vector<char>> board;
    vector<int> rowCounts;
    vector<int> colCounts;
    int diagCount;
    int antiDiagCount;

public:
    Board() : Board(3) {}
    
    Board(int size) : size(size), 
                     board(size, vector<char>(size, '\0')),
                     rowCounts(size, 0),
                     colCounts(size, 0),
                     diagCount(0),
                     antiDiagCount(0) {}
    
    bool makeMove(int row, int col, char symbol) {
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
    
    bool isValidMove(int row, int col) const {
        if (row < 0 || row >= size || col < 0 || col >= size) {
            return false;
        }
        return board[row][col] == '\0';
    }
    
    vector<vector<char>> getBoardState() const {
        return board; // Returns copy
    }
    
    char checkWinner() const {
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
        
        return '\0'; // No winner
    }
    
    bool isFull() const {
        for (const auto& row : board) {
            for (char cell : row) {
                if (cell == '\0') {
                    return false;
                }
            }
        }
        return true;
    }
    
    void reset() {
        board = vector<vector<char>>(size, vector<char>(size, '\0'));
        rowCounts = vector<int>(size, 0);
        colCounts = vector<int>(size, 0);
        diagCount = 0;
        antiDiagCount = 0;
    }
};

struct Move {
    string playerId;
    char symbol;
    int row;
    int col;
};

class Game {
private:
    string gameId;
    Board board;
    Player* player1;
    Player* player2;
    Player* currentPlayer;
    GameStatus status;
    vector<Move> movesHistory;
    
    string generateUUID() {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(0, 15);
        
        stringstream ss;
        ss << hex;
        for (int i = 0; i < 8; i++) {
            ss << dis(gen);
        }
        ss << "-";
        for (int i = 0; i < 4; i++) {
            ss << dis(gen);
        }
        ss << "-";
        for (int i = 0; i < 4; i++) {
            ss << dis(gen);
        }
        ss << "-";
        for (int i = 0; i < 4; i++) {
            ss << dis(gen);
        }
        ss << "-";
        for (int i = 0; i < 12; i++) {
            ss << dis(gen);
        }
        return ss.str();
    }

public:
    Game(Player* p1, Player* p2) {
        if (p1->getSymbol() == p2->getSymbol()) {
            throw invalid_argument("Players must have different symbols");
        }
        
        this->gameId = generateUUID();
        this->board = Board();
        this->player1 = p1;
        this->player2 = p2;
        this->currentPlayer = p1;
        this->status = GameStatus::IN_PROGRESS;
    }
    
    ~Game() {
        // Clean up if using dynamic allocation
        // delete player1;
        // delete player2;
    }
    
    string makeMove(const string& playerId, int row, int col) {
        // Check if game is over
        if (status != GameStatus::IN_PROGRESS) {
            return "GAME_OVER";
        }
        
        // Validate player
        if (playerId != player1->getPlayerId() && playerId != player2->getPlayerId()) {
            return "INVALID_PLAYER";
        }
        
        // Check if it's player's turn
        if (playerId != currentPlayer->getPlayerId()) {
            return "NOT_YOUR_TURN";
        }
        
        // Validate move
        if (!board.isValidMove(row, col)) {
            return "INVALID_MOVE";
        }
        
        // Make the move
        char symbol = currentPlayer->getSymbol();
        board.makeMove(row, col, symbol);
        
        // Record move
        Move move;
        move.playerId = playerId;
        move.symbol = symbol;
        move.row = row;
        move.col = col;
        movesHistory.push_back(move);
        
        // Check for winner
        char winner = board.checkWinner();
        if (winner == 'X') {
            status = GameStatus::X_WON;
            return "SUCCESS";
        } else if (winner == 'O') {
            status = GameStatus::O_WON;
            return "SUCCESS";
        }
        
        // Check for draw
        if (board.isFull()) {
            status = GameStatus::DRAW;
            return "SUCCESS";
        }
        
        // Switch turns
        currentPlayer = (currentPlayer == player1) ? player2 : player1;
        
        return "SUCCESS";
    }
    
    GameStatus getGameStatus() const {
        return status;
    }
    
    vector<vector<char>> getBoardState() const {
        return board.getBoardState();
    }
    
    Player* getCurrentPlayer() const {
        return currentPlayer;
    }
    
    vector<Move> getMovesHistory() const {
        return movesHistory;
    }
    
    void resetGame() {
        board.reset();
        currentPlayer = player1;
        status = GameStatus::IN_PROGRESS;
        movesHistory.clear();
    }
    
    string getGameId() const {
        return gameId;
    }
};

class GameManager {
private:
    map<string, Game*> games;

public:
    ~GameManager() {
        // Clean up games
        for (auto& pair : games) {
            delete pair.second;
        }
    }
    
    string createGame(const string& player1Id, const string& player2Id) {
        Player* player1 = new Player(player1Id, 'X');
        Player* player2 = new Player(player2Id, 'O');
        Game* game = new Game(player1, player2);
        string gameId = game->getGameId();
        games[gameId] = game;
        return gameId;
    }
    
    Game* getGame(const string& gameId) {
        auto it = games.find(gameId);
        return (it != games.end()) ? it->second : nullptr;
    }
    
    string makeMove(const string& gameId, const string& playerId, int row, int col) {
        auto it = games.find(gameId);
        if (it == games.end()) {
            return "GAME_NOT_FOUND";
        }
        return it->second->makeMove(playerId, row, col);
    }
    
    bool deleteGame(const string& gameId) {
        auto it = games.find(gameId);
        if (it != games.end()) {
            delete it->second;
            games.erase(it);
            return true;
        }
        return false;
    }
};

// Example usage
int main() {
    cout << "==================================================" << endl;
    cout << "Tic-Tac-Toe Game Design - C++ Example" << endl;
    cout << "==================================================" << endl;
    
    // Example 1: Single game
    cout << "\n--- Example 1: Single Game ---" << endl;
    Player player1("player1", 'X');
    Player player2("player2", 'O');
    Game game(&player1, &player2);
    
    cout << "Game ID: " << game.getGameId() << endl;
    cout << "Initial Status: " << gameStatusToString(game.getGameStatus()) << endl;
    
    // Make moves
    string result1 = game.makeMove("player1", 0, 0);
    cout << "Move by player1 at (0, 0): " << result1 << endl;
    cout << "Status: " << gameStatusToString(game.getGameStatus()) << endl;
    
    string result2 = game.makeMove("player2", 1, 1);
    cout << "Move by player2 at (1, 1): " << result2 << endl;
    cout << "Status: " << gameStatusToString(game.getGameStatus()) << endl;
    
    return 0;
}

