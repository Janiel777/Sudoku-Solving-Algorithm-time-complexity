# Sudoku-time-complexity
Compare the time complexity of an algorithm that solves Sudoku with brute force techniques. Two brute force algorithms are going to be compared. One in which all combinations are tested without any type of optimization and in the second the possible numbers will be calculated for each empty cell and then all the possible combinations with those numbers are tested. This is for the purpose of seeing how much the time complexity was reduced for the first algorithm. This repository is still in progress. The idea is to add a third algorithm but that uses branch and bound techniques to further reduce the time complexity.

## Index
- Introduction
  - [Basic rules to solve a sudoku](#Basic-rules-to-solve-a-sudoku)
- Algorithms
   - [What is brute force technique](#What-is-brute-force-technique)
     
   - [Brute force without any optimization for solving the sudoku](#Brute-force-without-any-optimization-for-solving-the-sudoku)
      
   - [Brute force reducing the possible numbers of each empty cell for solving the sudoku](#Brute-force-reducing-the-possible-numbers-of-each-empty-cell-for-solving-the-sudoku)

   - [What is Branch and bound technique](#What-is-Branch-and-bound-technique)
 
   - [Branch and bound for solving the sudoku](#Branch-and-bound-for-solving-the-sudoku)

- [Comparison of time complexity of algorithms](#Comparison-of-time-complexity-of-algorithms)
     

<a name="Basic-rules-to-solve-a-sudoku"></a>
# Basic rules to solve a sudoku

The challenge when solving a sudoku is to find what numbers can be placed in the empty spaces and that the condition is met that no number is repeated for each row, column and box.

Some Sudoku solving techniques are as follows:
- Basic techniques
    - Unique position
    - Only possible number
- Intermediate techniques
    - Possible candidates
    - Double pairs
    - Multiple lines
- Advanced techniques
    - Safe couples
    - Hidden couples and trios
- Master techniques
    - Forced chains
    -Swordfish
    -X-Wing
- Divination techniques
    - Nishio
    - Fortune telling

However, the techniques that we are going to use to make the algorithms in the code are not going to be any of those. Even so, you can find a description for each of them on these two pages that explain Sudoku solving techniques: <a href="https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques" target="_blank"> Page1</a> <a href="https://www.sudoku10.net/sudokus-tecnicas-resolucion-sudoku-basicas.html" target="_blank"> Page2</a>

<a name="What-is-brute-force-technique"></a>
# What is brute force technique
Using brute force when designing an algorithm to solve a problem is basically calculating all possible scenarios until the correct solution is found. Normally, this technique is usually the last option since even for a computer the execution time until finding the correct solution can be extremely enormous. Even so, this does not mean that it is ruled out as an algorithm design technique. A simple example could be in the exhaustive search for a password. Unless we have some clues as to what the password could be, we would have no choice but to try all possible combinations. However, if we know that the password begins with x characters, that would greatly reduce the number of possible combinations when finding the password.

In the context of a sudoku, the clues are the numbers that are in the same column, row and box of each cell without a number. In this way, many possibilities could be discarded for each cell without a number, which would considerably reduce the number of combinations that we would have to perform. But would this make it viable to use brute force to solve a sudoku?


<a name="Brute-force-without-any-optimization-for-solving-the-sudoku"></a>
# Brute force without any optimization for solving the sudoku

The following description is a flowchart of how the algorithm works.

1. We create a class called Nodes to store specific cells in the sudoku. In this case, they will be the cells that started out empty. The nodes will have a value, their row and their column in which they are located
2. We iterate through the entire sudoku (2 for nested loops) and make a list in which we will save all the empty cells in the form of nodes.
3. We create a function to know if the sudoku is solved or not. This function iterates through the list of nodes and for each node it checks the elements in its column, row and box to see if that value is accepted.
4. We make a recursive function which will have as parameters the list of nodes and an indexing variable to access a node for each level of recursion.
    - We iterate between all the possible numbers that a cell can have (1 to 9) and:
      - Is the sudoku solved? Yes: we stop No: we continue
      - We change the value of the node to the iterator variable of the for
      - We call the recursion for the next node
     
```python
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
      for j in range(n):
        if self.isSolved(sudoku, nodes) or i >= len(nodes): return
        nodes[i].setValue(j + 1, sudoku)
        recursiveFunc(nodes, i + 1)
        self.iterations += 1

    recursiveFunc(nodes)

```


<a name="Brute-force-reducing-the-possible-numbers-of-each-empty-cell-for-solving-the-sudoku"></a>
# Brute force reducing the possible numbers of each empty cell for solving the sudoku

Este algoritmo es basicamente igual que el anterior pero en vez de probar en cada celda los numeros del 1 al 9, se reducen los posibles numeros de cada celda con respecto a los valores en sus filas, columnas y recuadros. De esta manera se puede llegar a reducir muchisimo el tiempo de complejidad. La siguiente descripcion es un flowchart del algortimo:

1. We create a class called Nodes to store specific cells in the sudoku. In this case they will be the cells that started empty. Nodes will have a value, their row, their column, and their possible values with respect to the values in their column, row, and box in which they are located.
2. We iterate through the entire sudoku (2 for nested loops) and make a list in which we will save all the empty cells in the form of nodes.
3. We create a function to know if the sudoku is solved or not. This function iterates through the list of nodes and for each node it checks the elements in its column, row and box to see if that value is correct.
4. We make a recursive function which will have as parameters the list of nodes and an indexing variable to access a node for each level of recursion.
    - We iterate between all the possible numbers that a cell can have (In this case it varies for each node) and:
      - Is the sudoku solved? Yes: we stop No: we continue
      - We change the value of the node to his next value in his possible values list
      - We call the recursion for the next node
     
```python
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

    def recursiveFunc(nodes, i=0):
      if i >= len(nodes): return
      
      #print(nodes[i].possibleValues)
      for j in range(len(nodes[i].possibleValues)):
        if self.isSolved(sudoku, nodes) or i >= len(nodes): return
        #nodes[i].setValue(nodes[i].possibleValues[j], sudoku)
        self.setNodeNextValue(nodes[i], sudoku)
        recursiveFunc(nodes, i + 1)
        self.iterations += 1

    recursiveFunc(nodes)
```

<a name="What-is-Branch-and-bound-technique"></a>
# What is Branch and bound technique

Branch and bound is an optimization technique used to solve combinatorics problems. What it does is convert the problem into a tree of possible solutions which it visits one by one and explores the promising branches, discarding all combinations that would not lead to the most optimal solution.

<a name="Branch-and-bound-for-solving-the-sudoku"></a>
# Branch and bound for solving the sudoku

Why isn't the algorithm that calculates the possible values for each cell and then brute forces it a branch and bound algorithm? This is because even with this method in which possible combinations are discarded, there are iterations in which two cells that share the same column, row or box may have the same value at that moment. In addition, when they have the same values, time is wasted calculating all the combinations for the other nodes. That is to say, time is wasted trying combinations in a branch that we know will not be the solution.

[Here there will be an explanation of how to make a branch and bound algorithm to solve a sudoku]

<a name="Comparison-of-time-complexity-of-algorithms"></a>
# Comparison of time complexity of algorithms

The following is a table comparing the complexity times for each algorithm.
```
Number of Empty Cells   | Time in seconds (Force brute)     | Time in seconds (Force brute with optimization)
1                       | 0.0002007436752319336             | 0.0003960323333740234
2                       | 0.0029160404205322266             | 0.0010248327255249024
3                       | 0.01653665542602539               | 0.00048390865325927736
4                       | 0.14886958599090577               | 0.0003703784942626953
5                       | 1.0962364149093629                | 0.0007730245590209961
6                       | 17.91752004623413                 | 0.0017011547088623047
7                       |                                   | 0.001208658218383789
8                       |                                   | 0.0008583593368530273
9                       |                                   | 0.0008507966995239258
10                      |                                   | 0.0021387863159179686
11                      |                                   | 0.0030039358139038086
12                      |                                   | 0.002734413146972656
13                      |                                   | 0.002538614273071289
14                      |                                   | 0.006195821762084961
15                      |                                   | 0.004740405082702637
16                      |                                   | 0.0030010461807250975
17                      |                                   | 0.004759960174560547
18                      |                                   | 0.008332276344299316
19                      |                                   | 0.010550575256347656
20                      |                                   | 0.011111707687377929
21                      |                                   | 0.03309983253479004
22                      |                                   | 0.01857440948486328
23                      |                                   | 0.022574400901794432
24                      |                                   | 0.04464530467987061
25                      |                                   | 0.04456526279449463
26                      |                                   | 6.8226388692855835
```


After calculating an exponential regression in Excel for each data set, these are the time complexity projections plotted in <a href="https://www.geogebra.org/?lang=es" target="_blank">geogebra</a>. 

![image](https://github.com/Janiel777/Sudoku-time-complexity/assets/95184925/44ac876c-3972-4fd2-b515-58d00a43da3a)


- The green function is the unoptimized brute force algorithm.
- The blue function is the optimized brute force algorithm.





Analyzing the data you can notice a big difference in the complexity times. The unoptimized brute force algorithm can be said to have a limit of 8 empty cells before it is raised to infinity. Making this algorithm not viable. On the other hand, the optimized brute force algorithm can solve a sudoku with 35 empty cells before exceeding the second in execution time. This could already be a viable algorithm. However, for a number of empty cells greater than 40, the execution time is still too high.
