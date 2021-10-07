import numpy as np
from copy import deepcopy
import sys
import datetime

def initialState(eachState):
  for row in eachState:
    for ch in row:
      print(ch, end =" ")
    print('')
  print('\n')

def getIndex(ch, currentState):
  return([(ix,iy) for ix, row in enumerate(currentState) for iy, i in enumerate(row) if i == ch])

def checkBlockOnSolution(currentState):
  blocks = getIndex("B", currentState)
  reached = 0
  for eachBlock in blocks:
    for eachSolution in solutionPlaces:
      if(eachBlock == eachSolution):
        reached = reached + 1
  if(reached == totalBlocks):
    global game
    game = 'stop'
    global goalState
    goalState = currentState
    return 'stop'


def checkValidMove(ch, p):
  parentArray = deepcopy(p)
  if(ch == "w"):
    robot = getIndex("R", parentArray)
    if(parentArray[robot[0][0] -1][robot[0][1]] == "0"):
      return []

    elif(parentArray[robot[0][0] -1][robot[0][1]] == " "):
      parentArray[robot[0][0] -1][robot[0][1]] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0] -1][robot[0][1]] == "S"):
      parentArray[robot[0][0] -1][robot[0][1]] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0] -1][robot[0][1]] == "B"):
      blocks = getIndex("B", parentArray)
      if(parentArray[robot[0][0] - 2][robot[0][1]] == "0" or parentArray[robot[0][0] - 2][robot[0][1]]  == "B"):
          return []

      elif(parentArray[robot[0][0] - 2][robot[0][1]]  == " " or parentArray[robot[0][0] - 2][robot[0][1]]  == "S"):
          parentArray[robot[0][0] - 2][robot[0][1]]  = "B"
          parentArray[robot[0][0] - 1][robot[0][1]]  = " "
          parentArray[robot[0][0] - 1][robot[0][1]] = "R"
          parentArray[robot[0][0]][robot[0][1]] = " "
          for eachSolution in solutionPlaces:
            if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
              parentArray[eachSolution[0]][eachSolution[1]] = "S"
          return parentArray

        
  elif(ch == "d"):
    robot = getIndex("R", parentArray)
    if(parentArray[robot[0][0]][robot[0][1] + 1] == "0"):
      return []
    elif(parentArray[robot[0][0]][robot[0][1] + 1] == " "):
      parentArray[robot[0][0]][robot[0][1] + 1] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0]][robot[0][1] + 1] == "S"):
      parentArray[robot[0][0]][robot[0][1] + 1] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0]][robot[0][1] + 1] == "B"):
      blocks = getIndex("R", parentArray)
      if(parentArray[robot[0][0]][robot[0][1] + 2] == "0" or parentArray[robot[0][0]][robot[0][1] + 2] == "B"):
          return []

      elif(parentArray[robot[0][0]][robot[0][1] + 2] == " " or parentArray[robot[0][0]][robot[0][1] + 2] == "S"):
          parentArray[robot[0][0]][robot[0][1] + 2] = "B"
          parentArray[robot[0][0]][robot[0][1] + 1] = " "
          parentArray[robot[0][0]][robot[0][1] + 1] = "R"
          parentArray[robot[0][0]][robot[0][1]] = " "
          for eachSolution in solutionPlaces:
            if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
              parentArray[eachSolution[0]][eachSolution[1]] = "S"
          return parentArray

  elif(ch == "s"):
    robot = getIndex("R", parentArray)
    if(parentArray[robot[0][0] + 1][robot[0][1]] == "0"):
      return []

    elif(parentArray[robot[0][0] + 1][robot[0][1]] == " "):
      parentArray[robot[0][0] + 1][robot[0][1]] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0] + 1][robot[0][1]] == "S"):
      parentArray[robot[0][0] +1][robot[0][1]] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray


    elif(parentArray[robot[0][0] + 1][robot[0][1]] == "B"):
      blocks = getIndex("R", parentArray)
      if(parentArray[robot[0][0] + 2][robot[0][1]] == "0" or parentArray[robot[0][0] + 2][robot[0][1]]  == "B"):
          return []
          
      elif(parentArray[robot[0][0] + 2][robot[0][1]]  == " " or parentArray[robot[0][0] + 2][robot[0][1]]  == "S"):
          parentArray[robot[0][0] + 2][robot[0][1]]  = "B"
          parentArray[robot[0][0] + 1][robot[0][1]]  = " "
          parentArray[robot[0][0] + 1][robot[0][1]] = "R"
          parentArray[robot[0][0]][robot[0][1]] = " "
          for eachSolution in solutionPlaces:
            if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
              parentArray[eachSolution[0]][eachSolution[1]] = "S"
          return parentArray

  elif(ch == "a"):
    robot = getIndex("R", parentArray)
    if(parentArray[robot[0][0]][robot[0][1] - 1] == "0"):
      return []

    elif(parentArray[robot[0][0]][robot[0][1] - 1] == " "):
      parentArray[robot[0][0]][robot[0][1] - 1] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0]][robot[0][1] - 1] == "S"):
      parentArray[robot[0][0]][robot[0][1] - 1] = "R"
      parentArray[robot[0][0]][robot[0][1]] = " "
      for eachSolution in solutionPlaces:
        if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
          parentArray[eachSolution[0]][eachSolution[1]] = "S"
      return parentArray

    elif(parentArray[robot[0][0]][robot[0][1] - 1] == "B"):
      blocks = getIndex("R", parentArray)
      if(parentArray[robot[0][0]][robot[0][1] - 2] == "0" or parentArray[robot[0][0]][robot[0][1] - 2] == "B"):
          return []
          
      elif(parentArray[robot[0][0]][robot[0][1] - 2] == " " or parentArray[robot[0][0]][robot[0][1] - 2] == "S"):
          parentArray[robot[0][0]][robot[0][1] - 2] = "B"
          parentArray[robot[0][0]][robot[0][1] - 1] = " "
          parentArray[robot[0][0]][robot[0][1] - 1] = "R"
          parentArray[robot[0][0]][robot[0][1]] = " "
          for eachSolution in solutionPlaces:
            if(parentArray[eachSolution[0]][eachSolution[1]] == " "):
              parentArray[eachSolution[0]][eachSolution[1]] = "S"
          return parentArray

def generateChildrenOfParent(a):
  temp = deepcopy(a)
  directions = ['a','w','d','s']
  allChildren = []
  global dfsQueue
  dfsQueue.remove(temp)
  for eachDirection in directions:
    returnedArray = []
    returnedArray = checkValidMove(eachDirection,temp)
    global childrenFound
    if(len(returnedArray) != 0 and (str(returnedArray) not in finalTree) and (returnedArray not in childrenFound)):
      if(checkBlockOnSolution(returnedArray) == 'stop'):
        childrenFound.append(returnedArray)
        allChildren.append(returnedArray)
        dfsQueue = []
      else:
        childrenFound.append(returnedArray)
        allChildren.append(returnedArray)
        dfsQueue.insert(0,returnedArray)
  finalTree[str(a)] = allChildren
    

def getParent(childState):
  for eachKey in finalTree:
    if(childState in finalTree[eachKey]):
      global finalTrace
      finalTrace.append(eval(eachKey))

startTime = datetime.datetime.now()
firstArray = [['0','0','0','0','0','0','0','0'],['0',' ',' ',' ','0','R',' ','0'],['0',' ',' ',' ',' ','B',' ','0'],['0',' ',' ',' ','0',' ',' ','0'],['0','0','0','0','0','B','S','0'],[' ',' ',' ',' ','0',' ','S','0'], [' ',' ',' ',' ','0','0','0','0']]
# firstArray = [['0','0','0','0','0'],['0',' ','R',' ','0'],['0',' ','B','S','0'],['0','0','0','0','0']]

solutionPlaces = getIndex("S",firstArray)
totalBlocks = len(getIndex("B", firstArray))
finalTree = {}
finalTrace = []
childrenFound = []
dfsQueue = []
dfsQueue.append(firstArray)

val = ''
visitedKeys = []
visitedKeys.append(firstArray)

game = ''
goalState = []
recentParent = str(firstArray)

print("The initial state is :")
initialState(firstArray)
expandedNodes = 0
while len(dfsQueue) != 0:
  expandedNodes = expandedNodes + 1
  generateChildrenOfParent(dfsQueue[0])
    
if game == 'stop':
  endTime = datetime.datetime.now()
  print(endTime - startTime)
  print("The number of expanded nodes is: ", expandedNodes)
  finalTrace.append(goalState)
  while finalTrace[-1] != firstArray:
    getParent(finalTrace[-1])
  finalTrace.reverse()
  print("The number of steps it takes is ", len(finalTrace) - 1, "and the path is:")
  for eachState in finalTrace:
    initialState(eachState)
    
else:
  print("No goal state")
