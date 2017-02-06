import random

def sortNum():
	while True:
		try:
			val = int(input("Enter the number of values you would like to sort: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	numList = []
	numCount = 0
	while numCount < val:
		x = random.randint(0, 100)
		numList.append(x)
		numCount = numCount + 1

	while True:
		try:
			val1 = int(input("Would you like to sort in ascending or descending order? (enter 1 if ascending or enter 0 if descending): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		for x in range(val + 1):
			for x in range(val - 1):
				if numList[x] > numList[x + 1]:
					temp = numList[x + 1]
					numList[x + 1] = numList[x]
					numList[x] = temp

	if val1 == 0:
		for x in range(val + 1):
			for x in range(val - 1):
				if numList[x] < numList[x + 1]:
					temp = numList[x + 1]
					numList[x + 1] = numList[x]
					numList[x] = temp

	print("Sorted values:")
	for x in range(val):
		print(numList[x])

	while True:
		try:
			val1 = int(input("Would you like to sort a different set of values? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		sortNum()

	if val1 == 0:
		quit()

sortNum()
