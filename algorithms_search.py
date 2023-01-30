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
    frontier = [Node(state=framework.initial, parent=None, action=None)] # Stack
    num_explored = 0

    explored = set()
    while frontier:
        
        if len(frontier) == 0:
            raise Exception("No hay solucion para esta matriz")
                        
        node = frontier.pop()
        num_explored += 1
        # Si dado caso se encuentra la meta entonces se retornara la solucion
        if framework.is_goal(node.state):
            print("JAJAJAJAJA")
            return node
        
        # Se guardaran todos los nodos explorados
        explored.add(node.state)

        for action, state in framework.actions(node.state):
            if not any(node.state == state for node in frontier) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.append(child)
        
    return None
    
# A*
def a_star(framework):
    ...