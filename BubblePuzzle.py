import copy

def DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth, solved):
	prune = False
	rows = len(puzzle)
	cols = len(puzzle)

	pieceRows = len(pieces[currentDepth])
	pieceCols = len(pieces[currentDepth][0])

	for i in range(rows):
		# Check if piece will go out of bounds of the puzzle rows
		if (i + pieceRows > rows):
			break
		for j in range(cols):
			if solved[0]:
				break
			if puzzle[i][j] == -1:
				break

			# Check if piece will go out of bounds of the puzzle cols
			if (j + pieceCols > cols):
				break

			# Put the piece down if this is a valid spot
			tempPuzzle = copy.deepcopy(puzzle)
			prune = False
			for k in range(pieceRows):
				if (prune):
					break
				for l in range(pieceCols):
					if ((tempPuzzle[i+k][j+l] >= 1 or tempPuzzle[i+k][j+l] == -1) and pieces[currentDepth][k][l] == 1):
						prune = True
						break
					elif (pieces[currentDepth][k][l] == 1):
						tempPuzzle[i+k][j+l] = currentDepth + 1
			
			# Consider the puzzle if we were able to insert a piece
			if (prune == False):
				puzzle = copy.deepcopy(tempPuzzle)

			for k in range (rows):
				print(puzzle[k])
			print("\n")

			# TODO: Prune if able
			# prune = Pruning(puzzle)

			# Recursively call the DLS function for the new depth if we want to
			if (prune == False and currentDepth < maxDepth - 1):
				solved[0] = DepthLimitedSearch(puzzle, pieces, currentDepth + 1, maxDepth, solved)
			elif (prune == False and currentDepth == maxDepth - 1):
				return True
	return solved[0]

# Helper function for the Depth Limited Search
def BubblePuzzleAI(puzzle, pieces):
	currentDepth = 0
	maxDepth = len(pieces)
	solved = [False]
	DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth, solved)
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