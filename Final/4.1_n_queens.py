# Function to check if it's safe to place a queen at position (x, y) on the chessboard
def issafe(arr, x, y, n):
    # Checking the column for attacks
    for row in range(x):
        if arr[row][y] == 1:  # If there's a queen in the same column
            return False  # It's not safe to place a queen here

    # Checking the diagonal attack (upper left diagonal)
    row = x
    col = y
    while row >= 0 and col >= 0:  # Traverse diagonally up-left
        if arr[row][col] == 1:  # If there's a queen on the diagonal
            return False  # It's not safe to place a queen here
        row -= 1
        col -= 1

    # Checking the anti-diagonal attack (upper right diagonal)
    row = x
    col = y
    while row >= 0 and col < n:  # Traverse diagonally up-right
        if arr[row][col] == 1:  # If there's a queen on the anti-diagonal
            return False  # It's not safe to place a queen here
        row -= 1
        col += 1

    return True  # If no attacks, it is safe to place the queen

# Function to solve the N-Queens problem using backtracking
def nQueen(arr, x, n):
    if x >= n:  # Base case: If all queens are placed
        return True

    # Try placing a queen in all columns of row x
    for col in range(n):
        if issafe(arr, x, col, n):  # If it's safe to place a queen at (x, col)
            arr[x][col] = 1  # Place the queen
            if nQueen(arr, x + 1, n):  # Recursively place queens in the next row
                return True
            arr[x][col] = 0  # Backtrack: If placing queen here doesn't lead to a solution, remove it

    return False  # If no safe position found, return False

# Main function to take user input and print the solution
def main():
    n = int(input("Enter number of Queens : "))  # Input: number of queens
    arr = [[0] * n for i in range(n)]  # Create an empty n x n chessboard (0 means empty, 1 means queen)

    # Call the nQueen function to solve the problem
    if nQueen(arr, 0, n):  # Start from row 0
        # If a solution is found, print the chessboard
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")  # Print each cell (0 or 1)
            print()  # Print new line after each row

# Entry point of the program
if __name__ == '__main__':
    main()
