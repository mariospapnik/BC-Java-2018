'''
	## Hangman PvsAI
	Create a game for one player against the computer. The computer has a 'word bank', a list of words, 
	from where it chooses one for the game. The player tries to guess it, character by character with a maximum of 7 guesses. 
	If he manages to guess it he wins otherwise he loses. The game continually provides visual aid about the state of the game.
'''

from random import choice
from os import system

# MAIN LOOP FOR ONE ROUND
def One_Round(Lsecret, Lfound, tries, Hangman):
	used_letters = []
	while tries>0 and Lsecret!=Lfound:
		print("*"*20)
		print_Hangman(tries,Hangman)
		Print_Found(Lfound)
		print("\nTries:", tries)
		letter = input("Choose a letter:")
		while len(letter)!= 1 or not letter.isalpha() or letter.isupper() or letter in used_letters:
			letter = input("Choose a letter:")
		Lsecret, Lfound, tries= Letter_Lookup(letter,Lsecret,Lfound,tries)
		used_letters.append(letter)
		system('cls')
	return(Lsecret, Lfound, tries)

# PRINT THE LIST OF THE FOUND LETTERS
def Print_Found(Lfound):
	for i in range(len(Lfound)):
		print(" ",Lfound[i], end = ' ')

# LOOK IF LETTER EXISTS IN WORD
def	Letter_Lookup(letter,Lsecret,Lfound,tries):
		found = []
		for i in range(len(Lsecret)):
			if letter == Lsecret[i]:
				found.append(i)
				print('found letter',letter,"in index",i+1)
		if found==[]:
			print("try again")
			tries -=1
		else:
			for id in found:
				Lfound[id] = Lsecret[id]
		return(Lsecret,Lfound,tries)

# PRINT THE HANGMAN!
def print_Hangman(tries,Hangman):
	All = Hangman[tries-1]
	for i in range(len(All)):
		for j in range(len(All[i])):
			print(All[i][j], end='')
		print(' ')

# CHECK IF PLAYER WINS OF LOOSES		
def Won_Lost_Select(tries, Lfound, Lsecret, secretWord):		
	if tries == 0:
		print("*"*20)
		Print_Found(Lfound)
		print("\n You lost! the word is: ", secretWord)
		return False
		
	if Lsecret == Lfound:
		print("*"*20)
		Print_Found(Lfound)
		print("\n You won! the word is: ", secretWord)
		return True
		
#SELECT SINGLE OR DUAL PLAYER MODE
def Mode_Select():
	selection = input("select Mode: \n 1.Single Player	2.Dual Player\n")
	while True:
		if selection=='1':
			print("Single Player selected!")
			return False
		if selection=='2':
			print("Dual Player selected!")
			return True
			
#Lists for hangman display
#Tries7
A=['-','-','-','-','-','-','-','-']
B=['|']
All7 = [A,B,B,B,B,B,B,B]

#Tries6
B1=['|',' ',' ',' ',' ',' ',' ','|']
All6 = [A,B1,B,B,B,B,B,B]

#Tries5
C1=['|',' ',' ',' ',' ',' ','(',')']
All5 = [A,B1,C1,B,B,B,B,B]

#Tries4
D=['|',' ',' ',' ',' ',' ','|','|',' ']
E=['|',' ',' ',' ',' ',' ','|','|',' ',' ']
All4 = [A,B1,C1,D,E,B,B,B]

#Tries3
D1=['|',' ',' ',' ',' ','/','|','|','']
E1=['|',' ',' ',' ','/',' ','|','|',' ','']
All3 = [A,B1,C1,D1,E1,B,B,B]

#Tries2
D2=['|',' ',' ',' ',' ','/','|','|','\\']
E2=['|',' ',' ',' ','/',' ','|','|',' ','\\']
All2 = [A,B1,C1,D2,E2,B,B,B]

#Tries1
F=['|',' ',' ',' ',' ','/',' ',' ','']
G=['|',' ',' ',' ','/',' ',' ',' ',' ','']
All1 = [A,B1,C1,D2,E2,F,G,B]

#Tries0
F1=['|',' ',' ',' ',' ','/',' ',' ','\\']
G1=['|',' ',' ',' ','/',' ',' ',' ',' ','\\']
All0 = [A,B1,C1,D2,E2,F1,G1,B]

Hangman = [All0,All1,All2,All3,All4,All5,All6,All7]

#Set word list
T = ('rock','scissors','paper','exclusive','maintenance')
used_letters =[]
 
#Welcome Screen
print("*"*20)
print("Hangman Game\n Welcome!")
print("*"*20)

#Select Mode
MultiPlayer = Mode_Select()

system('cls')
#Execute Mode
if MultiPlayer==True:
	score1 = 0
	score2 = 0
	#True if player1 - False if player2
	P = True
	while score1<3 and score2<3:
		print("*"*20)
		print("SCORE: \n Player 1: ",score1,"| Player 2: ",score2)
		print("*"*20)
		if P:
			cur_player = 1
			opponent = 2
		else:
			cur_player = 2
			opponent = 1
			
		print("Player",cur_player,"plays")
		print("Player",opponent, "press any key to select a word secretly")
		a = input()
		for i in range(len(T)):
			print(i+1,'.', T[i], end='  ')
		while True:
			secretWord = input("\nSelect a word: ")
			if int(secretWord):
				secretWord = T[int(secretWord)-1]
				break
		
		system('cls')
		
		Lsecret = []
		for i in secretWord:
			Lsecret.append(i)
		Lfound = ['_']* len(Lsecret)
		tries = 7
		#RUN THE GAME
		Lsecret, Lfound, tries = One_Round(Lsecret, Lfound, tries, Hangman)
		#WON/LOST CHECK
		Won_Lost = Won_Lost_Select(tries, Lfound, Lsecret, secretWord)
		if Won_Lost:
			if P:
				score1+=1
			if not P:
				score2+=1
		P = not P
		system('cls')
	#CHECK WHO WINS	
	print("*"*20)
	if score1 == 3:
		print("PLAYER 1 WINS THE GAME")
	if score2 == 3:
		print("PLAYER 2 WINS THE GAME")
	print("SCORE: \n Player1: ",score1,"| Player2: ",score2)
	
	

	
if MultiPlayer==False:
	tries = 7
	secretWord = choice(T)
	Lsecret = []
	for i in secretWord:
		Lsecret.append(i)
	Lfound = ['_']* len(Lsecret)
	#RUN THE GAME
	Lsecret, Lfound, tries = One_Round(Lsecret, Lfound, tries, Hangman)
	#WON/LOST CHECK
	Won_Lost_Select(tries, Lfound, Lsecret, secretWord)
	

	
'''
A=['-','-','-','-','-','-','-','-']
B=['|',' ',' ',' ',' ',' ',' ','|']
C=['|',' ',' ',' ',' ',' ','(',')']
D=['|',' ',' ',' ',' ','/','|','|','\\']
E=['|',' ',' ',' ','/',' ','|','|',' ','\\']
F=['|',' ',' ',' ',' ','/',' ',' ','\\']
G=['|',' ',' ',' ','/',' ',' ',' ',' ','\\']
H=['|']
'''
'''	
	----------
	|		 |
	|   	 ()
	| 		/||\
	| 	   / || \
	| 		/  \
	|  	   /    \
	|
'''
	
