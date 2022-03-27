import numpy as np
import os

class makeEnvironment():
    
    goal_state = list(np.char.replace(np.hstack(np.arange(1,10)).astype(str),'9',''))
    initial_state = np.array([[1,2,3,],[4,5,6],[7,8,0]])
    
    # Constructor shuffle board
    def __init__(self):

        self.current_state = self.initial_state.copy()
        self.shuffle()
        self.movs = [0,1,2,3]
        self.warning = ''
        self.color = '#f37874'
    # Prepare callbacks values
    def __call__(self):
        callback = np.char.replace(np.hstack(self.current_state).astype(str),'0','')
        return callback

    # Access values in current_state (Note:dx equals to board[i,j])
    def __getitem__(self,idx):
        return self.current_state[idx[0]][idx[1]]

    # Board size
    def __len__(self):
        return len(self.goal_state)
    
    # Shuffle current_state
    def shuffle(self):
        
        for _ in range(8):
            actions = self.actions_space()
            idx = np.random.randint(0,len(actions),1)[0]
            self.action(actions[idx])

        return self.current_state

    # Define the movement side
    def action(self, sample, state= None):
        if state is None:
            state = self.current_state

        side, i, j = sample
        if side == 0:
            return self.movement(i, j, state, column= -1)
        if side == 1:
            return self.movement(i, j, state, row= -1)
        if side == 2:
            return self.movement(i, j, state, column= 1)
        if side == 3:
            return self.movement(i, j, state, row= 1)

    # Define movement states
    def movement(self,i, j, state,row=0, column= 0):
    
        if state is None:
            state = self.current_state

        if state[i + row][j + column] == 0:
            state[i + row][j + column] = state[i][j]
            state[i][j] = 0
        
        return state

    
    # Show the possible actions
    def actions_space(self, state=None):
        if state is None:
            state = self.current_state

        i, j = np.hstack(np.where(state == 0))
        samples = [[0, i, j+1], [1, i + 1, j], [2, i, j - 1], [3, i - 1, j]]
        for idx, val in enumerate([0,2]):
            if i == val:
                samples.pop(3 - idx*2)
            if j == val:
                samples.pop(2 - idx*2)

        return samples
    
    def try_move(self, i, j, state= None):
        self.previous_state = list(self.__call__())
        for mov in self.movs:
            self.step([mov,i,j], state)

        if self.previous_state == list(self.__call__()):
            self.warning = 'Movimento Invalido!'
        elif self.goal_state == list(self.__call__()) :
            self.color = '#93ec70'
            self.warning = 'Parabéns você ganhou!'
        else:
            self.warning = ''

        
    def step(self, sample, state):

        samples = self.actions_space(state)

        for _sample in samples:
            if sample == _sample:
                return self.action(sample, state)
    
    def crawl(self,q):
        
        for act in self.actions_space(q):
            yield self.action(act, q.copy()) , act