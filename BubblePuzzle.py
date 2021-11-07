import copy
import time
from matplotlib import pyplot as plt

# Depth Limited Search for the puzzle
# Places the puzzle pieces onto the board in the order that they are listed in the pieces array.
# Recursively calls itself to search the entire search space for all valid solutions
# parameters:
#		puzzle: a 2d array representing the state of the puzzle board
#		pieces: an array of 2d puzzle pieces that will be put in the board
#		currentDepth: the current depth of the DLS
#		maxDepth: the maximum depth of the DLS
#		pruneSize: the maximum size of islands that should be pruned. size can be 0, 1, 2, or 3+
# returns: void	
def DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth, pruneSize):
	prune = False
	rows = len(puzzle)
	cols = len(puzzle)

	plt.imshow(puzzle)
	plt.pause(0.000000001)

	pieceRows = len(pieces[currentDepth])
	pieceCols = len(pieces[currentDepth][0])

	for i in range(rows):
		# Check if piece will go out of bounds of the puzzle rows
		if (i + pieceRows > rows):
			break
		for j in range(cols):

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
					if ((puzzle[i+k][j+l] != 0) and pieces[currentDepth][k][l] == 1):
						prune = True
						break
					elif (pieces[currentDepth][k][l] == 1):
						puzzle[i+k][j+l] = currentDepth + 1
			
			# Reset the puzzle board if the piece won't fit at the current spot
			if (prune == True):
				puzzle = copy.deepcopy(tempPuzzle)
			# prune if there is an island
			else:
				prune = Pruning(puzzle, pruneSize)
				if (prune == True):
					puzzle = copy.deepcopy(tempPuzzle)

			# Recursively call the DLS function for the new depth if we aren't pruning
			if (prune == False and currentDepth < maxDepth - 1):
				DepthLimitedSearch(puzzle, pieces, currentDepth + 1, maxDepth, pruneSize)
				puzzle = copy.deepcopy(tempPuzzle)
			# Base Case : we found a valid puzzle board. print the board and return True
			elif (prune == False and currentDepth == maxDepth - 1):
				for k in range (rows):
					print(puzzle[k])
				print("\n")
				return
	return

# Helper function for the Depth Limited Search
def BubblePuzzleAI(puzzle, pieces, pruneSize):
	currentDepth = 0
	maxDepth = len(pieces)
	DepthLimitedSearch(puzzle, pieces, currentDepth, maxDepth, pruneSize)
	return

# Pruning function
# counts the number of zeros around each zero to determine if an island of zeros exists
# parameters:
#		puzzle: a 2d array representing the state of the puzzle board
#		pruneSize: the maximum size of islands that should be pruned. size can be 0, 1, 2, or 3+
# returns:
# 		True if there is an island and the board should be pruned
def Pruning(puzzle, pruneSize):
	if (pruneSize <= 0):
		return False
	for i in range(len(puzzle)):
		for j in range(len(puzzle[i])):
			if puzzle[i][j] == -1:
				break
			numZeros = 0
			iOffset1 = 0
			jOffset1 = 0
			iOffset2 = 0
			jOffset2 = 0
			if (puzzle[i][j] == 0):
				# Check the 4 neighbors of the current location for 0s
				if (i-1 >= 0 
				and puzzle[i-1][j] == 0):
					numZeros += 1
					iOffset1 = -1
				if (j-1 >= 0 
				and puzzle[i][j-1] == 0):
					numZeros += 1
					jOffset1 = -1
				if (j+1 <= len(puzzle) - 1 
				and puzzle[i][j+1] == 0):
					numZeros += 1
					jOffset1 = 1
				if (i+1 <= len(puzzle) - 1 
				and puzzle[i+1][j] == 0):
					numZeros += 1
					iOffset1 = 1

				# return true if island of size 1
				if (numZeros == 0):
					return True
				# if one neighbor is 0, check if there is an island of size 2
				elif (numZeros == 1 and pruneSize >= 2):
					# check the neighbors of the single neighboring zero
					if (i-1+iOffset1 >= 0 
					and puzzle[i-1+iOffset1][j+jOffset1] == 0):
						numZeros += 1
						if (iOffset1 == -1):
							iOffset2 = -1
					if (j-1+jOffset1 >= 0 
					and puzzle[i+iOffset1][j-1+jOffset1] == 0):
						numZeros += 1
						if (jOffset1 == -1):
							jOffset2 = -1
					if (j+1+jOffset1 <= len(puzzle) - 1 
					and puzzle[i+iOffset1][j+1+jOffset1] == 0):
						numZeros += 1
						if (jOffset1 == 1):
							jOffset2 = 1
					if (i+1+iOffset1 <= len(puzzle) - 1 
					and puzzle[i+1+iOffset1][j+jOffset1] == 0):
						numZeros += 1
						if (iOffset1 == 1):
							iOffset2 = 1
					
					if (numZeros == 2):
						return True
					# check if there is an island of 3 in a straight line
					elif(numZeros == 3 and pruneSize >= 3 and (iOffset1+iOffset2 == 2 or jOffset1+jOffset2 == 2)):
						if (i-1+iOffset1+iOffset2 >= 0
						and puzzle[i-1+iOffset1+iOffset2][j+jOffset1+jOffset2] == 0):
							numZeros += 1
						if (j-1+jOffset1+jOffset2 >= 0 
						and puzzle[i+iOffset1+iOffset2][j-1+jOffset1+jOffset2] == 0):
							numZeros += 1
						if (j+1+jOffset1+jOffset2 <= len(puzzle) - 1 
						and puzzle[i+iOffset1+iOffset2][j+1+jOffset1+jOffset2] == 0):
							numZeros += 1
						if (i+1+iOffset1+iOffset2 <= len(puzzle) - 1 
						and puzzle[i+1+iOffset1+iOffset2][j+jOffset1+jOffset2] == 0):
							numZeros += 1
						if (numZeros == 4):
							return True		
	return False

# ----------------- main program ----------------------
if __name__ == "__main__":
	# initial puzzle boards
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

	print("\nWelcome to the Daiso Bubble Puzzle Solver.")
	print("When given the pieces used and initial state of the board, The Solver finds the solutions to a Daiso bubble puzzle")
	print("The Solver will exhaust the search tree for the given board state to find all possible solutions.\n")

	#pieces4x4 = [p2, p1]
	#pieces7x7 = [p1, p2, p3, p4, p5, p6]

	ninePiece10x10 = [p4, p3, p1, p6, p7, p2, p8, p9, p5]
	elevenPiece10x10 = [p4, p11, p3, p1, p6, p7, p10, p2, p8, p9, p5]
	twelvePieces10x10 = [p4, p11, p3, p1, p6, p7, p10, p2, p8, p9, p12, p5] # Fastest order found, runs for about 3 minutes when pruning

	#BubblePuzzleAI(puzzle4x4, pieces4x4, 3)
	print("Here is a puzzle with 3 pieces inserted into it:")
	for i in range (len(ninePuzzle10x10)):
		print(ninePuzzle10x10[i])
	print("\n")

	print("Finding solutions to the puzzle:")
	start = time.time()
	BubblePuzzleAI(ninePuzzle10x10, ninePiece10x10, 3)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

	print("Here is a puzzle with 1 piece inserted into it:")
	for i in range (len(elevenPuzzle10x10)):
		print(elevenPuzzle10x10[i])
	print("\n")

	print("Finding solutions to the puzzle:")
	start = time.time()
	BubblePuzzleAI(elevenPuzzle10x10, elevenPiece10x10, 3)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

	print("Here is an empty puzzle board with no pieces inserted into it:")
	for i in range (len(puzzle10x10)):
		print(puzzle10x10[i])
	print("\n")

	print("Finding solutions to the puzzle by pruning islands of up to size 3:")
	start = time.time()
	puzzle = copy.deepcopy(puzzle10x10)
	BubblePuzzleAI(puzzle, twelvePieces10x10, 3)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

	print("Finding solutions to the puzzle by pruning islands of up to size 2:")
	start = time.time()
	puzzle = copy.deepcopy(puzzle10x10)
	BubblePuzzleAI(puzzle, twelvePieces10x10, 2)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

	print("Finding solutions to the puzzle by pruning islands of up to size 1:")
	start = time.time()
	puzzle = copy.deepcopy(puzzle10x10)
	BubblePuzzleAI(puzzle, twelvePieces10x10, 1)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

	print("Finding solutions to the puzzle without pruning any islands:")
	start = time.time()
	puzzle = copy.deepcopy(puzzle10x10)
	BubblePuzzleAI(puzzle, twelvePieces10x10, 0)
	end = time.time()
	seconds = end - start
	print("Time taken: %.3f seconds" %seconds)

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

	print(Pruning(testpuzzle1, 3))
	print(Pruning(testpuzzle2, 3))
	print(Pruning(testpuzzle3, 3))
	print(Pruning(testpuzzle4, 3))
	print(Pruning(testpuzzle5, 3))
	print(Pruning(testpuzzle6, 3))
	print(Pruning(testpuzzle7, 3))
	print(Pruning(testpuzzle8, 3))
	print(Pruning(testpuzzle9, 3))
	print(Pruning(testpuzzle10, 3))
	print(Pruning(testpuzzle11, 3))
	'''