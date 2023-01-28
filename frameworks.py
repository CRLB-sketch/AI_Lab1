######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Framework:
    - actions(s)
    - stepCost(s, a, s')
    - etc
"""
######################################################################################

from abc import ABC, abstractmethod
# from typing import override

# Definir el problema
class Framework(ABC):        
    def __init__(self, initial, goal = None) -> None:
        self.initial = initial
        self.goal = goal
        super().__init__()
    
    @abstractmethod
    def actions(self, state):
        ...
        
    @abstractmethod
    def result(self, state, action):
        ...       
              
    @abstractmethod
    def is_goal(self, state):        
        ...
    
    @abstractmethod
    def step_cost(self, state, actions, reach_state):
        ...
        
    @abstractmethod
    def path_cost(self, c, state1, action, state2):
        ...
            
# Definir el Laberinto en base a Framework
class Labyrinth(Framework):
    def __init__(self, matrix, goal = None) -> None:
        super().__init__(matrix, goal)
        
        # Vamos a almacenar el tamaño de la matriz dada
        self.height = len(matrix)
        self.width = max(len(matrix) for _ in matrix)
        
        # Paredes del laberinto
        self.laby_walls = []   
        self.goal = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if matrix[i][j] == 2:
                        # self.start = (i, j)
                        self.initial = (i, j)
                        row.append(False)
                    elif matrix[i][j] == 3:
                        self.goal.append((i, j))
                        row.append(False)
                    elif matrix[i][j] == 0:
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.laby_walls.append(row)
            
        self.solution = None # Guardar solucion
                
    # @override                
    def actions(self, state):        
        row, col = state
        
        # Definir las posibles acciones
        possible_actions = [
            ("UP", (row - 1, col)),
            ("DOWN", (row + 1, col)),
            ("LEFT", (row, col - 1)),
            ("RIGHT", (row, col + 1))
        ]
        
        # Vamos a asegurarnos que las acciones son validas
        acts = []
        for action, (x, y) in possible_actions:
            try:
                if not self.laby_walls[x][y]:
                    acts.append((action, (x, y)))
            except IndexError:
                continue
        return acts
        
    # @override        
    def result(self, state, action):
        ...
            
    # @override            
    def is_goal(self, state):
        return state == self.goal
    
    # @override    
    def step_cost(self, state, actions, reach_state):
        ...
        
    # @override        
    def path_cost(self, c, state1, action, state2):
        ...        