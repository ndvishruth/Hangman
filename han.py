import random 
from demo import diagram


def play_again():
	choice=input('Do you want to play again? Yes(Y)/No(N)\n').lower()
	if choice=='y' or choice=='yes':
		hangman()
	else:
		pass

def get_word():
	my_file=open('word.txt','r')
	line=my_file.readline()
	words=line.split()
	return random.choice(words)

def hangman():
	word = get_word()
	print('Word contains',len(word),'characters') 
	print("Guess the characters") 

	guesses = '' 
	turns = 10
	while turns > 0: 
		failed = 0
		for char in word: 
			if char in guesses: 
				print(char,end='') 			
			else: 
				print(" _",end='') 
				failed += 1
		if failed == 0: 
			print("The word is: ", word) 
			break
		print()
		guess = input("guess a character: ") 
		guesses += guess 

		if guess not in word: 
			
			turns -= 1
			print("Wrong") 
			print("You have", + turns, 'more guesses')
						
		diagram(turns) 

	play_again()



if __name__ == '__main__':
	hangman()