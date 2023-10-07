from AlgoritmoProperties import AlgoritmoProperties
from Node import Node


import time


class BruteForce(AlgoritmoProperties):
  def __init__(self):
    super().__init__()
    self.name = "BruteForce"
    

  def solveSudoku(self, sudoku):
    initialTime = time.time()
    #-----------------------------

    n = len(sudoku.unsolvedSudoku)

    sudoku.defineNodes()
        
    def recursiveFunc(nodes, i=0):
      for j in range(n):
        if sudoku.isSolved() or i >= len(sudoku.nodes): return
        sudoku.nodes[i].setValue(j + 1, sudoku)
        recursiveFunc(nodes, i + 1)

    
    recursiveFunc(sudoku.nodes)
    
    #-----------------------------
    self.times[-1].append(time.time() - initialTime)
    self.averageTimes[-1][1] = sum(self.times[-1][1:])/len(self.times[-1][1:])