from AlgoritmoProperties import AlgoritmoProperties

import time


class Branch_and_Bound(AlgoritmoProperties):
  def __init__(self):
    super().__init__()
    self.name = "Branch_and_Bound"

  def solveSudoku(self, sudoku):
    initialTime = time.time()
    #-------------------------------------------


    #-------------------------------------------
    self.times[-1].append(time.time() - initialTime)
    self.averageTimes[-1][1] = sum(self.times[-1][1:])/len(self.times[-1][1:])