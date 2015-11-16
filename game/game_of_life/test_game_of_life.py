import game_of_life

def test_isalive():
    grid = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,1]]

    life = game_of_life.isalive(grid,1,1)
    assert life == False
    life = game_of_life.isalive(grid,3,3)
    assert life == True

    
