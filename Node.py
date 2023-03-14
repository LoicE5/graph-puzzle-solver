from utils import available_moves, format_current_status_for_printing

class Node:

    def __init__(self, state:list, parent, direction:str, depth:int, cost:int, goal:list):
        self.state:list = state
        self.parent:Node = parent
        self.direction:str = direction
        self.depth:int = depth
        self.goal:list = goal

        self.AStar_evaluation:int = None
        self.heuristic:int = None

        if parent:
            self.cost:int = parent.cost + cost

        else:
            self.cost:int = cost

    
    def check_if_its_goal_state(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def misplaced_tiles(self,dimension:int): 
        counter = 0
        self.heuristic = 0
        for i in range(dimension**2):
						#check if the tile at index i is the same as the tile 
						#at index i of the goal state
            if (self.state[i] != self.goal[i]):
                counter += 1
        self.heuristic = self.heuristic + counter
				#once the score is generated, 
				#we return this score + the path cost (path cost is incremented at each node)
        self.AStar_evaluation = self.heuristic + self.cost

        return self.AStar_evaluation

   #heuristic function based on number of misplaced tiles
    def manhattan_distance(self ,dimension:int): 
        self.heuristic = 0
        for i in range(1 , dimension**2):
            dist = abs(self.state.index(i) - self.goal.index(i))
            
        #we generate a score as the distance between the current state and goal state
            self.heuristic = self.heuristic + dist/dimension + dist%dimension
			  #once the score is generated, 
				#we return this score + the path cost (path cost is incremented at each node)
        self.AStar_evaluation = self.heuristic + self.cost
        
        return self.AStar_evaluation

    #generates the different children of a node
    def expand(self , dimension:int)->list: 
        x = self.state.index(0)
        moves = available_moves(x,dimension)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - dimension] = temp[x - dimension], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + dimension] = temp[x + dimension], temp[x]
        
            # we need to add new Node to children and increase the depth 
            children.append(Node(temp, self, direction, self.depth + 1, 1, self.goal)) 
        return children
    
    #get the full solution of a puzzle, with the puzzle and the direction for each move
    def solution(self, dimension:int)->dict:
        solution = {}
        solution[format_current_status_for_printing(self.state,dimension)] = (self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            stre = format_current_status_for_printing(path.state,dimension)
            solution[stre] = (path.direction)
        res =dict(reversed(list(solution.items())))
        return res

