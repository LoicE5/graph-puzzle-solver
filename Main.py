from time import time as now
from Utils import start_timeout_check_thread, force_stop, clearCLI
from PuzzleSolver import PuzzleSolver, BFS, Astar

n = int(input("Please enter your desired puzzle's dimension :\n"))

base_solver = PuzzleSolver(n)

p = str(input(f"Please enter your {base_solver.dimension}*{base_solver.dimension} puzzle :\n"))

while(not base_solver.is_puzzle_string_right_dimension(p)):
    clearCLI()
    p = str(input(f"The dimension doesn't match the provided puzzle string.\nPlease enter your {base_solver.dimension}*{base_solver.dimension} puzzle :\n"))

base_solver.build_puzzle(p)

clearCLI()

print("The given state is : ", base_solver.state)
print("The goal state is : ", base_solver.goal)
print("Puzzle equal : ", base_solver.puzzle)

heuristic = str(input('Please specify wether you want a A* solving using Misplaced tiles heuristic (type "misplaced") or with Manhattan distance heuristic (type "manhattan") :\n'))


if base_solver.is_solvable():
    print("Solvable, please wait. \n")
    start_timeout_check_thread()
    
    bfs_start_time = now()
    BFS_solution = BFS(base_solver).run()
    BFS_time = now() - bfs_start_time

    print('BFS Solution is : ')
    for key,value in BFS_solution[0].items():
        print(key ,'|| Move -> ', value, ' ||\n\n')
    print('Number of explored nodes is ', BFS_solution[1])    
    print('BFS Time:', BFS_time , "\n")
    
    astar_start_time = now()
    AStar_solution = Astar(base_solver,heuristic).run()
    AStar_time = now() - astar_start_time

    print('A* Solution is with ',heuristic,' : ')
    for key,value in AStar_solution[0].items():
        print(key ,'|| Move -> ', value, ' ||\n\n')
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:', AStar_time)

    force_stop() # Here to kill any remaining thread after execution
    
    
else:
    print("Not solvable")

    


#1,2,3,4,5,6,7,8,9,14,15,0,13,10,11,12 resolvable par tous les algos 
#3.38 en misplaced tiles 9386 nodes explored
#22.114 en bfs avec 1352057 nodes explored
#0.041081905364990234 en manhattan 1014 nodes explored