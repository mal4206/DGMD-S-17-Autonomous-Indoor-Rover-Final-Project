'''
 Listing of different grid map configurations
 for testing shortest path algorithm
'''

EMPTY_GRID =   [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]


BOXED_IN_GRID =    [[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]]


OCCUPIED_GRID1 =   [[1,0,1,0,0],
                    [1,0,0,0,0],
                    [1,0,1,0,0],
                    [0,0,1,0,1],
                    [0,1,0,0,1]]


DIAGONAL_OCCUPIED_GRID =   [[1,0,0,0,0],
                            [0,1,0,0,0],
                            [0,0,0,0,0],
                            [0,0,0,1,0],
                            [0,0,0,0,1]]