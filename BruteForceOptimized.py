from AlgoritmoProperties import AlgoritmoProperties
import time
from Node import Node

class BruteForceOptimized(AlgoritmoProperties):
  def __init__(self):
    super().__init__()
    self.name = "BruteForceOptimized"

  def solveSudoku(self, sudoku):
    initialTime = time.time()
    #------------------------------------

    n = len(sudoku.unsolvedSudoku)
    
    sudoku.defineNodes()

    for n in sudoku.nodes:
      n.updatePossibleValues(sudoku)

    def recursiveFunc(i=0):
      if i >= len(sudoku.nodes): return
        
      for v in sudoku.nodes[i].possibleValues:
        if sudoku.isSolved() or i >= len(sudoku.nodes): return
        sudoku.nodes[i].setValue(v, sudoku)
        recursiveFunc(i + 1)

    recursiveFunc()

    #------------------------------------
    self.times[-1].append(time.time() - initialTime)
    self.averageTimes[-1][1] = sum(self.times[-1][1:])/len(self.times[-1][1:])