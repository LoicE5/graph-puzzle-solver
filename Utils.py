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