import random

def randomNum():
	x = random.randint(0, 100)
	while True:
		try:
			val = int(input("Guess a number: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val != x:
		if val < x:
			val = int(input("Too low. Guess again: "))
		if val > x:
			val = int(input("Too high. Guess again: "))

	while True:
		try:
			val1 = int(input("You guessed correctly! Play again? (enter 1 if yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		randomNum()

	if val1 == 0:
		quit()

randomNum()