from AlgoritmoProperties import AlgoritmoProperties

import time
import copy

class Branch_and_Bound(AlgoritmoProperties):
  def __init__(self):
    super().__init__()
    self.name = "Branch_and_Bound"

  def solveSudoku(self, sudoku):
    
    initialTime = time.time()
   
    #-------------------------------------------
    size = len(sudoku.unsolvedSudoku)
    
    sudoku.defineNodes()
    for n in sudoku.nodes:
      n.updatePossibleValues(sudoku)
      sudoku.defineNeighbors(n)
    
    def backtracking(currentNode, finished):
      if currentNode == None: 
        return
        
      if len(currentNode.possibleValues) == 0: 
        return
      
      for v in copy.deepcopy(currentNode.possibleValues):
        currentNode.setValue(v,sudoku)
        
        if sudoku.isSolved(): 
          finished[0] = True
          return
          
        l = currentNode.removeValueInNeighbors()
        backtracking(sudoku.nodeWithLessPossibleValues(), finished)
        
        if finished[0]: return
        
        currentNode.restoreValueInNeighbors(l)
        currentNode.setValue(-1, sudoku)
        

    
    backtracking(sudoku.nodeWithLessPossibleValues(), [False])
    #-------------------------------------------
    self.times[-1].append(time.time() - initialTime)
    self.averageTimes[-1][1] = sum(self.times[-1][1:])/len(self.times[-1][1:])

  def onePossibleValue(self, sudoku):

    for i in range(len(sudoku.nodes)):
      if len(sudoku.nodes[i].possibleValues) == 1:
        sudoku.nodes[i].setValue(sudoku.nodes[i].possibleValues[0],sudoku)
        sudoku.nodes[i].removeValueInNeighbors()
        sudoku.nodes.remove(sudoku.nodes[i])
        return True
    return False