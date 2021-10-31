import copy
import time

# Depth Limited Search for the puzzle
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
			#if solved[0]:
			#	break
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
					if ((puzzle[i+k][j+l] >= 1 or puzzle[i+k][j+l] == -1) and pieces[currentDepth][k][l] == 1):
						prune = True
						break
					elif (pieces[currentDepth][k][l] == 1):
						puzzle[i+k][j+l] = currentDepth + 1
			
			# Reset the puzzle board if the piece won't fit at the current spot
			if (prune == True):
				puzzle = copy.deepcopy(tempPuzzle)
			# prune if there is an island
			else:
				prune = Pruning(puzzle)
				if (prune == True):
					puzzle = copy.deepcopy(tempPuzzle)

			# Recursively call the DLS function for the new depth if we want to
			if (prune == False and currentDepth < maxDepth - 1):
				solved[0] = DepthLimitedSearch(puzzle, pieces, currentDepth + 1, maxDepth, solved)
				#if (solved[0] == False):
				puzzle = copy.deepcopy(tempPuzzle)
			elif (prune == False and currentDepth == maxDepth - 1):
				for k in range (rows):
					print(puzzle[k])
				print("\n")
				return True
	return solved[0]

# Helper function for the Depth Limited Search
def BubblePuzzleAI(puzzle, pieces):
	currentDepth = 0
	maxDepth = len(pieces)
	solved = [False]
	DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth, solved)
	return

# Pruning function
# returns True if puzzle should be pruned
def Pruning(puzzle):
	for i in range(len(puzzle)):
		for j in range(len(puzzle[i])):
			'''
			if (puzzle[i][j] == 0) and (i == 0 and j == 0):
				if (((puzzle[i][j+1] == -1) or (puzzle[i][j+1] >= 1))
				and ((puzzle[i+1][j] == -1) or (puzzle[i+1][j] >= 1))):
					return True
			elif (puzzle[i][j] == 0) and (i == 0 and j == len(puzzle) - 1):
				if (((puzzle[i][j-1] == -1) or (puzzle[i][j-1] >= 1))
				and ((puzzle[i+1][j] == -1) or (puzzle[i+1][j] >= 1))):
					return True
			elif (puzzle[i][j] == 0) and (i == len(puzzle) - 1 and j == 0):
				if (((puzzle[i-1][j] == -1) or (puzzle[i-1][j] >= 1)) 
				and ((puzzle[i][j+1] == -1) or (puzzle[i][j+1] >= 1))):
					return True
			elif (puzzle[i][j] == 0) and (i == 0):
				if (((puzzle[i][j-1] == -1) or (puzzle[i][j-1] >= 1))
				and ((puzzle[i][j+1] == -1) or (puzzle[i][j+1] >= 1))
				and ((puzzle[i+1][j] == -1) or (puzzle[i+1][j] >= 1))):
					return True
			elif (puzzle[i][j] == 0) and (j == 0):
				if (((puzzle[i-1][j] == -1) or (puzzle[i-1][j] >= 1))
				and ((puzzle[i][j+1] == -1) or (puzzle[i][j+1] >= 1))
				and ((puzzle[i+1][j] == -1) or (puzzle[i+1][j] >= 1))):
					return True
			elif (puzzle[i][j] == 0):
				if (((puzzle[i-1][j] == -1) or (puzzle[i-1][j] >= 1)) 
				and ((puzzle[i][j-1] == -1) or (puzzle[i][j-1] >= 1))
				and ((puzzle[i][j+1] == -1) or (puzzle[i][j+1] >= 1))
				and ((puzzle[i+1][j] == -1) or (puzzle[i+1][j] >= 1))):
					return True
			'''
			numZeros = 0
			iOffset = 0
			jOffset = 0
			if (puzzle[i][j] == 0):
				# Check the 4 neighbors of the current location for 0s
				if (i-1 >= 0):
					if (puzzle[i-1][j] == 0):
						numZeros += 1
						iOffset = -1
				if (j-1 >= 0):
					if (puzzle[i][j-1] == 0):
						numZeros += 1
						jOffset = -1
				if (j+1 <= len(puzzle) - 1):
					if (puzzle[i][j+1] == 0):
						numZeros += 1
						jOffset = 1
				if (i+1 <= len(puzzle) - 1):
					if (puzzle[i+1][j] == 0):
						numZeros += 1
						iOffset = 1

				# return true if island of 1
				if (numZeros == 0):
					return True
				# if there was a single neighbor that was 0, check if there is an island of 2
				elif (numZeros == 1):
					# check the neighbors of the single neighboring zero
					if (i-1+iOffset >= 0):
						if (puzzle[i-1+iOffset][j+jOffset] == 0):
							numZeros += 1
					if (j-1+jOffset >= 0):
						if (puzzle[i+iOffset][j-1+jOffset] == 0):
							numZeros += 1
					if (j+1+jOffset <= len(puzzle) - 1):
						if (puzzle[i+iOffset][j+1+jOffset] == 0):
							numZeros += 1
					if (i+1+iOffset <= len(puzzle) - 1):
						if (puzzle[i+1+iOffset][j+jOffset] == 0):
							numZeros += 1
					
					if (numZeros == 2):
						return True
				
	return False
#            if (puzzle[i][j] = 0 and puzzle[i][j+1] = 0)     # two empty spaces next to each other
#            or (puzzle[i][j] = 0 and puzzle[i+1][j] = 0)     # two empty spaces one below the other
#            or (puzzle[i][j] = 0 and puzzle[i+1][j-1] = 0)   # two empty spaces diagonal below to the left
#            or (puzzle[i][j] = 0 and puzzle[i+1][j+1] = 0):  # two empty spaces diagonal below to the right
#                if (puzzle[][])
#                    puzzle =[
#                            [ 0, 0, 0, 0 ],
#                            [ 0, 0, 0, -1 ],
#                            [ 0, 0, -1, -1 ],
#                            [ 0, -1, -1, -1 ]
#                        ]

# ----------------- main program ----------------------

# initial puzzle board
# 0 means empty space, -1 means it's off the board
puzzle4x4 =[
    [ 0, 0, 0, 0 ],
    [ 0, 0, 0, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

puzzle7x7 =[
    [ 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, -1 ],
    [ 0, 0, 0, 0, 0, -1, -1 ],
    [ 0, 0, 0, 0, -1, -1, -1 ],
    [ 0, 0, 0, -1, -1, -1, -1 ],
    [ 0, 0, -1, -1, -1, -1, -1 ],
    [ 0, -1, -1, -1, -1, -1, -1 ]
]

puzzle10x10 =[
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
]

ninePuzzle10x10 =[
    [ 0, 0, 0, 0, 10, 10, 12, 12, 12, 12 ],
    [ 0, 0, 0, 0, 10, 10, 10, 11, 11, -1 ],
    [ 0, 0, 0, 0, 0, 11, 11, 11, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
]

elevenPuzzle10x10 =[
    [ 0, 0, 0, 0, 0, 0, 12, 12, 12, 12 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, 0, -1, -1, -1, -1, -1, -1, -1, -1 ],
    [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
]

# list of pieces
p1 = [[ 1, 1 ],         # light green
      [ 1, 0 ],
      [ 1, 0 ],  
      [ 1, 0 ]]

p2 = [[ 0, 1, 1 ],      # red
      [ 1, 1, 0 ],
      [ 1, 0, 0 ]]

p3 = [[ 1, 1 ],         # medium blue
      [ 1, 0 ],
      [ 1, 1 ]]

p4 = [[ 0, 1, 0 ],      # white
      [ 1, 1, 1 ],
      [ 0, 1, 0 ]]

p5 = [[ 0, 1 ],         # brown
      [ 1, 1 ]]

p6 = [[ 1, 1, 1, 1 ],   # dark green
      [ 0, 0, 1, 0 ]]

p7 = [[ 1, 1, 1 ],      # purple
      [ 1, 0, 0 ],
      [ 1, 0, 0 ]]

p8 = [[ 1, 1 ],         # pink
      [ 1, 1 ]]

p9 = [[ 1, 0 ],         # orange
      [ 1, 0 ],
      [ 1, 1 ]]

p10 = [[ 1, 1, 0 ],     # light blue
       [ 1, 1, 1 ]]

p11 = [[ 0, 0, 1, 1 ],  # dark blue
       [ 1, 1, 1, 0 ]]

p12 = [[ 1, 1, 1, 1 ],  # yellow
       [ 0, 0, 0, 0 ]]

#pieces4x4 = [p2, p1]
#pieces7x7 = [p1, p2, p3, p4, p5, p6]

optimizedPieces10x10 = [p7, p9, p10, p12, p8, p11, p3, p4, p6, p5, p1, p2]
ninePiece10x10 = [p7, p9, p8, p3, p4, p6, p5, p1, p2]
elevenPiece10x10 = [p7, p9, p10, p8, p11, p3, p4, p6, p5, p1, p2]

#BubblePuzzleAI(puzzle4x4, pieces4x4)

start = time.time()
BubblePuzzleAI(ninePuzzle10x10, ninePiece10x10)
end = time.time()
print(end - start)

start = time.time()
BubblePuzzleAI(elevenPuzzle10x10, elevenPiece10x10)
end = time.time()
print(end - start)

start = time.time()
BubblePuzzleAI(puzzle10x10, optimizedPieces10x10)
end = time.time()
print(end - start)

#pruning algorithm test cases
'''
testpuzzle1 =[
    [ 0, 1, 0, 0 ],
    [ 1, 1, 0, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle2 =[
    [ 0, 0, 0, 0 ],
    [ 0, 0, 0, -1 ],
    [ 1, 1, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle3 =[
    [ 0, 0, 1, 0 ],
    [ 0, 0, 1, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle4 =[
    [ 1, 1, 0, 0 ],
    [ 0, 1, 0, -1 ],
    [ 1, 1, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle5 =[
    [ 0, 1, 0, 1 ],
    [ 0, 1, 1, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle6 =[
    [ 0, 1, 1, 1 ],
    [ 0, 1, 0, -1 ],
    [ 0, 1, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle7 =[
    [ 1, 0, 0, 1 ],
    [ 1, 1, 0, -1 ],
    [ 0, 1, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle8 =[
    [ 0, 0, 0, 0 ],
    [ 0, 0, 0, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]

testpuzzle9 =[
    [ 1, 0, 0, 1 ],
    [ 1, 0, 1, -1 ],
    [ 0, 0, -1, -1 ],
    [ 0, -1, -1, -1 ]
]
testpuzzle10 =[
    [ 1, 0, 0, 0 ],
    [ 1, 1, 1, -1 ],
    [ 1, 1, -1, -1 ],
    [ 1, -1, -1, -1 ]
]

testpuzzle11 =[
    [ 1, 0, 0, 1 ],
    [ 1, 0, 1, -1 ],
    [ 1, 1, -1, -1 ],
    [ 1, -1, -1, -1 ]
]

print(Pruning(testpuzzle1))
print(Pruning(testpuzzle2))
print(Pruning(testpuzzle3))
print(Pruning(testpuzzle4))
print(Pruning(testpuzzle5))
print(Pruning(testpuzzle6))
print(Pruning(testpuzzle7))
print(Pruning(testpuzzle8))
print(Pruning(testpuzzle9))
print(Pruning(testpuzzle10))
print(Pruning(testpuzzle11))
'''