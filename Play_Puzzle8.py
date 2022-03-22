import numpy as np
import random

#state = np.arange(9).reshape(3,3)
goal_state = np.arange(9).reshape(3,3)
state = np.array([[1,0,3],[4,7,5],[6,8,2]])
#[np.random.shuffle(x) for x in state]
#np.random.shuffle(state)


print(state)

"""
def moveUp(value,state):
    epty_i,epty_j = np.where(state == 0)
    empty_position = epty_i*3 + epty_j
    if (value > 0 and value < 9):
        i,j = np.where(state == value)
    if (i == epty_i + 1 and j == epty_j):
        position_value = i*3 + j
        np.take(state,[position_value,empty_position])
        np.put(state,[position_value,empty_position],[0,value])
    return print(state);

def moveDown(value,state):
    epty_i,epty_j = np.where(state == 0)
    empty_position = epty_i*3 + epty_j
    if (value > 0 and value < 9):
        i,j = np.where(state == value)
    if (i == epty_i - 1 and j == epty_j):
        position_value = i*3 + j
        np.take(state,[position_value,empty_position])
        np.put(state,[position_value,empty_position],[0,value])
    return print(state);

def moveLeft(value,state):
    epty_i,epty_j = np.where(state == 0)
    empty_position = epty_i*3 + epty_j
    if (value > 0 and value < 9):
        i,j = np.where(state == value)
    if (i == epty_i and j == epty_j + 1):
        position_value = i*3 + j
        np.take(state,[position_value,empty_position])
        np.put(state,[position_value,empty_position],[0,value])
    return print(state);

def moveRight(value,state):
    epty_i,epty_j = np.where(state == 0)
    empty_position = epty_i*3 + epty_j
    if (value > 0 and value < 9):
        i,j = np.where(state == value)
    if (i == epty_i and j == epty_j - 1):
        position_value = i*3 + j
        np.take(state,[position_value,empty_position])
        np.put(state,[position_value,empty_position],[0,value])
    return print(state);
"""
def swapPosition(position1,position2,state,value):
    np.take(state,[position1,position2])
    np.put(state,[position1,position2],[0,value])

def positionMath(x,y):
    return x*3 + y
    
def randomMove(state):
    value = random.randint(1,8)
    print(value)
    i,j = np.where(state == value)
    position_value = positionMath(i,j)
    epty_i,epty_j = np.where(state == 0)
    empty_position = positionMath(epty_i,epty_j)
    if (i == epty_i + 1 and j == epty_j):
        swapPosition(position_value,empty_position,state,value)
    elif (i == epty_i - 1 and j == epty_j):
        swapPosition(position_value,empty_position,state,value)
    elif (i == epty_i and j == epty_j + 1):
        swapPosition(position_value,empty_position,state,value)
    elif (i == epty_i and j == epty_j - 1):
        swapPosition(position_value,empty_position,state,value)
    return print(state);
    
def heuristicFunction(actual_state):
    return 0;

while (state.all(axis = 2) != goal_state.all(axis = 2)):
    randomMove(state)
"""    
while True:
    n = int(input("Selecione o número:"))
    choice = input("Seleciona o lado para o qual este deve se mover:")
    if (choice == "d"):
        moveRight(n,state)
    elif (choice == "a"):
        moveLeft(n,state)
    elif (choice == "w"):
        moveUp(n,state)
    elif (choice == "s"):
        moveDown(n,state)"""
