from cell import Cell
from board import board

def make_grid(intial_x, initial_y, SIZE, board):

    grid = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:

                val = board[i][j]
            else:
                val = None

            grid[i][j] = Cell((intial_x + (SIZE * j)), (initial_y + (SIZE * i)), val)

    for a in range(9):
        for b in range(9):
            if grid[a][b].val is not None:
                grid[a][b].is_final = True 
            
    return grid

def get_bounds(pos):

    mod = pos % 3

    if(mod == 0):
        lower = pos
        upper = (pos + 2)

    elif(mod == 1):
        lower = (pos - 1)
        upper = (pos + 1)

    elif(mod == 2):
        lower = (pos - 2)
        upper = (pos)

    return lower, upper

def make_panel(x, y, SIZE):

    panel_list = []

    for i in range(9):
        panel_list.append(Cell((x + (SIZE * i)), (y), (i + 1)))

    return panel_list

def ValidPosition(grid, num, row, col):
    
    for cell in grid[row]:
        if cell == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False
        
    row_lower, row_upper = get_bounds(row)
    col_lower, col_upper = get_bounds(col)

    for i in range(row_lower, row_upper):
        for j in range(col_lower, col_upper):
            if grid[i][j] == num:
                return False
            
    return True

def SolveBoard(grid, row, col):

    if row == 8 and col == 9:
        return True
    
    if col == 9:
        col = 0
        row += 1

    if (grid[row][col] != 0):
        return SolveBoard(grid, row, col + 1)
    
    for i in range(1, 10):
        if ValidPosition(grid, i, row, col):
            grid[row][col] = i

            if SolveBoard(grid, row, col + 1):
                return True
            
        grid[row][col] = 0

    return False

def ValidPositionObject(grid, num, row, col):
    
    for cell in grid[row]:
        if cell.val == num:
            return False

    for i in range(9):
        if grid[i][col].val == num:
            return False
        
    row_lower, row_upper = get_bounds(row)
    col_lower, col_upper = get_bounds(col)

    for i in range(row_lower, row_upper):
        for j in range(col_lower, col_upper):
            if grid[i][j].val == num:
                return False
            
    return True
