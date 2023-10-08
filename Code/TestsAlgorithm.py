from BruteForce import BruteForce
from BruteForceOptimized import BruteForceOptimized
from Backtracking import Backtracking


class TestsAlgorithm:
  def __init__(self):
    self.bruteForce = BruteForce()
    self.bruteForceOptimized = BruteForceOptimized()
    self.backtracking = Backtracking()
    
    self.algorithms = [ self.backtracking]


  def newListForTimes(self, title, a):
      a.times.append([title])
      a.averageTimes.append([title,0])
      a.maxTime.append([title + " max Time"])

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
      for max in a.maxTime:
        s += str(max[0]) + " " + str(max[1]) + "\n"
      s += "It Works: " + str(a.itWorks) + "\n"

    return s