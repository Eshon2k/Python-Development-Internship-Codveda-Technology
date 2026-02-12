def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1 # Place queen

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False

def print_board(board, n):
    for i in range(n):
        line = ""
        for j in range(n):
            line += " Q " if board[i][j] == 1 else " . "
        print(line)

# Main execution
if __name__ == "__main__":
    n = int(input("Enter the number of Queens (e.g., 4 or 8): "))
    # [span_1](start_span)Initialize board as a 2D array[span_1](end_span)
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
    else:
        print(f"\nSolution for {n}-Queens:")
        print_board(board, n)
