# Puzzle Solver

> Group : [Maxime Bourdon](https://github.com/Mbourdon95), [Loïc Etienne](https://github.com/LoicE5)

The goal of this project is to solve a 15-puzzle using two graph search algorithms :
- A* (Astar)
- BFS (Breadth-First Search)

A* can take both manhattan distance & displaced tiles heuristics

A 15-puzzle looks like the following : 

![15-puzzle image (credit : Michael Kim)](https://user-images.githubusercontent.com/59501884/224975884-ebd60aed-4230-435b-8fa3-7730d7435056.png)

This project is a school project.

- Starting a terminal at the root of the project, you can launch the program in two ways:
    - `python3 Main.py`:
        
        this file allows you to launch the program manually,
        
        the program will ask the size of the puzzle (matrix of size n)
        
        the format of a puzzle is a sequence of numbers separated by commas (if you don't fill this field, a random puzzle will be generated)
        
        (example: 1,2,3,4,5,6,7,8,9)
        
        Then we can choose the heuristic for the realization of the algorithm of A* (Misplaced Tiles (`misplaced`) or Manhattan(`manhattan`)), the execution starts.


        
        The execution will be done in two steps, first it will solve the puzzle with the BFS and then with the chosen A*
        
    - `python3 FromFile.py` :
        
        this file allows to launch the program in automatic, the file *puzzles_examples.txt* contains different puzzles which will be solved line by line, each line is composed :
        
        n : the size of the matrix
        
        string : the puzzle to solve

        You can edit this file, or create a new one following the same format. Please avoid adding extra whitespace in the file, as it is used to separate the dimension and the puzzle string already.

        > Among the default values in the *puzzles_examples.txt* file, one is non-solvable, and serves as an example about how non-solvable puzzles are handled.
        

You can also change the default time limit and heuristic ("manhattan", "misplaced") in the config.json file.
