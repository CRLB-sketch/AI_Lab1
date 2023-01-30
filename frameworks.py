######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Framework: Clase Abstractas y Derivadas de este

Por medio de esta clase se puede crear mas frameworks con la misma base
"""
######################################################################################

from abc import ABC, abstractmethod
from overrides import override

from collections import deque
from node import Node

# Definir el problema
class Framework(ABC):        
    def __init__(self, initial, goal = None) -> None:
        self.initial = initial
        self.goal = goal
        self.explored = None
        self.explored_amount = 0
        self.solution = None
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
    def path_cost(self, c, state1, action, state2):        
        ...
                
# Definir el Laberinto en base a Framework
class Labyrinth(Framework):
    def __init__(self, matrix, goal = None) -> None:
        super().__init__(matrix, goal)
        
        # Vamos a almacenar el tamaño de la matriz dada        
        self.matrix = matrix
        self.height = len(matrix)
        self.width = max(len(matrix) for _ in matrix)
        self.goal = []
        
        # Definir punto de partida y las metas disponibles
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if matrix[i][j] == 2:
                        self.initial = (i, j)
                        row.append(False)
                    elif matrix[i][j] == 3:
                        self.goal = (i, j)
                        row.append(False)
                except IndexError:
                    row.append(False)
                        
    @override                
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
                if 0 <= x < self.height and 0 <= y < self.width and self.matrix[x][y] != 0:
                    acts.append((action, (x, y)))
            except IndexError:
                continue
        return acts
        
    @override        
    def result(self, state, action):
        # Keep track of number of states explored
        self.num_explored = 0
        
            
    @override            
    def is_goal(self, state):
        return state == self.goal
    
    @override
    def path_cost(self, c, state1, action, state2):        
        return c + 1