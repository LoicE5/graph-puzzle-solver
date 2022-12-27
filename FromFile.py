from Utils import check_lines_integrity, start_timeout_check_thread, config, force_stop, clearCLI
from time import time as now
from PuzzleSolver import BFS, Astar

clearCLI()
filepath = input("Please enter the file path :\n")

file = open(filepath)

lines = file.readlines()

if not check_lines_integrity(lines):
    exit(f"Lines (at least 1) are not in the right format in {filepath}")

start_timeout_check_thread()

counter = 1

for line in lines:
    print("========== Puzzle n°",counter,"| value : ",line.replace("\n",""),"==========")

    n, p = line.split(" ")
    n = int(n)

    bfs_start_time = now()
    bfs_instance = BFS(
        dimension=n,
        puzzle_string=p
    )
    assert bfs_instance.is_solvable()
    BFS_solution = bfs_instance.run()
    BFS_time = now() - bfs_start_time

    print('BFS Solution is : ')
    for key,value in BFS_solution[0].items():
        print(key ,'|| Move -> ', value, ' ||\n\n')
    print('Number of explored nodes is ', BFS_solution[1])    
    print('BFS Time:', BFS_time , "\n")

    astar_start_time = now()
    AStar_instance = Astar(
        dimension=n,
        heuristic=config["default_heuristic"],
        puzzle_string=p
    )
    assert AStar_instance.is_solvable()
    AStar_solution = AStar_instance.run()
    AStar_time = now() - astar_start_time

    print('A* Solution is with ',config["default_heuristic"],' : ')
    for key,value in AStar_solution[0].items():
        print(key ,'|| Move -> ', value, ' ||\n\n')
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:', AStar_time)

    counter += 1


force_stop()