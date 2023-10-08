from Node import Node

import math
import random
import copy


class Sudoku:
  def __init__(self):
    self.sudokuSolved = list()
    
    self.unsolvedSudoku = list()
    self.nodes = list()
    
    """
    Methods:
    
    generateSudokuSolved(self, n):
    
    dissolveSudoku(self, sudoku, n):
    
    checkPosition(self, sudoku, row, column):
        checkColumn(sudoku, column):
        checkRow(sudoku, row):
        checkSquare(sudoku, row, column):
        
    isSolved(self, sudoku, nodes):
    
    defineNodes(self):
    """

  def generateSudokuSolved(self, n):
    nsqrt = math.sqrt(n)
    if not nsqrt.is_integer(): return
    nsqrt = int(nsqrt)
    
    while True:
      try:
        self.sudokuSolved = list()
        self.nodes = list()
        numbers = set(range(1, n + 1))
        rowsSets = [set() for i in range(n)]
        columnsSets = [set() for i in range(n)]
        squaresSets = [set() for i in range(n)]

        for row in range(n):
          self.sudokuSolved.append(list())
         
          for column in range(n):
            
            sqrRowIndex = row - int((row % nsqrt))
            sqrColumnIndex = column - int((column % nsqrt))

            possibleElements = list(numbers - rowsSets[row].union(columnsSets[column]).union(squaresSets[sqrRowIndex + int(sqrColumnIndex / 3)]))

            element = random.choice(possibleElements)
            rowsSets[row].add(element)
            columnsSets[column].add(element)
            squaresSets[sqrRowIndex + int(sqrColumnIndex / 3)].add(element)
            self.sudokuSolved[row].append(element)
            
      except Exception as e:
        continue
      break
      
  def dissolveSudoku(self, n):
    self.unsolvedSudoku = copy.deepcopy(self.sudokuSolved)


    pairs = set()  # Usamos un conjunto para asegurarnos de que no haya duplicados
    while len(pairs) < n:
        r = random.randint(0, len(self.unsolvedSudoku)-1)  # Modifica estos rangos según tus necesidades
        c = random.randint(0, len(self.unsolvedSudoku)-1)
        pair = (r, c)
        pairs.add(pair)  # Agrega el par al conjunto (si no está repetido)
    
    pairs = list(pairs)  # Convierte el conjunto en una lista si es necesario
    
    for t in pairs:
      self.unsolvedSudoku[t[0]][t[1]] = -1

  def checkPosition(self, row, column):
    n = len(self.unsolvedSudoku)

    def checkColumn(column):
      frequency = {}
      for i in range(n):
        if self.unsolvedSudoku[i][column] in frequency or self.unsolvedSudoku[i][column] == -1:
          return False
        else:
          frequency[self.unsolvedSudoku[i][column]] = 1
      return True

    def checkRow(row):
      frequency = {}
      for i in range(n):
        if self.unsolvedSudoku[row][i] in frequency or self.unsolvedSudoku[row][i] == -1:
          return False
        else:
          frequency[self.unsolvedSudoku[row][i]] = 1
      return True

    def checkSquare(row, column):
      nsqrt = int(math.sqrt(len(self.unsolvedSudoku)))
      sqrRowIndex = row - int((row % nsqrt))
      sqrColumnIndex = column - int((column % nsqrt))

      frequency = {}
      for i in range(nsqrt):
        for j in range(nsqrt):
          if self.unsolvedSudoku[sqrRowIndex + i][sqrColumnIndex + j] in frequency or self.unsolvedSudoku[sqrRowIndex + i][sqrColumnIndex + j] == -1:
            return False
          else:
            frequency[self.unsolvedSudoku[sqrRowIndex + i][sqrColumnIndex + j]] = 1
      return True

    return checkColumn(column) and checkRow(row) and checkSquare(row, column)

  """Iterate over all the cells that started empty and check if they are correct"""
  def isSolved(self):
    return all(self.checkPosition(self.nodes[i].r, self.nodes[i].c) for i in range(len(self.nodes)))

  def defineNodes(self):
    n = len(self.unsolvedSudoku)
    for row in range(n):
      for column in range(n):
        if (self.unsolvedSudoku[row][column] == -1):
          self.nodes.append(Node(-1, row, column))
          self.unsolvedSudoku[row][column] = -1

  def defineNeighbors(self, node):
    nsqrt = int(math.sqrt(len(self.unsolvedSudoku)))
    sqrRowIndex2 = node.r - int((node.r % nsqrt))
    sqrColumnIndex2 = node.c - int((node.c % nsqrt))
    for n in self.nodes:
      sqrRowIndex1 = n.r - int((n.r % nsqrt))
      sqrColumnIndex1 = n.c - int((n.c % nsqrt))

      if(n.r == node.r or n.c == node.c or (sqrRowIndex2,sqrColumnIndex2) == (sqrRowIndex1,sqrColumnIndex1) ):
        node.neighbors.append(n)
    

  def nodeWithLessPossibleValues(self):
    min = 999
    node = None
    for n in self.nodes:
      if(len(n.possibleValues) < min and n.v == -1):
        min = len(n.possibleValues)
        node = n
    return node

  def nodesWithoutValue(self):
    l = []
    for n in self.nodes:
      if(n.v == -1):
        l.append(n)

    return l

  def printSudoku(self):
    sudokuCopy = copy.deepcopy(self.unsolvedSudoku)
    
    # Rellenar las celdas con sus posibles valores entre corchetes y convertir a cadena
    for i in range(len(sudokuCopy)):
        for j in range(len(sudokuCopy)):
            if sudokuCopy[i][j] == -1:
                sudokuCopy[i][j] = '[' + ', '.join(map(str, self.getNode(i, j).possibleValues)) + ']'
            else:
                sudokuCopy[i][j] = str(sudokuCopy[i][j])  # Convertir a cadena si es un número entero

    # Encontrar el ancho máximo de cada columna
    column_widths = [max(map(len, col)) for col in zip(*sudokuCopy)]
    
    # Imprimir el sudoku con las columnas alineadas correctamente
    for row in sudokuCopy:
        formatted_row = [val.center(width) for val, width in zip(row, column_widths)]
        print(' '.join(formatted_row))

    print("\n")
    
  def getNode(self, r, c):
    for n in self.nodes:
      if(n.r == r and n.c == c):
        return n
    return []