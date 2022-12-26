

class State:
    AStar_evaluation = None
    heuristic = None
    def __init__(self, state, parent, direction, depth, cost, goal):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        self.goal = goal
        # self.visited = False

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

    
    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def Manhattan_Distance(self ,n): 
        self.heuristic = 0
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            #manhattan distance between the current state and goal state
            self.heuristic = self.heuristic + distance/n + distance%n
  
        self.AStar_evaluation = self.heuristic + self.cost
        
        return(self.AStar_evaluation)


    #heuristic function based on number of misplaced tiles
    def Misplaced_Tiles(self,n): 
        counter = 0
        self.heuristic = 0
        for i in range(n*n):
            if (self.state[i] != self.goal[i]):
                counter += 1
        self.heuristic = self.heuristic + counter
 
        self.AStar_evaluation = self.heuristic + self.cost

        return(self.AStar_evaluation)    #Nous on doit return      


    @staticmethod
    #this would remove illegal moves for a given state
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    #produces children of a given state
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
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
        
        
            children.append(State(temp, self, direction, self.depth + 1, 1, self.goal)) #depth should be changed as children are produced
        return children

    
    #gets the given state and returns it's direction + it's parent's direction till there is no parent
    def solution(self, n):
        solution = {}
        solution[aaa(self.state,n)] = (self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            stre = aaa(path.state,n)
            solution[stre] = (path.direction)
        res =dict(reversed(list(solution.items())))
        return res


def aaa(key,n):
        stre = "|"
        for i in range(len(key)):
            stre += " "
            stre += (str(key[i]))
            if((i+1) %n==0):
                stre += " |\n|"
        return stre