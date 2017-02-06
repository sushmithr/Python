def hexConversion():
	while True:
		try:
			val = int(input("Enter a number: "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	if val < 0:    
		print ("Invalid input. Please re-enter value: ")
		hexConversion()

	hexList = ["A", "B", "C", "D", "E", "F"]

	x = int(val/16)
	if (val%16) < 10:
		i = val%16
	else:
		i = hexList[(val%16)-10]

	myList = []
	myList.append(i)
	counter = 1

	while x != 0:
		y = x
		x = int(x/16)
		if (y%16) < 10:
			i = y%16
		else:
			i = hexList[(y%16)-10]
		myList.append(i)
		counter = counter + 1

	print (val, "in hexadecimal is: ", end = "")

	for x in range(counter-1, -1, -1):
		print (myList[x], end = "")

	while True:
		try:
			val1 = int(input("\n" + "Would you like to check a different string to see if it is a palindrome? (enter 1 is yes or enter 0 if no): "))
			break
		except ValueError:
			print("Invalid input. Please enter a different value.")

	while val1 != 0 and val1 != 1:
		val1 = int(input("Invalid input. Please re-enter value (enter 1 if yes or enter 0 if no): "))

	if val1 == 1:
		hexConversion()

	if val1 == 0:
		quit()

hexConversion()
