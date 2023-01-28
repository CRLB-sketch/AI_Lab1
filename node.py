class Node():
    def __init__(self, state, parent = None, action = None, path_cost = 0) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        
    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node