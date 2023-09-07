from solve_this import UNSOLVED

def test_number(grid, x, y, number):
    for i in range(9):
        if(grid[x][i] == number or grid[i][y] == number):
            return False
    x = x - (x % 3)
    y = y - (y % 3)
    for i in range(3):
        for j in range(3):
            if(grid[x + i][y + j] == number):
                return False
    return True

def print_grid(grid):
    with open('Answer.txt', 'w') as f:
        f.write('')
        
    with open('Answer.txt', 'a') as f:
        for i in grid:
            for j in i:
                f.write(f'{j} ')
            f.write('\n')

def solver(grid, current_x, current_y):
    if(current_x == 9):
        return solver(grid, 0, current_y + 1)
    if(current_y == 9):
        print_grid(grid)
        return True
    if(grid[current_x][current_y] == 0):
        for i in range(9):
            if(test_number(grid, current_x, current_y, i+1)):
                grid[current_x][current_y] = i+1
                if(solver(grid, current_x+1, current_y)):
                    return True
                grid[current_x][current_y] = 0
        return False
    return solver(grid, current_x+1, current_y)

solver(UNSOLVED, 0, 0)