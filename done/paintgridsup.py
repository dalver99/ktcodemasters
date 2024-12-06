R, G, B = 'R', 'G', 'B'

# Check if adjacent blocks have the same color
def is_valid(board):
    for i in range(2):
        for j in range(5):
            if i > 0 and board[i][j] == board[i - 1][j]:  # Check above
                return False
            if j > 0 and board[i][j] == board[i][j - 1]:  # Check left
                return False
    return True

# Recursively generate all possible colorings
def generate(board, i, j):
    if j == 5:  # Move to the next row
        i += 1
        j = 0
    if i == 2:  # If we have filled all rows
        if is_valid(board):
            for row in board:
                print(' '.join(row))
            print()
        return

    for color in (R, G, B):
        if i == 0 and j == 0:  # Ensure (0,0) is always Red
            board[i][j] = R
            generate(board, i, j + 1)
        else:
            board[i][j] = color
            generate(board, i, j + 1)

# Initialize the board
board = [[None for _ in range(5)] for _ in range(2)]
board[0][0] = R  # Set the (0,0) cell to Red
generate(board, 0, 1)