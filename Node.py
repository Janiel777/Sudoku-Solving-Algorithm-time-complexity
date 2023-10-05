import math

class Node:

  def __init__(self, v, r, c):
    self.v = v
    self.r = r
    self.c = c
    self.possibleValues = []
    self.neighbors = list()

  def setValue(self, v, sudoku):
    self.v = v
    sudoku.unsolvedSudoku[self.r][self.c] = self.v

  def updatePossibleValues(self, sudoku):
    n = len(sudoku.unsolvedSudoku)
    
    possibleValues = set(i for i in range(1,n+1))
    for i in range(n):
      possibleValues.discard(sudoku.unsolvedSudoku[self.r][i])
      possibleValues.discard(sudoku.unsolvedSudoku[i][self.c])
      
    nsqrt = int(math.sqrt(n))
    sqrRowIndex = self.r - int((self.r % nsqrt))
    sqrColumnIndex = self.c - int((self.c % nsqrt))

    for i in range(nsqrt):
      for j in range(nsqrt):
        possibleValues.discard(sudoku.unsolvedSudoku[sqrRowIndex + i][sqrColumnIndex + j])

    self.possibleValues = list(possibleValues)

  def updateNeighborsPossiblesValues(self):
    for neighbor in self.neighbors:
      neighbor.possibleValues.remove(self.v)