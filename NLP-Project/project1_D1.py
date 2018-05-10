import csv
import os
import sys

def transitionF(currState, strIndex):
	transitionFile = csv.reader(open(os.path.join(dirName, "transitionTable.txt"), "r"))
	for row in transitionFile:
		if((row[0] == currState) and (row[1] == strIndex)):
			return row[2]

def dRecognize(dirName, stringInput):
	startFile = open(os.path.join(dirName, "startState.txt"), "r")
	finalFile = open(os.path.join(dirName, "finalStates.txt"), "r")
	currentState = startFile.read() 
	finalState = finalFile.readlines()

	for index in range(len(stringInput)+1): 
		if(index == len(stringInput)): 
			for x in range(len(finalState)):
				if(currentState == finalState[x]):
					return 1
			return 0
		elif(transitionF(currentState, stringInput[index]) == "NULL"):
			return 0
		else:
			currentState = transitionF(currentState, stringInput[index])

dirName = sys.argv[1]
stringInput = sys.argv[2]

if(dRecognize(dirName, stringInput) == 1):
	print("MATCH")
else:
	print("REJECT")