from collections import deque
from node import Node

# Breadth First Search
def bfs(framework):    
    frontier = deque([Node(framework.initial)]) # Definir Queue
    
    while frontier:
        node = frontier.popleft()
        if framework.is_goal(node.state):
            return node
        frontier.extend(node.expand(framework))
    return None
    
# Depth First Search
def dfs(framework):
    frontier = [Node(framework.initial)] # Stack
    
    explored = set()
    while frontier:
        
        if len(frontier) == 0:
            raise Exception("No hay solucion para esta matriz")
                        
        node = frontier.pop()
        if framework.is_goal(node.state):
            print(node)
            return node
        frontier.extend(node.expand(framework))
        
    return None
    
# A*
def a_star(framework):
    ...