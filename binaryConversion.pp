def binaryConversion():
	while True:
		try:
			val = int(input("Enter a number: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	if val < 0:    
		print ("Invalid input. Please re-enter value: ")
		binaryConversion()

	x = int(val/2)
	i = val%2

	myList = []
	myList.append(i)
	counter = 1

	while x != 0:
		y = x
		x = int(x/2)
		i = y%2
		myList.append(i)
		counter = counter + 1

	print (val, "in binary is: ", end = "")

	for x in range(counter-1, -1, -1):
		print (myList[x], end = "")

	while True:
		try:
			val1 = int(input("\n" + "Would you like to convert another deciaml value to binary? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		binaryConversion()

	if val1 == 0:
		quit()

binaryConversion()



