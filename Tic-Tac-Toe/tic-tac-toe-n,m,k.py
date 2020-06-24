import os
# made in linux, please check in linux

# global variables
gamesFinished = []
gamesNotFinished = []
actualGame = [0,0,0,[],""]
actualBoard  = [ ['-' for i in range(1000) ] for j in range(1000)]
# global variables



def ls(ruta = '.'):
    return os.listdir(ruta)

def readDataArchive(arch):
	data = [0,0,0,[],""]
	try:
		file = open(arch,"r").readlines()
		n,m,k = file[0].split() 
		data[0],data[1],data[2] = int(n),int(m),int(k)
		for i in range(1,len(file)):
			x,y = file[i].split()
			x,y = int(x),int(y)
			data[3].append([x,y])
		data[4] = arch
	except:
		data[0] = -1
	# n,m,k, list of a moves 
	return data
def createArchive(arch):
	
	file = open(arch,"w")
	file.write(str(actualGame[0])+" "+str(actualGame[1])+ " "+str(actualGame[2])+"\n")
	for move in actualGame[3]:
		file.write(str(move[0])+" "+str(move[1])+"\n")
	file.close()


def chargeArchive():
	for arch in ls():
		if(arch == "tic-tac-toe-n,m,k.py"):
			continue
		if arch[-5:]==".ttt1":
			gameAux = readDataArchive(arch)
			if(gameAux[0]>0):
				gamesFinished.append(gameAux)
		if arch[-5:]==".ttt0":
			gameAux = readDataArchive(arch)
			if(gameAux[0]>0):
				gamesNotFinished.append(gameAux)


def pause():
	print()
	input("Press enter to continue: ")
	print()

def printBoard():
	for i in range(actualGame[0]):
		for j in range(actualGame[1]):
			print(actualBoard[i][j],end="")
		print()

def cleanBoard():
	for i in range(actualGame[0]):
		for j in range(actualGame[1]):
			actualBoard[i][j] = '-'


def readMove():
	while 1:
		try:
			move = input().split()
			if(len(move)>2):
				print("Try again : ",end="")
				continue
			x,y = int(move[0]),int(move[1])
			if(actualBoard[x][y] != '-'):
				print("Location kept. Try again: ",end=" ")
				continue
			if(x == -1 and y==-1): 
				return [-1,-1]
			if 0<=x and x<actualGame[0] and 0<=y and y<actualGame[1]:
				return [x,y]
		except:
				print("Sorry. ",end="")
		print("Try again : ",end="")
	
		

def saveGame(isFinished):
	# create archive
	arch = input("Enter the name of the game: ")
	arch = arch + ".ttt" + str(isFinished)
	actualGame[4] = arch
	createArchive(arch)
	# save in list	
	if(isFinished==0):
		gamesNotFinished.append([actualGame[0],actualGame[1],actualGame[2],[ ele for ele in actualGame[3] ],actualGame[4]])
	else:
		gamesFinished.append([actualGame[0],actualGame[1],actualGame[2],[ ele for ele in actualGame[3] ],actualGame[4] ])
def checkWinGame(x,y):
	k = actualGame[2]
	# check rows and columns
	cont = -1
	a,b=x,y
	while a>=0 and actualBoard[a][b] == actualBoard[x][y]:
		a-=1
		cont+=1
	a,b=x,y
	while a<actualGame[0] and actualBoard[a][b] == actualBoard[x][y]:
		a+=1
		cont+=1
	if cont >=k:
		return True
	cont = -1
	a,b=x,y
	while b>=0 and actualBoard[a][b] == actualBoard[x][y]:
		b-=1
		cont+=1
	a,b=x,y
	while b<actualGame[1] and actualBoard[a][b] == actualBoard[x][y]:
		b+=1
		cont+=1
	if cont >=k:
		return True
	# check diagonals
	cont = -1
	a,b=x,y
	while a>=0 and b>=0 and actualBoard[a][b] == actualBoard[x][y]:
		a,b=a-1,b-1
		cont+=1
	a,b=x,y
	while a<actualGame[0] and b<actualGame[1] and actualBoard[a][b] == actualBoard[x][y]:
		a,b=a+1,b+1
		cont+=1
	if cont >=k:
		return True
	cont = -1
	a,b=x,y
	while b>=0 and a<actualGame[0] and actualBoard[a][b] == actualBoard[x][y]:
		b,a=b-1,a+1
		cont+=1
	a,b=x,y
	while a>=0 and b<actualGame[1] and actualBoard[a][b] == actualBoard[x][y]:
		a,b=a-1,b+1
		cont+=1
	if cont >=k:
		return True
	return False

def runningGame():
	global actualGame
	global actualBoard
	pos =  len(actualGame[3]) %2
	go  = 1
	while(1):
		os.system("clear")
		print()
		print("n:",actualGame[0],"m:",actualGame[1],"k:",actualGame[2])
		print("Remember: print -1 -1 for saving the game")
		print()
		printBoard()
		print()
		if(pos==0):
			print("Turn of a first player: ")
			x,y = readMove()
			if(x==-1 and y==-1):
				saveGame(0)
				go=0
				break
			actualGame[3].append([x,y])
			actualBoard[x][y] = 'X'
		else:
			print("Turn of a second player: ")
			x,y = readMove()
			if(x==-1 and y==-1):
				saveGame(0)
				go=0
				break
			actualGame[3].append([x,y])
			actualBoard[x][y] = 'O'
		if(checkWinGame(x,y)):
			os.system("clear")
			if(pos==0): 
				print("Fist player win")
			else:
				print("Second player win")
			print()
			printBoard()
			print()
			pause()
			break
		if(len(actualGame[3])==actualGame[0]*actualGame[1]):
			print("Draw game")
			print()
			printBoard()
			print()
			pause()
		pos = 1 - pos

	if(go==1):
		saveGame(1)

def cmpBoard(game):
	return len(game[3])

def menuPreviousGame():
	global actualGame
	global actualBoard
	while 1:
		os.system("clear")
		if(len(gamesNotFinished)==0):
			print("Not previous games")
			pause()
			return
		print("Choose a previous game.")
		op = -1
		cont = 1
		for game in gamesNotFinished:
			print(cont,". "+game[4])
			cont+=1
		print("0. Exit menu")
		while 1:
			try:
				op = int(input("Chose index of a game: "))
				if op<0 or op>len(gamesNotFinished):
					op = error(),xd  # Sorry for bad trick  
				break
			except:
				print("Try again: ",end="")
		if op==0:
			break
		ind = op
		global actualGame
		actualGame = gamesNotFinished[op-1]	
		os.system('clear')
		print()
		print("-------------------------------------------------")
		print("Choose a option")
		print("1. Play game")
		print("2. Delete game")
		print("0. Back last menu")
		print("-------------------------------------------------")
		print()
		while 1:
			try:
				op = int(input("Chose index of a game: "))
				if op<0 or op>len(gamesNotFinished):
					op = error(),xd  # Sorry for bad trick  
				break
			except:
				print("Try again: ",end="")
		if op==2:
			os.remove(gamesNotFinished[ind-1][4])
			gamesNotFinished.pop(ind-1)
		elif op==1:
			pos = 0
			cleanBoard()
			for move in actualGame[3]:	
				if pos==0:
					actualBoard[move[0]][move[1]] = 'X'
				else:
					actualBoard[move[0]][move[1]] = 'O'
				pos = 1-pos
			runningGame()

def showPastGames():
	os.system("clear")
	gamesFinished.sort(key=cmpBoard,reverse=True)
	cont = 1
	for game in gamesFinished:
		print(cont,". "+game[4])
		print("    Number of moves:", cmpBoard(game))
		cont+=1
	pause()

def showPastBoard():
	os.system("clear")
	if(len(gamesFinished)==0):
		print("Not game finished. Play more")
		pause()
		return
	while 1:
		os.system("clear")
		print("Choose a game.")
		cont = 1
		for game in gamesFinished:
			print(cont,". "+game[4])
			cont+=1
		print("0. Back to menu")
		op = 0
		while 1:
			try:
				op = int(input("Chose index of a game: "))
				if op<0 or op>len(gamesFinished):
					op = error(),xd  # Sorry for bad trick  
				break
			except:
				print("Try again: ",end="")
		if(op==0):
			break
		global actualGame
		global actualBoard
		actualGame = gamesFinished[op-1]
		pos = 0
		cleanBoard()	
		for move in actualGame[3]:	
			if pos==0:
				actualBoard[move[0]][move[1]] = 'X'
			else:
				actualBoard[move[0]][move[1]] = 'O'
			pos = 1-pos
		print()
		printBoard()
		print()
		pause()

def menu():
	while 1:
		os.system('clear')
		print()
		print("-------------------------------------------------")
		print("Welcome to tic-tac-toe n,m,k version")
		print()
		print("Choose options")
		print("1. Play game ")
		print("2. Play o erase previous game")
		print("3. View past games ")
		print("4. Show past gameboards ")
		print("0. Exit")
		print("-------------------------------------------------")
		print()
		print("Choose your options: ")
		op = input()

		if(op=='0'):
			break
		elif op =='1':
			print()
			while 1:
				try:
					dim =  input("Enter the board dimensiones (n<=1000,m<1000): ").split()
					if int(dim[0])<=0 or int(dim[1])<=0:
						print("Try again.")
						continue
					actualGame[0],actualGame[1] = min(1000,int(dim[0])),min(1000,int(dim[1]))
					break
				except:
					print("Try again. ")
			while 1:
				try:
					valueOfK = input("Enter the value of k<=max(m,n): ")
					if int(valueOfK)<=0:
						print("Try again. ")
						continue
					actualGame[2] = min(max(actualGame[0],actualGame[1]),int(valueOfK)) 
					break
				except:
					print("Try again. ")
			cleanBoard()
			actualGame[3] = []
			actualGame[4] = ''
			runningGame()
		elif op =='2':
			menuPreviousGame()
		elif op =='3':
			showPastGames()
		elif op =='4': 
			showPastBoard()
		else:
			print()
			print("Incorrect option")
			pause()
			print()




chargeArchive()
menu()
