#EEE 111 WFXY2 PRE-SOFTWARE PROJECT
#BEA ROSARI B. SUPANGA ---> 2018-10282
#GAME OF LIFE

def initGrid(h,w):
	"""This function initializes the 2D list represented by zeroes"""
	grid = [[0 for i in range(w)] for j in range(h)]
	return(grid)

def displayGrid(temp):
	"""This function displays the contents of the grid"""
	for row in temp:
		for col in row:
			print (col,end='')
		print()

def upperleft(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the upperleft"""
	count = 0
	if grid[i+1][j]==1:
		count = count+1
	if grid[i+1][j+1]==1:
		count = count+1
	if grid[i][j+1]==1:
		count = count+1
	return count

def lowerleft(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the lowerleft"""
	count = 0
	if grid[i-1][j]==1:
		count = count+1
	if grid[i-1][j+1]==1:
		count = count+1
	if grid[i][j+1]==1:
		count = count+1
	return count

def upperright(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the upperright"""
	count = 0
	if grid[i+1][j]==1:
		count = count+1
	if grid[i+1][j-1]==1:
		count = count+1
	if grid[i][j-1]==1:
		count = count+1
	return count

def lowerright(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the lowerright"""
	count = 0
	if grid[i-1][j]==1:
		count = count+1
	if grid[i-1][j-1]==1:
		count = count+1
	if grid[i][j-1]==1:
		count = count+1
	return count

def left(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the leftmost side"""
	count=0
	if grid[i-1][j]==1:
		count = count+1
	if grid[i+1][j]==1:
		count = count+1
	if grid[i-1][j+1]==1:
		count = count+1
	if grid[i][j+1]==1:
		count = count+1
	if grid[i+1][j+1]==1:
		count=count+1
	return count

def top(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the topmost side"""
	count=0
	if grid[i][j-1]==1:
		count = count+1
	if grid[i+1][j-1]==1:
		count = count+1
	if grid[i+1][j]==1:
		count = count+1
	if grid[i+1][j+1]==1:
		count = count+1
	if grid[i][j+1]==1:
		count=count+1
	return count

def bottom(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the bottommost side"""
	count=0
	if grid[i][j-1]==1:
		count = count+1
	if grid[i-1][j-1]==1:
		count = count+1
	if grid[i-1][j]==1:
		count = count+1
	if grid[i-1][j+1]==1:
		count = count+1
	if grid[i][j+1]==1:
		count=count+1
	return count

def right(i,j,grid):
	"""This function counts the number of live neighbors if the cell is in located in the rightmost side"""
	count=0
	if grid[i-1][j]==1:
		count = count+1
	if grid[i-1][j-1]==1:
		count = count+1
	if grid[i][j-1]==1:
		count = count+1
	if grid[i+1][j-1]==1:
		count = count+1
	if grid[i+1][j]==1:
		count=count+1
	return count

def normal(i,j,grid):
	"""This function counts the number of live neighbors if the cell is not a corner."""
	count=0
	if grid[i-1][j-1]==1:
		count=count+1
	if grid[i][j-1]==1:
		count=count+1
	if grid[i+1][j-1]==1:
		count=count+1
	if grid[i-1][j]==1:
		count=count+1
	if grid[i+1][j]==1:
		count=count+1
	if grid[i-1][j+1]==1:
		count=count+1
	if grid[i][j+1]==1:
		count=count+1
	if grid[i+1][j+1]==1:
		count=count+1
	return count

def checknode(i,j,grid,temp):
	"""This function that checks and counts the number of neighbors of a coordinate in the grid."""
	"""Under this function as well, is the implementation of the rules of “Game of Life” 
	based on the number of neighbors of a coordinate in the grid."""

	count=0 #The total number of live neighbors 
	if i ==0 and j ==0:
		count = upperleft(i,j,grid)
	elif i==0 and j ==20:
		count = upperright(i,j,grid)
	elif i==0:
		count = top(i,j,grid)
	elif i ==20 and j ==0:
		count = lowerright(i,j,grid)
	elif i==20 and j ==20:
		count = lowerright(i,j,grid)
	elif i==20:
		count = bottom(i,j,grid)
	elif j==0:
		count = left(i,j,grid)
	elif j==20:
		count = right(i,j,grid)
	else:
		count = normal(i,j,grid)

	if grid[i][j]==1: #General rules of Game of Life based on the number of live neighbors
		if count<2:
			temp[i][j]=0 #Each cell with one or no neighbors dies, as if by solitude.
		if count>3:
			temp[i][j]=0 #Each cell with four or more neighbors dies, as if by overpopulation.
		if count==2 or count==3:
			temp[i][j]=1 #Each cell with two or three neighbors survives.
	elif grid[i][j]==0:
		if count==3:
			temp[i][j]=1 #Each cell with three neighbors becomes populated.


def main():
	"""Main function of the Game of Life program"""
	file= input("Choose from the text files: \n -tumbler.txt \n -corners.txt \n -cross.txt \n -exploder.txt \n -small_exploder.txt \n ten_cell_row.txt \nEnter the name of file you want to input:") #User-inputted name of the file with the coordinates
	grid = initGrid(21,21) 
	#if file== "tumbler.txt" or "corners.txt" or "cross.txt" or "exploder.txt" or "small_exploder.txt" or "ten_cell_row.txt" :
	fh=open(file,'r') #Opens the file inputter by user and reads it
	coor=[]
	for line in fh:
		for val in line.split():
			coor.append(int(val)) #Making a list of all the numbers in the file
	coor.pop(0) #Deleting the first line/number N which represents the number of succeeding lines in the file.
	x=[] #list for the x-coordinates
	y=[] #list for the y-coordinates
	for i in range (0,len(coor)):
		if i%2==0: #if the index is even, it is an x-coordinate
			x.append(coor[i])
		else: #if the index is odd, it is a y-coordinate
			y.append(coor[i])

	for i in range(0,len(x)):
		grid[x[i]][y[i]]=1 #This loop changes the cell into a 1 if it is a coordinate based on the list of coordinates.

	fh.close() #closing file for formality 


	for iterations in range(0,11): #Runs the simulated execution for each iteration for ten iterations.
		temp = initGrid(21,21) #temp is the new grid containing the results of the execution of rules
		print("Run: "+ str(iterations))
		displayGrid(grid) #displays the grid for each step 
		for i in range(0,21):
			for j in range(0,21):
				checknode(i,j,grid,temp) #Checks the live neighbors and state of every cell 
		grid = temp 
		

if __name__== "__main__":
	main()

