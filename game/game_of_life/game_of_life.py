def isalive(grid,x,y):
    return grid[x][y] == 1


def live(grid,x,y):
    grid[x][y] = 1
    return grid


def generate_grid():
    grid = [[0,0,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,1,0]]
    return grid

def desplay(grid):
    for i in grid:
        for j in i:
            print grid[i][j]

def count_neighbour(grid,x,y):
    count = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == dy == 0: #same index
                continue
            elif dx+x < 0 or dy+y < 0: # avoid negative index
                continue
            else:
                try:
                    if grid[(x+dx)][(y+dy)] == 1 : 
                        count = count + 1
                except IndexError :
                    continue
    return count


def next_generation(grid):
    next_gen = [[0 for x in range(4)] for y in range(4)]
    for x in range(len(grid)):
        for  y in range(len(grid[x])):
                
                if count_neighbour(grid,x,y) in [2,3] and isalive(grid,x,y):
                   next_gen = live(next_gen,x,y)
                elif not isalive(grid,x,y)  and count_neighbour(grid,x,y) == 3:
                  next_gen = live(next_gen,x,y)

    return next_gen

    
    
