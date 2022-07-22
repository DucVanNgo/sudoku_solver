import numpy as np

input_grid = [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def check(x,y,n):
    """Checking for row (x) and column (y), if value 'n' is a possible. If it
    is, function returns 'True', else 'False'"""
    for i in range(9):
        if input_grid[x][i] == n:
            return False

    for i in range(9):
        if input_grid[i][y] == n:
            return False

    for i in range(3):
        for j in range(3):
            if input_grid[(x//3)*3+i][(y//3)*3+j] == n:
                return False

    return True


def solver(sudoku = input_grid):
    """Function solving the input sudoku recursively using backtracking. If there are multiple solutions,
    all solutions will be shown with a line break in between them."""

    for i in range(9):

        for j in range(9):

            if sudoku[i][j] == 0:

                for k in range(1,10):

                    if check(i,j,k):

                        sudoku[i][j] = k
                        # Recursion: Continue to solve sudoku with k as input in field input_grid[i][j]
                        solver()
                        #If solver function doesn't find a solution, it should place a 0 in the field [i][j] again, so that a different number can be tried
                        sudoku[i][j] = 0
                return
    print(np.matrix(sudoku), "\n")

if __name__ == '__main__':
    solver()
