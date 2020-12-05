#EEE 111 WFXY2 PRE-SOFTWARE PROJECT
#BEA ROSARI B. SUPANGA ---> 2018-10282
#TIC-TAC-TOE

def initBoard(board):
	"""This function initializes the board to be empty"""
	board = [['*','*','*'],['*','*','*'],['*','*','*']]	
	#I used asterisk as a non-whitespace character to indicate an empty position
	return board

def printBoard(board):
	"""This function displays the contents of the board"""
	print("         ")
	print("    1 2 3")
	print("---------")
	print("1 |", board[0][0],board[0][1],board[0][2])
	print("2 |", board[1][0],board[1][1],board[1][2])
	print("3 |", board[2][0],board[2][1],board[2][2])	

def isFilled(board):
	"""This function determines if a board is completely filled with pieces."""
	for row in board:
		for col in row:
			if col == '*':
				return -1
	return 0

def placePiece(board,row,col,piece):
	"""This function places the character piece into the corresponding row and col"""
	if row.isdigit()==False or col.isdigit()==False:
		return -1
	if int(row) >3 or int(col) >3 or int(row)<1 or int(col) <1:
		return -1 #Error handling if input for row and column is not within 1-3
	if board[int(row)-1][int(col)-1]!='*':
		return -1 #Returns -1 if not yet filled
	if piece == 1:
		board[int(row)-1][int(col)-1] = 'X' #Placing an X (Player 1)
	if piece == 2:
		board[int(row)-1][int(col)-1] = 'O' #Placing an O (Player 2)
	return 0 #Returns a value of 0 is the board is completely filled with pieces. 

def checkWin(board,piece):
	"""A function that checks the board for an occurence where three of
	 the same piece is lined up in the same row, col, or diagonal."""
	if piece == 1: #Checks the win combinations for X(Player 1)
		if not(checkRow(board,0)==checkRow(board,1)==checkRow(board,2)):
			print('Winner player 1')
			return 1
		if not(checkCol(board,0)==checkCol(board,1)==checkCol(board,2)):
			print('Winner player 1')
			return 1
		if checkDiag(board):
			print('Winner player 1')
			return 1
	if piece == 2: #Checks the win combinations for O(Player 2)
		if not(checkRow(board,0)==checkRow(board,1)==checkRow(board,2)):
			print('Winner player 2')
			return 1
		if not(checkCol(board,0)==checkCol(board,1)==checkCol(board,2)):
			print('Winner player 2')
			return 1
		if checkDiag(board):
			print('Winner player 2')
			return 1

def checkRow(board,row):
	"""This function checks the where three of the same piece 
	is lined up in the same row"""
	if board[row][0]==board[row][1]==board[row][2]!='*':
		return 1
	return 0

def checkCol(board,col):
	"""This function checks the where three of the same piece 
	is lined up in the same column"""
	if board[0][col]==board[1][col]==board[2][col]!='*':
		return 1
	return 0
	
def checkDiag(board):
	"""This function checks the where three of the same piece 
	is lined up in the same diagonal"""
	if board[0][0]==board[1][1]==board[2][2]!='*':
		return 1
	if board[0][2]==board[1][1]==board[2][0]!='*':
		return 1
	return 0
	
def main():	
	"""Main function for Tic-Tac-Toe program"""	
	board=[] #Empty list for board			
	board= initBoard(board) #Initializing contents for board
	print("         ")
	print("Welcome to Bea's TicTacToe! :) ")
	printBoard(board) #Displaying empty board 
	while(1):
		print("         ")
		print("Player 1") #Inputs for Player 1(X)
		row = input("Enter row:") #Asking for coordinates
		col = input("Enter col:")
		while(placePiece(board,(row),(col),1)): 
			#Checking if input coordinates are valid
			print('Invalid Coordinates. Try Again') #Error handling
			row =input("Enter row:") #Asking for user input again
			col =input("Enter col:")
		printBoard(board) #Displaying updated board
		if(checkWin(board,1)): #Stops the game when Player 1 wins
			break
		if(not(isFilled(board))): #Stops the game when board is filled
			print('Draw') #Tie between Player 1 and 2
			break
		print("         ")
		print("Player 2") #Inputs for Player 2(0)
		row = input("Enter row:")
		col = input("Enter col:")
		while(placePiece(board,(row),(col),2)):
			#Checking if input coordinates are valid
			print('Invalid Coordinates. Try Again') #Error handling
			row=input('Enter row:') #Asking for user input again
			col = input('Enter col:')
		printBoard(board) #Displaying updated board
		if(checkWin(board,1)): #Stops the game when Player 2 wins
			break

if __name__== "__main__":
	main()
