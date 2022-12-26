from Utils import get_inv_count
from State import State
from queue import PriorityQueue
from queue import Queue
from typing import List

class PuzzleSolver:
    dimension:int
    puzzle:list = []
    rows:list = []
    state:list = []
    goal:list = []

    def __init__(self, dimension:int, puzzle_string:str=None):
        self.dimension = dimension
        if puzzle_string is not None:
            self.build_puzzle(puzzle_string)

    def build_puzzle(self, puzzle_string:str):
        j = 1
        for i in puzzle_string.split(","):
            i = int(i)
            self.state.append(i)
            self.rows.append(i)
            if len(self.rows) % self.dimension == 0: 
                self.puzzle.append(self.rows)
                self.rows = []
            self.goal.append(j)
            j+=1
        self.goal[len(self.goal)-1] = 0

    def is_puzzle_string_right_dimension(self, puzzle_string:str):
        return len(puzzle_string.split(",")) == (self.dimension*self.dimension)

    def is_solvable(self):
        # This function returns true if given
        # instance of N*N - 1 puzzle is solvable

        # Count inversions in given puzzle
        inv_count = get_inv_count(self.puzzle,self.dimension)
    
        # If grid is odd, return true if inversion
        # count is even.
        if (self.dimension & 1):
            return ~(inv_count & 1)
    
        else:    # grid is even
            pos = self.find_x_position()
            if (pos & 1):
                return ~(inv_count & 1)
            else:
                return inv_count & 1

    def find_x_position(self):
        # start from bottom-right corner of matrix
        for i in range(self.dimension - 1,-1,-1):
            for j in range(self.dimension - 1,-1,-1):
                if (self.puzzle[i][j] == 0):
                    return self.dimension - i

class Astar(PuzzleSolver):

    def __init__(self, dimension:int, heuristic:str, puzzle_string:str=None):
        super().__init__(dimension, puzzle_string)
        self.heuristic = heuristic

    def run(self):
        frontier = PriorityQueue()
        explored = []
        counter = 0
        root = State(self.state, None, None, 0, 0, self.goal)
        if self.heuristic == 'manhattan':
            evaluation = root.Manhattan_Distance(self.dimension) 
        else:
            evaluation = root.Misplaced_Tiles(self.dimension) 
        frontier.put((evaluation, counter, root)) #based on A* evaluation

        while not frontier.empty():
            current_node:tuple = frontier.get()
            current_node:State = current_node[2]
            explored.append(current_node.state)
            
            if current_node.test():
                return current_node.solution(self.dimension), len(explored)

            children = current_node.expand(self.dimension)
            for child in children:
                if child.state not in explored:
                    counter += 1
                    if self.heuristic == 'manhattan':
                        evaluation = child.Manhattan_Distance(self.dimension) 
                    else:
                        evaluation = child.Misplaced_Tiles(self.dimension) 
                    frontier.put((evaluation, counter, child)) #based on A* evaluation
        return

class BFS(PuzzleSolver):

    def __init__(self, dimension:int, puzzle_string:str=None):
        super().__init__(dimension, puzzle_string)

    def run(self):
        frontier = Queue()
        explored = set()
        
        initial = State(self.state, None, None, 0, 0, self.goal)
        frontier.put(initial)
        counter = 0

        # while nodes is not empty
        while not frontier.empty():

            current_node:State = frontier.get()
            current_state:list = current_node.state

            explored.add(str(current_state))
            children:List[State] = current_node.expand(self.dimension)

            if current_node.test():
                return current_node.solution(self.dimension), len(explored)

            for child in children:
                if str(child.state) not in explored:
                    counter += 1
                    frontier.put(child)
        return