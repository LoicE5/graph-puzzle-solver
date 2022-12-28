from Utils import get_inv_count
from Node import Node
from queue import PriorityQueue
from queue import Queue
from typing import List

class PuzzleSolver:

    def __init__(self, dimension:int, puzzle_string:str=None):
        self.dimension:int = dimension
        self.puzzle:list = []
        self.rows:list = []
        self.state:list = []
        self.goal:list = []
        
        if puzzle_string is not None:
            self.build_puzzle(puzzle_string)

    def build_puzzle(self, puzzle_string:str):
        self.puzzle = []
        self.rows = []
        self.state = []
        self.goal = []

        j = 1

        for i in puzzle_string.split(","):
            self.state.append(int(i))
            self.rows.append(int(i))

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
        self.heuristic:str = heuristic

    def run(self):
         #let nodes equal empty list of nodes
        nodes = PriorityQueue()
        #let explored_nodes equal empty list of nodes
        explored_nodes = []
        counter = 0
        # let initial_node, the initial Start Node
        initial_node = Node(self.state, None, None, 0, 0, self.goal)
        if self.heuristic == 'manhattan':
            score = initial_node.manhattan_distance(self.dimension) 
        else:
            score = initial_node.misplaced_tiles(self.dimension) 
        # put the start Node into nodes 
        nodes.put((score, counter, initial_node)) 
        while not nodes.empty():
            #Get the current node
            current_node:tuple = nodes.get()
            current_node:Node = current_node[2]
            explored_nodes.append(current_node.state)
            # if current_Node is the goal
            if current_node.check_if_its_goal_state():
                #return the solution
                return current_node.solution(self.dimension), len(explored_nodes)
            #else generate possible children of the state
            children = current_node.expand(self.dimension)
            for child in children:
                if child.state not in explored_nodes:
                    counter += 1
                    #call the heuristic function to generate the score
                    if self.heuristic == 'manhattan':
                        score = child.manhattan_distance(self.dimension) 
                    else:
                        score = child.misplaced_tiles(self.dimension) 
                    #put the child into nodes 
                    nodes.put((score, counter, child)) 
        return

class BFS(PuzzleSolver):

    def __init__(self, dimension:int, puzzle_string:str=None):
        super().__init__(dimension, puzzle_string)

    def run(self):
       #let nodes equal empty list of nodes
        nodes = Queue()
        #let explored_nodes equal empty list of nodes
        explored_nodes = set()
        # put the start Node into frontier
        initial_node = Node(self.state, None, None, 0, 0, self.goal)
        nodes.put(initial_node)
        counter = 0

        # while nodes is not empty
        while not nodes.empty():

            current_node:Node = nodes.get()
            current_state:list = current_node.state

            explored_nodes.add(str(current_state))
            # if current_Node is the goal
            if current_node.check_if_its_goal_state():
                #return the solution
                return current_node.solution(self.dimension), len(explored_nodes)
            #else generate possible children of the state
            children:List[Node] = current_node.expand(self.dimension)
            for child in children:
                if str(child.state) not in explored_nodes:
                    counter += 1
                    #put the child into frontier 
                    nodes.put(child)
        return
