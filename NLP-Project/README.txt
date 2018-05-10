Sushmith Ramesh
CSC470-02
Project 1
Due: September 27, 2016

FSA Recognizer:

Within the compressed tar.gz file, you should find a project1 folder that contains three source code files(project1_D1, project1_D2, and project1_D3) as well as this current README.txt file. The three source code files implement the respective delivery requirements as follows:

project1_D1: basic D-recognize program that accepts a language machine and matches or rejects given string inputs accordingly
project1_D2: same functionality as project1_D1, however, has the additional capability of recognizing string input matches even if the match is not necessarily at the beginning of the input
project1_D3: same functionality as project1_D2, however, has the additional capability of recognizing input matches even if more characters are present after the matched string

There should also be two folders in addition to the three source code files. One should be named sheepLanguageMachine and the other one should be name cowLanguageMachine. Within each of these two files, there should five text files(alphabet.txt, finalStates.txt, startState.txt, states.txt, and transitionTable.txt)

The cowLanguageMachine folder correlates to a specific test machine different from the given sheepLanguageMachine. It is structured as follows:
Finite set of N states: Q = {q0, q1, q2, q3}
Finite set of input alphabet: Σ = {m, o, !}
Start state: S = {q0}
Set of final states: F = {q3}
Transition function: F(q, i) -> q, where F is the transtion function that takes q(element of set Q) and i(element of set Σ) as input and returns q(element of set Q)[Q x Σ -> Q]

Different language machines can be created and passed as test machines, alongside different test string inputs, to the different source codes as long as build conventions are followed. To create a test machine, create a folder with a specified name and create five text files within the folder with the following names and contents:

states.txt: each line contains a different state of the machine (all states should be included within the file)
alphabet.txt: each line contains a character of the possible input alphabet 
startState.txt: one-line file that contains the start state
finalStates.txt: each line contains a different final/accepting state (all final state should be included within the file)
transitionTable.txt: each line contains "stateID1","inputSymbol","stateID2", where for a given state("stateID1") and given input symbol("inputSymbol") the machine transitions to another state("stateID2"). If there is no possible transition from a given state, then "NULL" is used as the next state and it is also possible for the machine to stay in the same state it started in.

To execute this code open the terminal and move to the location of the project1 folder from the compressed tar.gz file. Once you are in the project1 folder, type the following command in the terminal:

python sourceCodeName.py languageMachineName stringInput

EX.
python project1_D1.py sheepLanguageMachine baaa!