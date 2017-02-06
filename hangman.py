import random

def hangman():
	x = random.randint(0, 7)
	myList = ["planet", "freeze", "tsunami", "island", "cappuccino", "elephant", "rocket", "earthquake"]
	word = myList[x]
	blank = "-"
	blankWord = blank*len(word)

	guessCount = 25

	while blankWord != word:
		print("Guess the", len(word), "letter word. You have", guessCount, "guess(es).")
		val = (input("Enter a letter or the word: "))
		guessCount = guessCount - 1
		if val == word:
			while True:
				try:
					print("You have guessed the word correctly in", (25 - guessCount), "guess(es)!")
					val1 = int(input("Play Again? (enter 1 is yes or enter 0 if no): "))
					break
				except ValueError:
					print("Invalid input. Please enter a different value.")

			while val1 != 0 and val1 != 1:
				val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

			if val1 == 1:
				hangman()

			if val1 == 0:
				quit()
		elif guessCount == 0:
			while True:
				try:
					print("You did not guess the word correctly! The word was", word + ".")
					val1 = int(input("Play Again? (enter 1 is yes or enter 0 if no): "))
					break
				except ValueError:
					print("Invalid input. Please enter a different value.")

			while val1 != 0 and val1 != 1:
				val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

			if val1 == 1:
				hangman()

			if val1 == 0:
				quit()
		else:
			counter = 0
			for x in range(len(word)):
				if val == word[x]:
					blankWord = blankWord[:x] + val + blankWord[x+1:]	
					counter = counter + 1
			if counter != 0:
				print("You guessed a letter correctly:", counter, val + ",", blankWord + ".")
			else:
				print("Incorrect guess: No", val + ",", blankWord + ".", "Try again.")	

	while True:
		try:
			print("You have guessed the word correctly in", (25 - guessCount), "guesses!")
			val1 = int(input("Play Again? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		hangman()

	if val1 == 0:
		quit()

hangman()