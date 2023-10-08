# Sudoku-Solving-Algorithm-time-complexity
Compare the time complexity of an algorithm that solves Sudoku with brute force techniques. Two brute force algorithms are going to be compared. One in which all combinations are tested without any type of optimization and in the second the possible numbers will be calculated for each empty cell and then all the possible combinations with those numbers are tested. This is for the purpose of seeing how much the time complexity was reduced for the first algorithm. This repository is still in progress. The idea is to add a third algorithm but that uses branch and bound techniques to further reduce the time complexity.

## Index
- Introduction
  - [Basic rules to solve a sudoku](#Basic-rules-to-solve-a-sudoku)
- Algorithms
   - [What is brute force technique](#What-is-brute-force-technique)
     
   - [Brute force without any optimization for solving the sudoku](#Brute-force-without-any-optimization-for-solving-the-sudoku)
      
   - [Brute force reducing the possible numbers of each empty cell for solving the sudoku](#Brute-force-reducing-the-possible-numbers-of-each-empty-cell-for-solving-the-sudoku)

   - [What is backtracking technique](#What-is-Branch-and-bound-technique)
 
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
Using brute force when designing an algorithm to solve a problem is basically calculating all possible scenarios until you find the correct solution. Normally this technique is usually the last option since even for a computer the execution time until finding the correct solution can be extremely enormous. Even so, this does not mean that it is discarded as an algorithm design technique. A simple example could be searching exhaustively for a password. Unless we have some clues as to what the password could be, we would have no choice but to try every possible combination. However, if we know that the password can only begin and end with numbers, that would greatly reduce the number of possible combinations when finding the password.

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

This algorithm is basically the same as the previous one but instead of testing the numbers from 1 to 9 in each cell, the possible numbers in each cell are reduced with respect to the values in its rows, columns and boxes. In this way, the complexity time can be greatly reduced. The following description is a flowchart of the algorithm:

1. We create a class called Nodes to store specific cells in the sudoku. In this case they will be the cells that started empty. Nodes will have a value, their row, their column, and their possible values with respect to the values of their column, row, and box they are in.
2. We go through the entire sudoku (2 for nested loops) and make a list in which we will save all the empty cells in the form of nodes.
3. We create a function to know if the sudoku is solved or not. This function loops through the list of nodes and for each node checks the elements in its column, row, and box to see if that value is correct.
4. We make a function that calculates and defines a list for each node containing its possible values that they can take and we call this function for each node.
5. We make a recursive function which will have as parameters the list of nodes and an indexing variable to access a node for each level of recursion.
  - We iterate between all the possible numbers that a cell can have (In this case it varies for each node) and:
    - Is the sudoku solved? Yes: we stop No: we continue
    - We change the value of the node to its next value in its list of possible values
    -  We call recursion for the next node.
     
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

<a name="What is backtracking technique"></a>
# What is backtracking technique

Backtracking is a search technique used to solve search problems. What it does is explore the tree of possible paths, discarding all branches that would not lead to the solution.

<a name="Branch-and-bound-for-solving-the-sudoku"></a>
# Backtracking for solving the sudoku

In the context of a sudoku, what the backtracking algorithm does is visit the nodes and assume values for each of them. When you encounter a node that no longer has possible values due to the assumptions that were made, it means that it is time to go back and change to the next value of the last node to which we assumed a value. This allows us to discard search branches every time we find a dead end, so the possible combinations are reduced the more we explore the branches. 

This method of moving as deep as possible before going back and continuing the search on the next branch is known as Deep first search. Now, you will know that any algorithm that can be implemented with Deep first search can also be implemented with Breadth first seacrh. However, in the context of a sudoku, this way of moving through the combination tree does not offer us any advantage over Deep first seacrh. In fact, to be able to move using Breadth first search we would have to use more memory to be able to keep track of which would be the next node to expand. This makes the Deep fisrt seacrh search form the most optimal for this type of problem.

The following description is a flowchart of how the algorithm works.

1. We create a class called Nodes to store specific cells in the sudoku. In this case they will be the cells that started empty. The nodes will have a value, their row, their column, their possible values and their neighboring nodes.

2. we iterate through the entire sudoku (2 for loops nested) and make a list of nodes for all the cells that started empty. Nodes that have values of -1 will be considered empty.

3. Afterwards, it is iterated over the list of nodes and it is defined for each node, what are the possible values that they can take and what are their neighboring nodes.

4. We create a recursive function that will implement the backtracking technique. This will receive a node as a parameter.
   - For that node we are in, it will iterate through its possible values.
     - Its value will be changed to the current value of the for loop.
     - The value assumed for the current node will be removed from the list of possible values of the neighboring nodes of the node in which we are located.
     - We calculate the node with the smallest number of possible values and that does not have an assigned value.
     - We call the recursion for that node.
     - After the recursive call, if the sudoku was not solved after having changed the value of the current node, you must return to the neighbors the value that was eliminated from all the lists of possible values for each neighbor and without forgetting also add it to the list of possible values of the current node we are in. Without forgetting to change the value of the current node to -1.
     - End of for loop
       
(Base statements for the bactracking)
  - If there is no node that has not been assigned a value, it means that all of them already have a value and therefore the sudoku is already solved. In this context, that function that calculates the next node would return None.
  - When the current node does not have any possible number to assume.

5. Call the backtracking function for any node in the node list.

The implemented code:

```python
def solveSudoku(self, sudoku):

    size = len(sudoku.unsolvedSudoku)
    
    sudoku.defineNodes()
    for n in sudoku.nodes:
      n.updatePossibleValues(sudoku)
      sudoku.defineNeighbors(n)
    
    
    def backtracking(currentNode, finished):

      if currentNode == None: 
        finished[0] = True
        return
        
      if len(currentNode.possibleValues) == 0: 
        return
      
      for v in copy.deepcopy(currentNode.possibleValues):
        currentNode.setValue(v,sudoku)
          
        l = currentNode.removeValueInNeighbors()
        backtracking(sudoku.nodeWithLessPossibleValues(), finished)
        
        if finished[0]: return
        
        currentNode.restoreValueInNeighbors(l)
        currentNode.setValue(-1, sudoku)
        
```


<a name="Comparison-of-time-complexity-of-algorithms"></a>
# Comparison of time complexity of algorithms

The following is a table comparing the average complexity times for each algorithm after having solved 100 sudoku for each number of blank cells. The brute force algorithm took too long when there were 7 empty cells or more.
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
