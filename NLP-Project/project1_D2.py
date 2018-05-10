import csv
import os
import sys

def transitionF(currState, strIndex):
	transitionFile = csv.reader(open(os.path.join(dirName, "transitionTable.txt"), "r"))
	for row in transitionFile:
		if((row[0] == currState) and (row[1] == strIndex)):
			return row[2]
	return currState

def dRecognize(dirName, stringInput):
	startFile = open(os.path.join(dirName, "startState.txt"), "r")
	finalFile = open(os.path.join(dirName, "finalStates.txt"), "r")
	initialState = startFile.read() 
	currentState = initialState
	finalState = finalFile.readlines()

	for index in range(len(stringInput)+1): 
		for x in range(len(finalState)):
			if((currentState == finalState[x]) and (index != len(stringInput))):
				return 0
		if(index == len(stringInput)): 
			for x in range(len(finalState)):
				if(currentState == finalState[x]):
					return 1
			else:
				return 0
		elif(transitionF(currentState, stringInput[index]) == "NULL"):
			currentState = transitionF(initialState, stringInput[index])
		else:
				currentState = transitionF(currentState, stringInput[index])

dirName = sys.argv[1]
stringInput = sys.argv[2]

if(dRecognize(dirName, stringInput) == 1):
	print("MATCH")
else:
	print("REJECT")