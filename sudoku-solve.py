def is_valid_board(board, pos, num):
    # Returns if the attempted move is valid
    # Check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(board):
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if is_valid_board(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print(" - - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")
            if j == 8:
                print(board[i][j], "| ", end="\n")
            else:
                print(str(board[i][j]) + " ", end="")
    print(" - - - - - - - - - - - - - -")

sudoku =    [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

solve(sudoku)
print_board(sudoku)