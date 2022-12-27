from threading import Thread
from time import time as now, sleep as wait
import os
import json
from typing import List

config = json.load(open("./config.json"))

# Timeout checking

def check_timeout(timeout:int):
    wait(timeout)
    force_stop(f"Timeout exceeded. Allowed time for resolving is {timeout} seconds.",1)

def start_timeout_check_thread():
    th = Thread(target=check_timeout,args=(config["timeout"],))
    th.start()

def force_stop(message:str=None, exit_status:int=0):
    if message is not None:
        print(message)
    os._exit(exit_status)

# Algorithms-related defs

def get_inv_count(arr:List[list], n:int):
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

def clearCLI():
    os.system('cls') if os.environ.get('OS','') == 'Windows_NT' else os.system('clear')

def format_current_status_for_printing(key:str,n:int)->str:
    stre = "|"
    for i in range(len(key)):
        stre += " "
        stre += (str(key[i]))
        if((i+1) %n==0):
            stre += " |\n|"
    return stre

#this would remove illegal moves for a given state
def available_moves(x:int,n:int)->list: 
    moves = ['Left', 'Right', 'Up', 'Down']
    if x % n == 0:
        moves.remove('Left')
    if x % n == n-1:
        moves.remove('Right')
    if x - n < 0:
        moves.remove('Up')
    if x + n > n**2 - 1:
        moves.remove('Down')

    return moves

def check_lines_integrity(lines:List[str])->bool:
    for line in lines:

        splitted = line.split(" ")

        if len(splitted) != 2:
            return False
        
        dimension = int(splitted[0])
        puzzle_string = splitted[1].replace("\n","").split(",")

        if len(puzzle_string) != dimension**2:
            return False
        
    return True
