

def isalive(grid,x,y):
    return grid[x][y] == 1


def kill(grid,x,y):
    grid[x][y] = 0 
    return grid 


def live(grid,x,y):
    grid[x][y] = 1
    return grid


def generate_grid():
        grid = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,1]]

        return grid



def count_neighbour(grid,x,y):
    count = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == dy == 0: #same index
                continue
            elif dx+x < 0 or dy+y < 0:
                continue
            else:
                try:
                    
                    if grid[(x+dx)][(y+dy)] == 1 : 
                        count = count + 1
                except IndexError :
                    continue
    return count


# grid = [[1,0,0],
#             [1,0,0],
#             [0,0,1]]
 

# print count_neighbour(grid,0,0)
