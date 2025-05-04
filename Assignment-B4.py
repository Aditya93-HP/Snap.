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
