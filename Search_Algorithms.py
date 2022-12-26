from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


#Breadth-first Search
def BFS(given_state , n, goal):
    frontier = Queue()
    explored = set()
    
    initial = State(given_state, None, None, 0, 0, goal)
    frontier.put(initial)

    counter = 0
	# while nodes is not empty


    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state
        explored.add(str(current_state))
        children = current_node.expand(n)
        if current_node.test():
            return current_node.solution(n), len(explored)
        for child in children:
            if str(child.state) not in explored:
                counter += 1
                frontier.put(child)
    return

def AStar_search(given_state , n, goal, heuristic):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0, goal)
    if heuristic == 'manhattan':
        evaluation = root.Manhattan_Distance(n) 
    else:
        evaluation = root.Misplaced_Tiles(n) 
    frontier.put((evaluation, counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(n), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                if heuristic == 'manhattan':
                    evaluation = child.Manhattan_Distance(n) 
                else:
                    evaluation = child.Misplaced_Tiles(n) 
                frontier.put((evaluation, counter, child)) #based on A* evaluation
    return
