"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
import time
import copy

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_slide, print_swing
from search.move import closestNodes, tokenMoves
from search.treepq import *
#from search.tree import *
from search.output import convertInput, printOutput

TYPE = 0
R = 1
Q = 2
UPPER = "upper"
LOWER = "lower"


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).

    boardDict = convertInput(data)
    print_board(board_dict=boardDict, compact=False)

    start = time.time()
    ### Note!!! need to build a visited array for BFS too! ###
    ################# testing part1
    mytree = tree(data)
    solution = mytree.bfs(data)
    ##################
    end = time.time()

    """start = time.time()
    ### Note!!! need to build a visited array for BFS too! ###
    ################# testing part1
    initial = data[UPPER][0]
    target = data[LOWER][0]
    goalState = copy.deepcopy(data)
    goalState[UPPER][0] = list(tuple(initial[TYPE]) + tuple([target[R], target[Q]]))
    mytree = tree(data)
    solution = mytree.bfs(data, goalState)
    ##################
    end = time.time()"""
    
    """while solution:
        nextBoard = solution.pop()
        print_board(board_dict=convertInput(nextBoard), compact=True)
        time.sleep(0.25)
    print(nextBoard)"""
    print(solution.popleft())
    print("Runtime is", end - start, "s")
    