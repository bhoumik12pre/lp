# Function to check if it is safe to place a queen at position (row, col)
def is_safe(board, row, col, n):
    # Check this column on the upper side (previous rows)
    for i in range(row):
        # Check if there's a queen in the same column, same diagonal, or same anti-diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False  # If any condition matches, it's not safe to place the queen
    return True  # It is safe to place the queen

# Backtracking function to find all possible solutions
def solve_n_queens_util(board, row, n, solutions):
    # Base case: If all queens are placed, add the solution to the list
    if row == n:
        solutions.append(board[:])  # Add a copy of the current board to the solutions
        return

    # Try to place a queen in every column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):  # If it's safe to place a queen
            board[row] = col  # Place queen at (row, col)
            solve_n_queens_util(board, row + 1, n, solutions)  # Recur to place the next queen in the next row
            board[row] = -1  # Backtrack: Remove the queen and try the next column

# Main function to solve the N-Queens problem
def solve_n_queens(n):
    board = [-1] * n  # Initialize the board with -1 (indicating no queens are placed yet)
    solutions = []  # List to store all possible solutions

    solve_n_queens_util(board, 0, n, solutions)  # Start placing queens from the first row

    return solutions  # Return all found solutions

# Function to print all the solutions in a readable format
def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            # For each row, print a 'Q' in the column where the queen is placed and '.' elsewhere
            print(' '.join(['Q' if i == row else '.' for i in range(len(solution))]))
        print("\n")  # Print a blank line between different solutions

# Input for the N-Queens problem
n = int(input("Enter the value of N: "))  # Ask the user for the size of the board
solutions = solve_n_queens(n)  # Solve the N-Queens problem

# Output the total number of solutions and print each solution
print(f"Total solutions for {n}-Queens problem: {len(solutions)}")  # Print the number of solutions
print_solutions(solutions)  # Print all the solutions
