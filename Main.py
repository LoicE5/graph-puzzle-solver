from Search_Algorithms import BFS, AStar_search
from time import time
import os

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

def getInvCount(arr):
    arr1=[]
    for y in arr:
        for x in y:
            arr1.append(x)
    arr=arr1
    inv_count = 0
    for i in range(n * n - 1):
        for j in range(i + 1,n * n):
            # count pairs(arr[i], arr[j]) such that
            # i < j and arr[i] > arr[j]
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count+=1
         
     
    return inv_count
 
 
# find Position of blank from bottom
def findXPosition(puzzle):
    # start from bottom-right corner of matrix
    for i in range(n - 1,-1,-1):
        for j in range(n - 1,-1,-1):
            if (puzzle[i][j] == 0):
                return n - i
 
 
# This function returns true if given
# instance of N*N - 1 puzzle is solvable
def isSolvable(puzzle):
    # Count inversions in given puzzle
    invCount = getInvCount(puzzle)
 
    # If grid is odd, return true if inversion
    # count is even.
    if (n & 1):
        return ~(invCount & 1)
 
    else:    # grid is even
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1


#1,8,7,3,0,5,4,6,2 is solvable
#12,1,10,2,7,11,4,14,5,0,9,15,8,13,6,3 is solvable


if isSolvable(puzzle):
    print("Solvable, please wait. \n")
    
    #time1 = time()
   # BFS_solution = BFS2(state,goal)
   # BFS_time = time() - time1
   # print('BFS Solution is ', BFS_solution[0])
   # print('Number of explored nodes is ', BFS_solution[1])    
  #  print('BFS Time:', BFS_time , "\n")
    
    time4 = time()
    AStar_solution = AStar_search(state, n, goal, heuristic)
    AStar_time = time() - time4
    print('A* Solution is ', AStar_solution[0])
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:', AStar_time)
    
    
else:
    print("Not solvable")
