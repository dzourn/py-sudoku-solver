import numpy as np

#valid
matrix = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],
    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,0,0,0,5]
]

#invalid
iboard = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],
    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,6,0,0,5]
]

def set_num(board, row, col, num):

    #check if number is in same row
    for i in range(9):
        if board[row][i] == num:
            return False

    #check if number is in same column
    for i in range(9):
        if board[i][col] == num:
            return False

    #check if number is in box
    first_row = row - row%3
    first_col = col - col%3

    for i in range(3):
        for y in range(3):
            if board[i + first_row][y + first_col] == num:
                return False

    return True

def solve(board, row, col):
    
    #check if we reached the max of our board 
    if row == 8 and col == 9:
        return True

    #go to next row/reset column index
    if col == 9:
        row = row + 1
        col = 0

    #check if we alreade have a number
    if board[row][col] > 0:
        return solve(board, row, col + 1)

    #place number
    for num in range(1,10):
        if set_num(board, row, col, num):
            board[row][col] = num
            #recursion  
            if  solve(board, row, col + 1):
                return True
        #wrong number
        board[row][col] = 0

    #everything failed/impossible
    return False

def main(board):
    if solve(board, 0, 0):
        print(np.array(board))
    else:
        print('No solution')

if __name__ == '__main__':
    main(matrix) 
    main(iboard)
