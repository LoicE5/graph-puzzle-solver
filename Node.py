from Utils import available_moves, format_current_status_for_printing

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

    
    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def manhattan_distance(self ,n:int): 
        self.heuristic = 0
        for i in range(1 , n*n):
            dist = abs(self.state.index(i) - self.goal.index(i))
            
            #manhattan distance between the current state and goal state
            self.heuristic = self.heuristic + dist/n + dist%n
  
        self.AStar_evaluation = self.heuristic + self.cost
        
        return self.AStar_evaluation

    #heuristic function based on number of misplaced tiles
    def misplaced_tiles(self,n:int): 
        counter = 0
        self.heuristic = 0
        for i in range(n*n):
            if (self.state[i] != self.goal[i]):
                counter += 1
        self.heuristic = self.heuristic + counter
 
        self.AStar_evaluation = self.heuristic + self.cost

        return self.AStar_evaluation

    #produces children of a given state
    def expand(self , n:int)->list: 
        x = self.state.index(0)
        moves = available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
            children.append(Node(temp, self, direction, self.depth + 1, 1, self.goal)) #depth should be changed as children are produced
        return children
    
    #gets the given state and returns it's direction + it's parent's direction till there is no parent
    def solution(self, n:int)->dict:
        solution = {}
        solution[format_current_status_for_printing(self.state,n)] = (self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            stre = format_current_status_for_printing(path.state,n)
            solution[stre] = (path.direction)
        res =dict(reversed(list(solution.items())))
        return res

