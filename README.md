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


<a name="Brute-force-reducing-the-possible-numbers-of-each-empty-cell-for-solving-the-sudoku"></a>
# Brute force reducing the possible numbers of each empty cell for solving the sudoku

<a name="What-is-Branch-and-bound-technique"></a>
# What is Branch and bound technique

<a name="Branch-and-bound-for-solving-the-sudoku"></a>
# Branch and bound for solving the sudoku

<a name="Comparison-of-time-complexity-of-algorithms"></a>
# Comparison of time complexity of algorithms
