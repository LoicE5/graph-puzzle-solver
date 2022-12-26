from Search_Algorithms import BFS, AStar_search
from time import time
import os
from Utils import start_timeout_check_thread, force_stop, getInvCount, findXPosition, isSolvable

#initial state
n = int(input("Enter n\n"))
puzzle=[]
rows = []
state = []
goal = []
print("Enter your" ,n,"*",n, "puzzle")
p = str(input())

while(len(p.split(",")) != n*n):
    os.system('cls')
    print("Enter your" ,n,"*",n, "puzzle")
    p = str(input())
j = 1
for i in p.split(","):
    state.append(int(i))
    rows.append(int(i))
    if len(rows) % n == 0: 
        puzzle.append(rows)
        rows = []
    goal.append(j)
    j+=1
goal[len(goal)-1] = 0 
os.system('cls')
print("The given state is : ", state)
print("The goal state is : ", goal)
print("Puzzle equal : ", puzzle)

print("Need Misplaced or manhattan resolution")
heuristic = str(input())


#1,8,7,3,0,5,4,6,2 is solvable
#7, 11, 5, 8, 1, 10, 2, 4, 9, 0, 3, 6, 13, 14, 15, 12 is solvable


if isSolvable(puzzle,n):
    print("Solvable, please wait. \n")
    start_timeout_check_thread()
    
    time1 = time()
    BFS_solution = BFS(state,n,goal)
    BFS_time = time() - time1
    print('BFS Solution is : ')
    for key,value in BFS_solution[0].items():
        print(key ,'|| Move -> ', value, ' ||\n\n')
    print('Number of explored nodes is ', BFS_solution[1])    
    print('BFS Time:', BFS_time , "\n")
    
    time4 = time()

    AStar_solution = AStar_search(state, n, goal, heuristic)
    AStar_time = time() - time4
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