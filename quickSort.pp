import random

def partition(myList, pleft, pright):
	j = pleft
	t = pright
	pivot = myList[j]

	while j < t: 
		if myList[j+1] <= pivot: 
			temp = myList[j+1]
			myList[j+1] = myList[j]
			myList[j] = temp
			j = j+1
		else: 
			temp = myList[j+1]
			myList[j+1] = myList[t]
			myList[t] = temp
			t = t-1

	return j

def quickSort(myList, left, right):
	if (right-left) < 1:
		return

	j = partition(myList, left, right)

	quickSort(myList, left, j-1)
	quickSort(myList, j+1, right)

def main():
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

	quickSort(numList, 0, numCount-1)

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
		main()

	if val1 == 0:
		quit()

main()