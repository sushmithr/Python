def factorial():
	while True:
		try:
			val = int(input("Enter a number: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")
	i = val - 1

	if val < 0 or val > 100:    
		print ("Invalid input. Please re-enter factorial value: ")
		factorial()
	elif val == 0:
		print("The factorial is 1")

		while True:
			try:
				val1 = int(input("Would you like to calculate another factorial? (enter 1 if yes or enter 0 if no): "))
				break
			except ValueError:
				print("Invalid input. Please enter a different value.")

		while val1 != 0 and val1 != 1:
			val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

		if val1 == 1:
			factorial()

		if val1 == 0:
			quit()
	else: 
		while i >= 1:
			val = val * i
			i = i - 1
		print ("The factorial is {val}".format(val = val)) 

		while True:
			try:
				val1 = int(input("Would you like to calculate another factorial? (enter 1 if yes or enter 0 if no): "))
				break
			except ValueError:
				print("Invalid input. Please enter a different value.")

		while val1 != 0 and val1 != 1:
			val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

		if val1 == 1:
			factorial()

		if val1 == 0:
			quit()

factorial()