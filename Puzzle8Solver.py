import numpy as np
import random

goal_state = np.arange(9).reshape(3,3)
initial_search = np.arange(9).reshape(3,3)
[np.random.shuffle(x) for x in initial_search]
np.random.shuffle(initial_search)
print(initial_search)

def swapPosition(position1,position2,state,value):
    np.take(state,[position1,position2])
    np.put(state,[position1,position2],[0,value])
    return state

def flagState(actual_state):
    state2 = np.zeros((3,3))
    for x in range(3):
        for y in range(3):
            state2[x][y] = int(actual_state[x][y])
    return state2

def positionMath(x,y):
    return x*3 + y

def Queue(stt):
    flag = flagState(stt)
    e_i,e_j = np.where(flag == 0)
    t = np.zeros(1)
    if(e_i == 0 and e_j == 0):
        t = [flag[0][1],flag[1][0]]
        search_value = random.choice(t)
    elif(e_i == 0 and e_j == 1):
        t = [flag[0][0],flag[1][1],flag[0][2]]
        search_value = random.choice(t)
    elif(e_i == 0 and e_j == 2):
        t = [flag[0][1],flag[1][2]]
        search_value = random.choice(t)
    elif(e_i == 1 and e_j == 0):
        t = [flag[0][0],flag[1][1],flag[2][0]]
        search_value = random.choice(t)
    elif(e_i == 1 and e_j == 1):
        t = [flag[0][1],flag[1][0],flag[1][2],flag[2][1]]
        search_value = random.choice(t)
    elif(e_i == 1 and e_j == 2):
        t = [flag[0][2],flag[1][1],flag[2][2]]
        search_value = random.choice(t)
    elif(e_i == 2 and e_j == 0):
        t = [flag[1][0],flag[2][1]]
        search_value = random.choice(t)
    elif(e_i == 2 and e_j == 1):
        t = [flag[2][0],flag[1][1],flag[2][2]]
        search_value = random.choice(t)
    elif(e_i == 2 and e_j == 2):
        t = [flag[2][1],flag[1][2]]
        search_value = random.choice(t)
    priorityQueue(search_value,stt,goal_state)
    return int(search_value);

def priorityQueue(search_tool,stt,goal):
    i_t,j_t = np.where(stt == search_tool)
    i_g,j_g = np.where(goal == search_tool)
    if (i_t == i_g and j_t == j_g and search_tool == 1):
        return Queue(stt);
    elif (i_t == i_g and j_t == j_g and search_tool == 2):
        return Queue(stt);
    else:
        return search_tool;
    
def Search(state):
    new_state = flagState(state)
    value = Queue(new_state)
    
    i,j = np.where(new_state == value)
    position_value = positionMath(i,j)
    epty_i,epty_j = np.where(new_state == 0)
    empty_position = positionMath(epty_i,epty_j)
    if (position_value == (empty_position + 3)):
        swapPosition(position_value,empty_position,new_state,value)
    elif (position_value == (empty_position - 3)):
        swapPosition(position_value,empty_position,new_state,value)
    elif (position_value == (empty_position + 1)):
        swapPosition(position_value,empty_position,new_state,value)
    elif (position_value == (empty_position - 1)):
        swapPosition(position_value,empty_position,new_state,value)
    return new_state;
    
def hF(actual_stt,goal_stt):
    h = 0
    for v in range (1,9):
        i_s,j_s = np.where(actual_stt == v)
        i_gs,j_gs = np.where(goal_stt == v)
        h = h + abs(i_s - i_gs) + abs(j_s - j_gs)
    return h;

    
while (True):
    next_search = Search(initial_search)
    if(hF(next_search,goal_state) > hF(initial_search,goal_state)):
        opt = [initial_search,Search(initial_search)]
        next_search = random.choice(opt)
    initial_search = next_search
    print(initial_search,hF(initial_search,goal_state))
    if(hF(initial_search,goal_state) == 0):
        break;




