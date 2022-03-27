from mimetypes import init
from typing import AbstractSet
from Puzzle8 import Puzzle8Environment
import numpy as np

class AStarSolver():

    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])

    def __init__(self, env):
        self.env = env
        self.init = self.env.current_state
        self.open_list, self.closed_list, self.f_list, self.h_list, self.g_list = [], [], [], [], []
        self.open_list.append(self.init)
        self.g_score = 0
        self.h = self.h_score(self.init)
        self.f = self.g_score + self.h
        self.parent, self.best_path = [], []
        self.h_list.append(self.h)
        self.g_list.append(self.g_score)
        self.f_list.append(self.f)
    
    def h_score(self,node):
        h= 0
        for i in range(len(node)):
            for j in range(len(node)):
            
                i_g, j_g = np.hstack(np.where(self.goal == node[i][j]))
                
                h+= abs(i_g - i)
                h+= abs(j_g - j)
        
        return h
    
    def create_node(self):
        self.node, self.g, self.h, self.f = self.open_list[-1], self.g_list[-1], \
                                            self.h_list[-1] , self.f_list[-1]

        for l in [self.open_list, self.h_list,self.g_list, self.f_list]:
            l.pop()

    def verify(self):
        for open, closed in zip([list(np.hstack(x)) for x in self.open_list], \
                                [list(np.hstack(y)) for y in self.closed_list]):
            if (list(np.hstack(self.node)) == open) or (list(np.hstack(self.node)) == closed):
                return False
        return True


    def forward(self):
        self.create_node()

        verified = self.verify()

        if verified:
            self.g_score +=1

            self.closed_list.append(self.node)

            for new_node, action in self.env.crawl(self.node):
                self.open_list.append(new_node)
                self.parent.append([new_node, self.node, action])

                new_h = self.h_score(new_node)
                new_f = self.g + new_h
                
                self.g_list.append(self.g_score)
                self.h_list.append(new_h)
                self.f_list.append(new_f)
            
            self.sort() 
        
              
    def sort(self):
        idxs = np.argsort(np.array(self.f_list), axis=0)[::-1]

        self.open_list = list(np.array(self.open_list)[idxs])
        self.h_list = list(np.array(self.h_list)[idxs])
        self.g_list = list(np.array(self.g_list)[idxs])
        self.f_list.sort(reverse=True)

    def backward(self):
   
        for child, parent, action in self.parent:
           
            if list(np.hstack(child)) == list(np.hstack(self.node)):
                self.node = parent
                self.best_path.append(action)
                break
    
    def search(self):
        while self.h != 0:
            self.forward()
        
        for _ in range(self.g): 
            self.backward()

        self.best_path.reverse()
        return self.best_path