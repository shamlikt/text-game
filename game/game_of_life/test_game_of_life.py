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




def test_count_neighbour():
    
    grid = [[1,0,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,1]]
    count1 =  game_of_life.count_neighbour(grid,0,0)
    count2 =  game_of_life.count_neighbour(grid,0,1)
    count3 =  game_of_life.count_neighbour(grid,0,2)
    count4 =  game_of_life.count_neighbour(grid,0,3)
    count5 =  game_of_life.count_neighbour(grid,1,0)
    count6 =  game_of_life.count_neighbour(grid,1,1)
    count7 =  game_of_life.count_neighbour(grid,1,2)
    count8 =  game_of_life.count_neighbour(grid,1,3)
    count9 =  game_of_life.count_neighbour(grid,2,0)
    count10 =  game_of_life.count_neighbour(grid,2,1)
    count11 =  game_of_life.count_neighbour(grid,2,2)
    count12 =  game_of_life.count_neighbour(grid,2,3)
    count13 =  game_of_life.count_neighbour(grid,3,0)
    count14 =  game_of_life.count_neighbour(grid,3,1)
    count15 =  game_of_life.count_neighbour(grid,3,2)
    count16 =  game_of_life.count_neighbour(grid,3,3)
    
    assert count1  == 1
    assert count2  == 2
    assert count3  == 1
    assert count4  == 0
    assert count5  == 3
    assert count6  == 2
    assert count7  == 2
    assert count8  == 0
    assert count9  == 2
    assert count10 == 1
    assert count11 == 3
    assert count12 == 1
    assert count13 == 1
    assert count14 == 1
    assert count15 == 2
    assert count16 == 0


def test_next_generation():
    
    grid =[[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
 
    grid1 = [[0,0,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,1,0]]
             

    new_life = game_of_life.next_generation(grid)
    new_life1 = game_of_life.next_generation(grid1)
    
    assert new_life == [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
    assert new_life1 == [[0,0,0,0],[0,1,1,1],[0,1,1,1],[0,0,0,0]]
    




    
    


    



    


    


    


    


    





    

