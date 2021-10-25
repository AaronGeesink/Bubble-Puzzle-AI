puzzle =[
    [ 0, 0, 0, 0 ],
    [ 0, 0, 0, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

p1 = [[ 1, 1 ],
      [ 1, 0 ],
      [ 1, 0 ],  
      [ 1, 0 ]    
]
p2 = [[ 0, 1, 1 ],
      [ 1, 1, 0 ],
      [ 1, 0, 0 ]   
]

pieces = [p1, p2]

def Pruning(puzzle):
    for i in range(len(puzzle):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] = 0:        # one empty space
                if (puzzle[i-1][j-1] = 1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = 1) # most common case with no -1
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = -1 and puzzle[i-1][j+1] = -1 and puzzle[i][j-1] = -1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = -1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = 1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = -1 and puzzle[i-1][j+1] = -1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = 1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = -1 and puzzle[i-1][j+1] = -1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = -1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = -1 and puzzle[i-1][j+1] = -1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = -1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = -1 and puzzle[i+1][j+1] = -1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = -1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = -1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = 1)
                or (puzzle[i-1][j-1] = 1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = -1)
                or (puzzle[i-1][j-1] = 1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = 1 and puzzle[i][j+1] = -1 and puzzle[i+1][j-1] = 1 and puzzle[i+1][j] = -1 and puzzle[i+1][j+1] = -1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = -1 and puzzle[i][j+1] = 1 and puzzle[i+1][j-1] = -1 and puzzle[i+1][j] = 1 and puzzle[i+1][j+1] = -1)
                or (puzzle[i-1][j-1] = -1 and puzzle[i-1][j] = 1 and puzzle[i-1][j+1] = 1 and puzzle[i][j-1] = -1 and puzzle[i][j+1] = -1 and puzzle[i+1][j-1] = -1 and puzzle[i+1][j] = -1 and puzzle[i+1][j+1] = -1):
                    puzzle =[
                        [ 0, 0, 0, 0 ],
                        [ 0, 0, 0, -1 ],
                        [ 0, 0, -1, -1 ],
                        [ 0, -1, -1, -1 ]
                    ]
            if (puzzle[i][j] = 0 and puzzle[i][j+1] = 0)     # two empty spaces next to each other
            or (puzzle[i][j] = 0 and puzzle[i+1][j] = 0)     # two empty spaces one below the other
            or (puzzle[i][j] = 0 and puzzle[i+1][j-1] = 0)   # two empty spaces diagonal below to the left
            or (puzzle[i][j] = 0 and puzzle[i+1][j+1] = 0):   # two empty spaces diagonal below to the right
                if (puzzle[][])
                    puzzle =[
                            [ 0, 0, 0, 0 ],
                            [ 0, 0, 0, -1 ],
                            [ 0, 0, -1, -1 ],
                            [ 0, -1, -1, -1 ]
                        ]

