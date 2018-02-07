from collections import Counter
import operator

words = []
userLength = 0
userWord = ''
missedChars = 0
lettersGuessed = []
displayWord = []
lettersWithFreq = Counter()		

def main():
	global displayWord
	global words
	global lettersWithFreq	
	global userLength
	userLength = raw_input("Enter the length of the word: ")

	displayWord = [None] * int(userLength)

	with open("words.txt", 'r') as in_file:
		for line in in_file:
			line = line.rstrip("\n\r")
                        if (len(line) == int(userLength)):
				words.append(line)

	if(len(words) == 0):
		print "There are no words of that length, try again..."
		main()
	else:
		for word in words:
			x = Counter(word)
                	lettersWithFreq = lettersWithFreq + x	
			print word+ ", ",			
	
	selectWord()

	print "\n---THE GAME HAS BEGUN---"	
	
	initialGuess = autoGuess(words,0)
	startGame(initialGuess);
		

def startGame(guess):
	global lettersGuessed
	global missedChars
	global words
	global userWord

	lettersGuessed.append(guess)
	
	userAnswer = raw_input("Is " + guess + " in the word (y=yes/n=no): ")
	
	if (userAnswer == 'y' or userAnswer == 'Y'):
		print "Letters Guessed: ",
		print lettersGuessed
		printHangman(missedChars)
		editDisplayWord(guess)
		printDisplayWord()
		refineWords(guess, 1)
		if len(words) == 1:
			print "\n"	
			printHangman(missedChars)
			completeDisplayWord()
			printDisplayWord()
	elif(userAnswer == 'n' or userAnswer == 'N'):
		print "Letters Guessed: ",
		print lettersGuessed
		print "The letter " + guess + " is not in the word." 
		missedChars = missedChars + 1
		printHangman(missedChars)
		printDisplayWord()
		refineWords(guess, 0)
		if len(words) == 1:
			print "\n"	
			printHangman(missedChars)
			completeDisplayWord()
			printDisplayWord()
	else:
		startGame(guess)	



	if len(words) == 1:
		if userWord != words[0]:
			print "\n"
			print "ERROR: YOU MUST HAVE MADE A MISTAKE..."
			exit(0)
		print "\n\nTHE COMPUTER HAS FOUND YOUR WORD!"
		userWord = words[0]
		printHangman(missedChars)
		completeDisplayWord()
		printDisplayWord()
		exit(0)
	
	if None not in displayWord:
		print "\n\nTHE COMPUTER HAS FOUND YOUR WORD!"
		exit(0)
	
	print "\n\n\n"
	newGuess = autoGuess(words,0)
	startGame(newGuess)

def autoGuess(words, recur):
	global lettersWithFreq
	global lettersGuessed
	
	if len(words) == 0:
		print "ERROR: YOU LED ME IN THE WRONG DIRECTION... THANKS."
		exit(0)
		
	if recur == 0:
                lettersWithFreq = Counter()
                for word in words:
                        x = Counter(word)
                        lettersWithFreq = lettersWithFreq + x        

        letterTuple = max(lettersWithFreq.iteritems(), key=lambda x: x[1])
        maxFreqLetter = letterTuple[0]
        if maxFreqLetter in lettersGuessed:
                del lettersWithFreq[maxFreqLetter]
                return autoGuess(words, 1)
        else:
                print "GUESS: " + maxFreqLetter
                return maxFreqLetter

        return maxFreqLetter	

def guessWord(words):
	global displayWord
	
	newWords = []
	
	print "COMPARING POSITION OF LETTERS TO WORDS IN THE LIST..."
	print "NEW LIST FORMED..."
	
	for word in words:
		match = 0
		listWord = list(word)
		for x in range(0,len(displayWord)):
			if(displayWord[x] != None):
#				print displayWord[x],
#				print "==",
#				print listWord[x],
#				print "?"
				if(displayWord[x] == listWord[x]):
					match = 1
				else:
					match = 0
					break
		if match == 1:
			print word,
			newWords.append(word)	
	
	if(len(newWords) == 0):
		return words

	return newWords

	


def refineWords(letter, contains):
	global words
	global userLength
	newWords = []

	print "\n"
#	print "REMAINING WORDS: ",
	if contains == 1:
		for word in words:
			if letter in word:
				newWords.append(word)	
				#print word,
	else:
		for word in words:
			if letter not in word:
				newWords.append(word)	
				#print word,

	newWords = guessWord(newWords)
	
	words = newWords

def selectWord():
	global words
	global userWord
	userWord = raw_input("\n\nEnter a word from the list above: ")
    
	if userWord in words:
		print "\nYou have selected the word: " + userWord
	else:
		print "\nTry again"
		selectWord()


def printHangman(misses):
	if misses == 0:
		print "-----"
	if misses == 1:
		print "-----"
		print "  |  "
	if misses == 2:
		print "-----"
		print "  |  "
		print "  |  "
	if misses == 3:
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
	if misses == 4:
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print "  |  "
	if misses == 5:	
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print " /|  "
	if misses == 6:
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print " /|\ "
	if misses == 7:	
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print " /|\ "
		print "  |  "
	if misses == 8:	
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print " /|\ "
		print "  |  "
		print " /   "
	if misses == 9:
		print "-----"
		print "  |  "
		print "  |  "
		print " ( ) "
		print " /|\ "
		print "  |  "
		print " / \ "
		print "THE COMPUTER HAS LOST THE GAME, THE MAN HAS BEEN HANGED."
		exit(0)

def editDisplayWord(guess):
	global displayWord
	global userWord
	count = 0

	for char in userWord:
		if char == guess:
			displayWord[count] = guess
			count = count + 1
		else:
			count = count + 1

def printDisplayWord():
	global displayWord
	print "\n"
	for letter in displayWord:
		if letter == None:
			print "_",
		else:
			print letter,

def completeDisplayWord():
	global userWord
	wordLength = len(userWord)
	userWordList = list(userWord)

	for letter in userWordList:
		editDisplayWord(letter)

if __name__ == "__main__": main()
