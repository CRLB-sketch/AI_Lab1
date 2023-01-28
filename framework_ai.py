"""
Framework: (matriz como parametro)
    - actions(s)
    - stepCost(s, a, s')
    - etc
"""

from abc import ABC, abstractmethod

class Framework(ABC):        
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        super().__init__()
    
    @abstractmethod
    def actions(state):
        ...
        
    @abstractmethod
    def step_cost(state, actions, reach_state):
        ...
        
# Breadth First Search
class BFS(Framework):    
    def actions(state):
        return
            
    def step_cost(state, actions, reach_state):
        return

# Depth First Search
class DFS(Framework):
    def actions(state):
        return
            
    def step_cost(state, actions, reach_state):
        return
    