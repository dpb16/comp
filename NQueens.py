def IsSafe(board, row, col, N):
    # Check this row to the left
    for i in range(col):  # Only check left side in the current row
        if board[row][i] == 1:
            return False

    # Check this column
    for i in range(N):  # Check all rows in the current column
        if board[i][col] == 1:
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def SolveNQueen(board, col, N):
    if col >= N:  # Base case: all queens placed
        return True

    for i in range(N):
        if IsSafe(board, i, col, N):
            board[i][col] = 1  # Place queen

            if SolveNQueen(board, col + 1, N):
                return True

            board[i][col] = 0  # Backtrack

    return False

def main():
    N = 4
    board = []
    for i in range(N):
        row = [0] * N
        board.append(row)

    if not SolveNQueen(board, 0, N):
        print("No Solution Found")
    else:
        print("Solution:")
        for row in board:
            print(row)

# Example usage
main()
