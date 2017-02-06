def palindromeCheck():
	val = (input("Enter a string to check if it is a palindrome: "))
	oldString = []
	newString = []

	for x in range(len(val)):
		oldString.append(val[x])

	for x in range(len(val) - 1, -1, -1):
		newString.append(oldString[x])

	newVal = newString[0]

	for x in range(1, len(val), 1):
		newVal = newVal + newString[x]

	if newVal == val:
		print(val, "is a palindrome: True")
	else:
		print(val, "is a palindrome: False")

	while True:
		try:
			val1 = int(input("Would you like to check a different string to see if it is a palindrome? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		palindromeCheck()

	if val1 == 0:
		quit()

palindromeCheck()