def reverseString():
	val = (input("Enter a string you would like to reverse: "))
	oldString = []
	newString = []

	for x in range(len(val)):
		oldString.append(val[x])

	for x in range(len(val) - 1, -1, -1):
		newString.append(oldString[x])

	print("Reversed string: ", end = "")

	for x in range(len(val)):
		print(newString[x], end = "")

	while True:
		try:
			val1 = int(input("\n" + "Would you like to reverse a different string? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		reverseString()

	if val1 == 0:
		quit()

reverseString()