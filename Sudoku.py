import math
import random
import os
import copy
import time
import sys

class Node:

  def __init__(self, v, r, c):
    self.v = v
    self.r = r
    self.c = c
    self.possibleValues = dict()
    self.neighborNodes = list()

  def setValue(self, v, sudoku):
    self.v = v
    sudoku[self.r][self.c] = self.v



class Sudoku:

  def __init__(self):
    self.record = []
    self.iterations = 0

  """
  1. n is a product of a square? If it is not, it stops.
  2. We define a set with all the possible numbers in sudoku. That is, in a 9x9 sudoku the numbers are from 1 to 9.
  3. We define 3 lists that will contain sets. The first will contain the sets of the elements of each row.
  That is, list[0] will contain all the elements of row index 0. The second list will contain all
  the sets with the elements in each column and the third will contain all the sets with the elements in each square.
  This means that for each list there are n number of sets.
  
  4. We iterate n times and add a row.
    5. We iterate n times and calculate the union of the sets corresponding to the row, column and square in which we are.
    We calculate the difference of the sets of all possible numbers - the union and this returns us the possible numbers in that
    row, column and square.
    6. We choose a random number from that list and add it to the sudoku and to their respective sets of said column, row and square.
  
  7. It is possible that this algorithm does not generate sudokus on the first attempt, since it is possible that in step 5,
  the set with the possible numbers does not have elements, having a possible index error. So from step 2 onwards it has to
  be inside a While true and a try except.
  """

  def generateSudokuSolved(self, n):

    initialTime = time.time()
    self.iterations = 0
    nsqrt = math.sqrt(n)
    if not nsqrt.is_integer(): return
    nsqrt = int(nsqrt)

    while True:
      try:
        sudoku = []
        numbers = set(range(1, n + 1))
        rowsSets = [set() for i in range(n)]
        columnsSets = [set() for i in range(n)]
        squaresSets = [set() for i in range(n)]

        for row in range(n):
          sudoku.append(list())
          # os.system('cls' if os.name == 'nt' else 'clear')
          # for j in range(len(sudoku)):
          #     print(sudoku[j])
          for column in range(n):
            #if row = 4 and column = 7 and sudoku is 9x9
            #sqrRowIndex = 4 - (4 % 3) = 3
            #sqrColumnIndex = 7 - (7 % 3) = 6
            #sqrRowIndex/3 + sqrColumnIndex is the square index in the squaresSets list
            sqrRowIndex = row - int((row % nsqrt))
            sqrColumnIndex = column - int((column % nsqrt))

            possibleElements = list(
                numbers - rowsSets[row].union(columnsSets[column]).union(
                    squaresSets[sqrRowIndex + int(sqrColumnIndex / 3)]))

            element = random.choice(possibleElements)
            rowsSets[row].add(element)
            columnsSets[column].add(element)
            squaresSets[sqrRowIndex + int(sqrColumnIndex / 3)].add(element)
            sudoku[row].append(element)
            self.iterations += 1
      except Exception as e:
        # os.system('cls' if os.name == 'nt' else 'clear')
        continue

      # os.system('cls' if os.name == 'nt' else 'clear')

      finalTime = time.time()
      self.record.append((("Iteraciones", self.iterations),("Time in seconds",finalTime - initialTime), "Generate Sudoku Solved"))
      self.iterations = 0
      return sudoku

  """1.Pick n random positions and delete them. In this context, clear is simply changing by -1."""
  def dissolveSudoku(self, sudoku, n):
    unsolvedSudoku = copy.deepcopy(sudoku)
    for i in range(n):
      unsolvedSudoku[random.randint(0,len(unsolvedSudoku) - 1)][random.randint(0,len(unsolvedSudoku[0]) - 1)] = -1
    return unsolvedSudoku

  """Check if a specific cell is correct"""
  def checkPosition(self, sudoku, row, column):
    n = len(sudoku)

    def checkColumn(sudoku, column):
      frequency = {}
      for i in range(n):
        self.iterations += 1
        if sudoku[i][column] in frequency or sudoku[i][column] == -1:
          return False
        else:
          frequency[sudoku[i][column]] = 1
      return True

    def checkRow(sudoku, row):
      frequency = {}
      for i in range(n):
        self.iterations += 1
        if sudoku[row][i] in frequency or sudoku[row][i] == -1:
          return False
        else:
          frequency[sudoku[row][i]] = 1
      return True

    def checkSquare(sudoku, row, column):
      nsqrt = int(math.sqrt(len(sudoku)))
      sqrRowIndex = row - int((row % nsqrt))
      sqrColumnIndex = column - int((column % nsqrt))

      frequency = {}
      for i in range(nsqrt):
        for j in range(nsqrt):
          self.iterations += 1
          if sudoku[sqrRowIndex + i][sqrColumnIndex + j] in frequency or sudoku[sqrRowIndex + i][sqrColumnIndex + j] == -1:
            return False
          else:
            frequency[sudoku[sqrRowIndex + i][sqrColumnIndex + j]] = 1
      return True

    return checkColumn(sudoku, column) and checkRow(
        sudoku, row) and checkSquare(sudoku, row, column)

  """Iterate over all the cells that started empty and check if they are correct"""
  def isSolved(self, sudoku, nodes):
    return all(self.checkPosition(sudoku, nodes[i].r, nodes[i].c) for i in range(len(nodes)))



  """calculates the possible values that a node can take according to its neighbors in its row, column and square"""
  def calculatePossibleValues(self, node, sudoku):
    n = len(sudoku)
    
    possibleValues = set(i for i in range(1,n+1))
    for i in range(n):
      possibleValues.discard(sudoku[node.r][i])
      possibleValues.discard(sudoku[i][node.c])
      self.iterations += 1


    nsqrt = int(math.sqrt(len(sudoku)))
    sqrRowIndex = node.r - int((node.r % nsqrt))
    sqrColumnIndex = node.c - int((node.c % nsqrt))

    for i in range(nsqrt):
      for j in range(nsqrt):
        possibleValues.discard(sudoku[sqrRowIndex + i][sqrColumnIndex + j])
        self.iterations += 1

    node.possibleValues = {k:v for k, v in enumerate(possibleValues)}

  """The neighbors of a node are all those cells that started empty from the beginning."""
  def calculateNeighborNodes(self, node, nodes, sudoku):
    n = len(sudoku)
    nsqrt = int(math.sqrt(len(sudoku)))

    nodeSqrIndex = (node.r - int((node.r % nsqrt)), node.c - int((node.c % nsqrt)))
    
    for n in nodes:
      nSqrIndex = (n.r - int((n.r % nsqrt)), n.c - int((n.c % nsqrt)))
      if n.r == node.r or n.c == node.c or nodeSqrIndex == nSqrIndex:
        node.neighborNodes.append(n)
      self.iterations += 1

  """The next value of a node is the next value in its dictionary of possible values"""
  def setNodeNextValue(self, node, sudoku):
    if node.v == -1:
      node.setValue(node.possibleValues[0], sudoku)
    
    #print(node.possibleValues, node.r, node.c)
    keyNode = None
    for k,v in node.possibleValues.items():
      if v == node.v:
        keyNode = k
        break
      self.iterations += 1

    index = keyNode + 1 if keyNode + 1 < len(node.possibleValues) else 0

    node.setValue(node.possibleValues[index], sudoku)
    
  """This method uses brute force to find the solution to Sudoku. What it does is
  that it tries all the possible combinations but before starting, it calculates the possible
  numbers that there may be for each cell. So with this technique you can reduce many possible
  combinations. Even so, it is not efficient since it is still brute force and for a very
  large number of empty cells, the time complexity is still very high."""
  def solveWithForceBrute1(self, sudoku):

    initialTime = time.time()
    n = len(sudoku)

    
    nodes = []
    for row in range(n):
      for column in range(n):
        if (sudoku[row][column] == -1):
          nodes.append(Node(-1, row, column))
          #sudoku[row][column] = 1
        self.iterations += 1

    for n in nodes:
      self.calculatePossibleValues(n, sudoku)
      self.calculateNeighborNodes(n, nodes, sudoku)

    def recursiveFunc(nodes, i=0):
      if i >= len(nodes): return
      # os.system('cls' if os.name == 'nt' else 'clear')
      # for l in sudoku:
      #   print(l)
      #print(nodes[i].possibleValues)
      for j in range(len(nodes[i].possibleValues)):
        if self.isSolved(sudoku, nodes) or i >= len(nodes): return
        #nodes[i].setValue(nodes[i].possibleValues[j], sudoku)
        self.setNodeNextValue(nodes[i], sudoku)
        recursiveFunc(nodes, i + 1)
        self.iterations += 1

    recursiveFunc(nodes)
    # os.system('cls' if os.name == 'nt' else 'clear')
    finalTime = time.time()
    self.record.append((("iterations", self.iterations),("Time in seconds", finalTime - initialTime), "Solve sudoku")) 
    self.iterations = 0

  
  
  """This method uses brute force to find the solution to Sudoku. What it does
  is that it tries all possible combinations for each empty cell. This is not
  efficient since even for up to 6 empty cells it can take more than 10 seconds."""
  def solveWithForceBrute(self, sudoku):

    initialTime = time.time()
    n = len(sudoku)

    #saves a list with all the cells that started empty
    nodes = []
    for row in range(n):
      for column in range(n):
        if (sudoku[row][column] == -1):
          nodes.append(Node(1, row, column))
          sudoku[row][column] = 1
        self.iterations += 1

    def recursiveFunc(nodes, i=0):

      # os.system('cls' if os.name == 'nt' else 'clear')
      # for l in sudoku:
      #   print(l)

      for j in range(n):
        if self.isSolved(sudoku, nodes) or i >= len(nodes): return
        nodes[i].setValue(j + 1, sudoku)
        recursiveFunc(nodes, i + 1)
        self.iterations += 1

    recursiveFunc(nodes)
    # os.system('cls' if os.name == 'nt' else 'clear')
    finalTime = time.time()
    self.record.append((("iterations", self.iterations),("Time in seconds", finalTime - initialTime), "Solve sudoku")) 
    self.iterations = 0



def delete_last_line():
  sys.stdout.write("\033[F")  
  sys.stdout.write("\033[K") 

"""In this class, tests are done on solving sudokus and calculating average times."""
class AlgorithmTests:
  def __init__(self, sudokuSize, emptyCells, numberOfMaxTests):
    self.sudoku = Sudoku()
    self.iterationsAverage = 0
    self.timeAverage = 0
    self.sudokuSize = sudokuSize
    self.emptyCells = emptyCells
    self.currentAlgorithm = ""
    self.numberOfMaxTests = numberOfMaxTests
    self.numberOfTests = 0
    self.limitTime = 2

  def resetValues(self):
    self.iterationsAverage = 0
    self.timeAverage = 0
    self.currentAlgorithm = ""
    self.numberOfTests = 0
  
  def testForceBrute(self):
    self.resetValues()
    print("\n")
    self.currentAlgorithm = "Force Brute"
    sumIterationsSolveSudoku = 0
    sumTimeSolveSudoku = 0
    
    for j in range(self.numberOfMaxTests):
      
      delete_last_line()
      print("Intento:",j+1, "Empty spaces:", self.emptyCells)
      
      sudokuSolved = self.sudoku.generateSudokuSolved(self.sudokuSize)
      
      unsolvedSudoku = self.sudoku.dissolveSudoku(sudokuSolved, self.emptyCells)
      self.sudoku.solveWithForceBrute(unsolvedSudoku)
      sumIterationsSolveSudoku += self.sudoku.record[-1][0][1]
      sumTimeSolveSudoku += self.sudoku.record[-1][1][1]
      self.numberOfTests += 1
      if(self.sudoku.record[-1][1][1] > self.limitTime):
        #print("Force Brute: Sudoku 9x9 with 5 empty spaces took more than 5 seconds")
        break

    delete_last_line()
    self.iterationsAverage = sumIterationsSolveSudoku/self.numberOfTests
    self.timeAverage = sumTimeSolveSudoku/self.numberOfTests

  def testForceBrute1(self):
    self.resetValues()
    print("\n")
    self.currentAlgorithm = "Force Brute 1"
    sumIterationsSolveSudoku = 0
    sumTimeSolveSudoku = 0

    for j in range(self.numberOfMaxTests):
      delete_last_line()
      print("Intento:",j+1, "Empty spaces:", self.emptyCells)

      sudokuSolved = self.sudoku.generateSudokuSolved(self.sudokuSize)
      
      unsolvedSudoku = self.sudoku.dissolveSudoku(sudokuSolved, self.emptyCells)
      self.sudoku.solveWithForceBrute1(unsolvedSudoku)
      sumIterationsSolveSudoku += self.sudoku.record[-1][0][1]
      sumTimeSolveSudoku += self.sudoku.record[-1][1][1]
      self.numberOfTests += 1
      if(self.sudoku.record[-1][1][1] > self.limitTime):
        #print("Force Brute 1: Sudoku 9x9 with 5 empty spaces took more than 5 seconds")
        break

    delete_last_line()
    self.iterationsAverage = sumIterationsSolveSudoku/self.numberOfTests
    self.timeAverage = sumTimeSolveSudoku/self.numberOfTests

  def information(self):
    s = ""
    s += self.currentAlgorithm + "\n"
    s += "Sudoku Size: " + str(self.sudokuSize) + "\n"
    s += "Empty Cells: " + str(self.emptyCells) + "\n"
    s += "Iterations Average: " + str(self.iterationsAverage) + "\n"
    s += "Time Average: " + str(self.timeAverage) + "\n"
    s += "Solved Sudokus: " + str(self.numberOfTests) + "\n"
    return s
    

    

def main():
 
  rangeEmptyCells = 40
  
  for i in range(1, rangeEmptyCells+1):
    forceBrute = AlgorithmTests(9,i,100)
    forceBrute.testForceBrute()
    print(forceBrute.information())
    if(forceBrute.timeAverage > 2): break

  for i in range(1,rangeEmptyCells+1):
    forceBrute1 = AlgorithmTests(9,i,100)
    forceBrute1.testForceBrute1()
    print(forceBrute1.information())
    if(forceBrute1.timeAverage > 2): break
    
main()
