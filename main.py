from Sudoku import Sudoku
from TestsAlgorithm import TestsAlgorithm
import sys

def delete_last_line():
  sys.stdout.write("\033[F")  
  sys.stdout.write("\033[K") 

def main():
  sudoku = Sudoku()
  tester = TestsAlgorithm()

  number_of_Tests = 100
  emptyCellsRange = 81
  timeLimit = 1

  for alg in tester.algorithms:
    
    for emptycellnumber in range(1,emptyCellsRange+1):
      if len(alg.averageTimes) != 0 and alg.averageTimes[-1][1] > timeLimit or not alg.itWorks: break
        
      title = str(emptycellnumber) + " empty cells"
      tester.newListForTimes(title, alg)
      
      for testNumber in range(number_of_Tests):
        if alg.averageTimes[-1][1] > timeLimit or not alg.itWorks: break
          
        delete_last_line()
        print(alg.name,"Empy cells number:",emptycellnumber, testNumber,"of", number_of_Tests)
        sudoku.generateSudokuSolved(9)
        sudoku.dissolveSudoku(emptycellnumber)
        tester.testAlgorithm(sudoku, alg)
        
      delete_last_line()
    

  print(tester.algorithmInformation())

main()