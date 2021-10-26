def DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth):
	prune = False
	rows = len(puzzle)
	cols = len(puzzle)

	for i in range (rows):
		print(puzzle[i])

	pieceRows = len(pieces[currentDepth])
	pieceCols = len(pieces[currentDepth][0])

	for i in range(rows):
		for j in range(cols):
			if puzzle[i][j] == -1:
				break

			# check if piece will cause out of bounds error
			# TODO
			if (i + pieceRows >= rows or j + pieceCols >= cols):
				break

			# Put the piece down if this is a valid spot
			# TODO
			for k in range(pieceRows):
				if (prune):
					break
				for l in range(pieceCols):
					if (puzzle[i+k][j+l] >= 1 and pieces[currentDepth][k][l] == 1):
						prune = True
						break
					elif (puzzle[i+k][j+l] == 0 and pieces[currentDepth][k][l] == 1):
						puzzle[i+k][j+l] = currentDepth + 1
						

			# Prune if able
			# prune = Pruning(puzzle)

			# Recursively call the DLS function for the new depth if we want to
			if (prune == False or currentDepth < maxDepth - 1):
				DepthLimitedSearch(puzzle, pieces, currentDepth + 1, maxDepth)
	return

# Helper function for the Depth Limited Search
def BubblePuzzleAI(puzzle, pieces):
	currentDepth = 0
	maxDepth = len(pieces)
	DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth)
	return

# initial puzzle board
# 0 means empty space, -1 means it's off the board
puzzle =[
    [ 0, 0, 0, 0 ],
    [ 0, 0, 0, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

# list of pieces
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

BubblePuzzleAI(puzzle, pieces)