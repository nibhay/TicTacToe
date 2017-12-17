import sys
import os
from random import randint
arr=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
XorO={0:'X',1:'O'}
player=0
count=1
player_win_count={0:0, 1:0}

def init():
	'''
	initializes variables for new game
		arr: tic-tac-toe board
		player: randomly choose which player will play first
		XorO: dictionar player to X/O
		count: move count it can go upto 9
	'''
	global arr, XorO, count, player
	arr=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	player= randint(0,1)
	XorO= choice_X_or_O()
	count =1
	
def clear_screen():
	'''
	clears the console
	'''
	os.system('cls' if os.name=='nt' else 'clear')


def choice_X_or_O():
	'''
	asks the 1st player to choose between X or O
	'''
	inpt =''
	dict ={}
	while inpt not in ['X','O']:
		inpt=input("Player{} you want X or O: ".format(player+1)).upper()
	else:	
		dict[player]=inpt
		if(inpt=='X'):
			dict[1-player]='O'
		else:
			dict[1-player]='X'
	return dict

def print_board():
	'''
	Prints current state of tic-tac-toe board
	'''
	clear_screen()
	row_num=1
	for row in arr:
		print("   |   |")
		col_num=1
		for elem in row :
			print (" "+elem+" ", end='')
			if col_num !=3:
				print("|",end='')
			col_num+=1
		if row_num!=3:
			print("\n___|___|___")
		else:
			print("\n   |   |")
		row_num+=1

def input_move():
	'''
	This method takes a number from system input, and returns a tupel of row,col on the board
	'''
	inpt=''
	while(inpt not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
		inpt = input("Enter a number between 1 to 9: ")
	else:
		inpt =int(inpt)-1
	return ( int(inpt/3), inpt%3)

def ask_to_play_next_move():
	'''
	Takes input from user
	'''
	print("player{}'s Turn".format(player+1))
	return input_move()

def play():
	'''
	main game:
		1. ask for input cell from a player till the player enters a valid cell
		2. update the board
		3. check if any player has won, if not switch player, if true return
		4. check if the game is draw, if true return
		5. repeat from step 1-5
	'''
	move=ask_to_play_next_move()
	while(validate_move(move[0],move[1]) == False):
		move = ask_to_play_next_move()
	update_board(move)
	if(check_is_win(move)):
		update_score()
		print ("congratulations, Player{} is Winner!!" .format(player+1))
		return
	if(check_draw()):
		print ("Game draw!")
		return
	play()

def update_score():
	'''
	increases the score for current player
	'''
	global player_win_count
	player_win_count[player]+=1
	
def update_board(move):
	'''
	updates the move in the board
	'''
	global arr
	arr[move[0]][move[1]]=XorO[player]
	print_board()

def row_match(row):
	'''
	checks if the every element in the row is same as played by the player in current move
	Input: row
	Result: True if win, otherwise False 
	'''
	for col in range(0,3):
		if arr[row][col]!=XorO[player]:
			return False
	return True

def col_match(col):
	'''
	checks if the every element in the coloumn is same as played by the player in current move
	Input: col
	Result: True if win, otherwise False 
	'''
	for row in range(0,3):
		if arr[row][col]!=XorO[player]:
			return False
	return True

def diagonal_match(move):
	'''
	checks if the every element in the left or right diagonal is same as played by the player in current move
	Input: move <---- tuple (row,col)
	Result: True if win, otherwise False 
	'''
	if(move[0] != move[1] and (move[0] + move[1]) != 2):
		return False
	if(move[0] == move[1]):
		for i in range(0,3):
			if(arr[i][i] != XorO[player]):
				break
		else: 
			return True
	if(move[0]+move[1]==2):
		for i in range(0,3):
			if(arr[i][2-i]!=XorO[player]):
				break
		else: 
			return True
	return False

def swith_player():
	'''
	switches player
	'''
	global player
	player=1-player


def check_is_win(move):
	'''
	checks if the current move result in win 
	'''
	global count
	count+=1
	if row_match(move[0]) or col_match(move[1]) or diagonal_match(move):
		return True
	swith_player()
	return False


def check_draw():
	'''
	checks if the game is draw
	'''
	if(count>9):
		return True
	return False


def validate_move(row, col):
	'''
	validates if the cell at row, col is available
	'''
	val=arr[row][col]
	if(val!=" "):
		return False
	return True

def start_game():
	'''
	starting point of the game
	'''
	init()
	print_board()
	play()
	print("Score Player1: {} , Player2: {}".format(player_win_count[0],player_win_count[1]))
	run_again =input("do you want to play again Y/N: ")
	run_again=run_again.lower()
	if(run_again.startswith('y')):
		start_game()	


start_game()