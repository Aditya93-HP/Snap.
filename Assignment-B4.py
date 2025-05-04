def solve_n_queens(n):
    def backtrack(row, cols, pos_diag, neg_diag):
        if row == n: return True
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag: continue
            cols.add(col); pos_diag.add(row + col); neg_diag.add(row - col)
            board[row][col] = 'Q'
            if backtrack(row + 1, cols, pos_diag, neg_diag): return True
            board[row][col] = '.'; cols.remove(col); pos_diag.remove(row + col); neg_diag.remove(row - col)
        return False
    board = [['.'] * n for _ in range(n)]
    cols, pos_diag, neg_diag = set(), set(), set()
    return board if backtrack(0, cols, pos_diag, neg_diag) else None
def print_board(board):
    if board: 
        for row in board: print(" ".join(row))
    else: print("No solution exists.")
if __name__ == "__main__":
    print_board(solve_n_queens(int(input("Enter number of queens: "))))

'''INPUT
Enter number of queens: 4
'''
'''OUTPUT
. Q . .
. . . Q
Q . . .
. . Q .
'''
'''
### **1. `solve_n_queens(n):`**

* This is the main function that solves the N-Queens problem. The argument `n` represents the number of queens (and the size of the chessboard).
* It calls a helper function `backtrack()` to try placing queens on the board using a backtracking approach.

### **2. `def backtrack(row, cols, pos_diag, neg_diag):`**

* This is a helper function that uses backtracking to place queens on the chessboard.
* **Arguments:**

  * `row`: The current row being considered for placing a queen.
  * `cols`: A set that tracks the columns where queens are already placed.
  * `pos_diag`: A set that tracks the positive diagonals (from top-left to bottom-right).
  * `neg_diag`: A set that tracks the negative diagonals (from top-right to bottom-left).

### **3. `if row == n: return True`**

* This line checks if all queens have been placed (i.e., the current row equals `n`).
* If true, it means the solution is found, so it returns `True` to indicate success.

### **4. `for col in range(n):`**

* This is a loop that iterates over all the columns in the current row (`row`).
* The function tries placing a queen in each column of the current row and checks if it is safe.

### **5. `if col in cols or (row + col) in pos_diag or (row - col) in neg_diag: continue`**

* This line checks if the current column, positive diagonal, or negative diagonal is already occupied by another queen.
* `cols`: Tracks columns where queens are placed.
* `(row + col)`: The formula for the positive diagonal (top-left to bottom-right).
* `(row - col)`: The formula for the negative diagonal (top-right to bottom-left).
* If any of these conditions are true, it means placing a queen at the current position would result in a conflict, so the loop continues to the next column.

### **6. `cols.add(col); pos_diag.add(row + col); neg_diag.add(row - col)`**

* If the current column and diagonals are free, it adds the current column and diagonal positions to the respective sets.
* These sets will track where queens have been placed, helping to avoid conflicts.

### **7. `board[row][col] = 'Q'`**

* This places a queen (`'Q'`) on the current position on the board.

### **8. `if backtrack(row + 1, cols, pos_diag, neg_diag): return True`**

* This recursively calls `backtrack()` to attempt placing a queen on the next row.
* If placing queens on subsequent rows leads to a solution (i.e., the function returns `True`), then this current placement is correct, and the function returns `True`.

### **9. `board[row][col] = '.'; cols.remove(col); pos_diag.remove(row + col); neg_diag.remove(row - col)`**

* If placing a queen on the current position doesn't lead to a solution (i.e., the recursive call fails), it backtracks:

  * The queen is removed from the board (set the position to `'.'`).
  * The current column and diagonal positions are removed from their respective sets.

### **10. `return False`**

* If no safe position was found for the queen in the current row, it returns `False` to backtrack further.

### **11. `board = [['.'] * n for _ in range(n)]`**

* This initializes an empty chessboard of size `n x n` with all cells set to `'.'` (indicating no queens are placed).

### **12. `cols, pos_diag, neg_diag = set(), set(), set()`**

* These are sets used to track columns and diagonals that are blocked due to previously placed queens.

### **13. `return board if backtrack(0, cols, pos_diag, neg_diag) else None`**

* This calls the `backtrack()` function starting from row 0.
* If `backtrack()` returns `True` (indicating a solution was found), it returns the filled board.
* If no solution is found, it returns `None`.

### **14. `def print_board(board):`**

* This is a helper function to print the chessboard.
* It prints the board in a readable format where `Q` represents queens, and `.` represents empty cells.

### **15. `if board:`**

* This checks if a valid board was returned (i.e., the solution exists).
* If a solution exists, it proceeds to print the board.

### **16. `for row in board: print(" ".join(row))`**

* This loops through each row of the board and prints the elements of the row, joined by a space.

### **17. `else: print("No solution exists.")`**

* If the board is `None` (i.e., no solution), it prints a message indicating that no solution exists.

### **18. `if __name__ == "__main__":`**

* This checks if the script is being run directly (not imported).
* If true, it proceeds to execute the following lines.

### **19. `print_board(solve_n_queens(int(input("Enter number of queens: "))))`**

* This asks the user to input the number of queens (`n`).
* It then calls `solve_n_queens(n)` to solve the problem and prints the result using `print_board()`.

### **Summary of Logic:**

The code uses a backtracking algorithm to find a solution to the N-Queens problem. It attempts to place queens row by row, checking if placing a queen in a particular column is safe (i.e., it does not conflict with any previously placed queens in terms of columns or diagonals). If a solution is found, it returns the board; otherwise, it returns `None`.
'''