from BruteForce import BruteForce
from BruteForceOptimized import BruteForceOptimized
from Branch_and_Bound import Branch_and_Bound
from Sudoku import Sudoku


class TestsAlgorithm:
  def __init__(self):
    self.bruteForce = BruteForce()
    self.bruteForceOptimized = BruteForceOptimized()
    self.branch_and_Bound = Branch_and_Bound()
    
    self.algorithms = [ self.branch_and_Bound]

    #self.sudoku = Sudoku()

  def newListForTimes(self, title, a):
      a.times.append([title])
      a.averageTimes.append([title,0])

  def testAlgorithm(self, sudoku, alg):
    
    alg.solveSudoku(sudoku)
    
    if(not sudoku.isSolved()): 
      alg.itWorks = False
      
    

  def algorithmInformation(self):
    s = ""
    
    for a in self.algorithms:
      s += "\n"
      s += a.name + "\n"
      #s += "Times:\n"
      # for time in a.times:
      #   s += str(time) + "\n"
      s += "Average time with: \n"
      for avr in a.averageTimes:
        s += str(avr[0]) + str(" ") + str(avr[1]) + "\n"
      s += "It Works: " + str(a.itWorks) + "\n"

    return s