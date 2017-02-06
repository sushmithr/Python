def fibonacci():
	while True:
		try:
			val = int(input("Enter the number of values you would like to see from the fibonacci sequence: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	if val < 0 or val > 100:    
		print ("Invalid input. Please re-enter value: ")
		fibonacci()
	else:
		if val == 1:
			print ("The fibonacci sequence is: ")
			print ("0")

			while True:
				try:
					val1 = int(input("Would you like to see more or less of the fibonacci sequence? (enter 1 if yes or enter 0 if no): "))
					break
				except ValueError:
					print("Invalid input. Please enter a different value.")

			while val1 != 0 and val1 != 1:
				val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

			if val1 == 1:
				fibonacci()

			if val1 == 0:
				quit()
		else:
			print ("The fibonacci sequence is: ")
			print ("0")
			for x in range(1, val):
				print (fibonacci1(x))

			while True:
				try:
					val1 = int(input("Would you like to see more or less of the fibonacci sequence? (enter 1 if yes or enter 0 if no): "))
					break
				except ValueError:
					print("Invalid input. Please enter a different value.")

			while val1 != 0 and val1 != 1:
				val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

			if val1 == 1:
				fibonacci()

			if val1 == 0:
				quit()

def fibonacci1(x):
	a = 1
	b = 1
	for i in range(x-1):
		c = a + b
		a = b
		b = c
	return a

fibonacci()

