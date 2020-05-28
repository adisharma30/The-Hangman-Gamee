import json
import random 




class Hangman:
	"""docstring for Hangman"""
	def __init__(self):
		super(Hangman, self).__init__()
		pass		

	def hangman_figure(self):
		if self.chance==9:
			print("You have been spared once!")

		elif self.chance==8:
			print("You won't be spared from now on")
			print("8 turns left")
			print("     O     ")

		elif self.chance==7:
			print("     O     ")
			print("     |     ")
			print("7 turns left")

		elif self.chance==6:
			print("     O     ")
			print("     |     ")
			print("    /     ")
			print("6 turns left")

		elif self.chance==5:
			print("     O     ")
			print("     |     ")
			print("    / \     ")
			print("5 turns left")
		elif self.chance==4:
			print("     O     ")
			print("     |     ")
			print("    / \     ")
			print("4 turns left")
		elif self.chance==3:
			print("   \ O /    ")
			print("     |     ")
			print("    / \     ")
			print("3 turns left")
		elif self.chance==2:
			print("   \ O_/    ")
			print("     |     ")
			print("    / \     ")
			print("2 turns left")
		elif self.chance==1:
			print("   \ O_|/    ")
			print("     |     ")
			print("    / \     ")
			print("1 turns left")
			print("Don't let the innocent man die")
		elif self.chance==0:
			print("     O_|    ")
			print("    /|\     ")
			print("    / \     ")
			print("You could not save the innocent man,GAME OVER!!")

	def Word_list(self):

		result=random.choice(['formally',"pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable",'immutable','invinsible','monster','vampire','memories','disaster','india','consistent','office','friends'])
		self.word_len=len(result)
		self.word_store=list(result)
				
	def main_game(self):
		#print('The word is %s long'%Word_list.list_result_len)
		spaces=[]
		self.chance=10
		print("These are the total blanks in the word")
		for space in range(0,self.word_len):

			spaces.append('_ ')
			print(spaces[space],end=" ")
			
		
		for x in range(0,25):
			choose =input('\nKindly choose a letter that you think this word contains :\n')
			if choose in self.word_store:
				position=self.word_store.index(choose)
				spaces[position]= choose
				while True:
					try:
						position2=self.word_store.index(choose,position+1)
					except ValueError:
						break
					else:
						spaces[position2]=choose
						break

				for y in range(0,self.word_len):
					print(spaces[y],end=" ")
				if self.word_store==spaces:
					print("\nCONGRATULATIONS! You have saved the innocent man's life\n")
					break
				else:		
					print("\nGreat!! This letter is present in the word, Keep Going\n")

			else:
				self.chance=self.chance-1				
				print("Sorry this letter does not exist in the word")			
				self.hangman_figure()
				if self.chance==0:
					break


name=input('Hi! Kindly enter your name : \n' )
print(" Welcome to the hangman game:- %s"%name.upper())
print("\nYou have to save the man's LIFE before he gets hang,All the Best!\n")
hg = Hangman()
hg.Word_list()
get=hg.main_game()








