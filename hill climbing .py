import random

def hill_climbing(problem, max_iterations):
    current_state = problem.initial_state()
    for _ in range(max_iterations):
        neighbors = problem.get_neighbors(current_state)
        if not neighbors:
            break
        best_neighbor = max(neighbors, key=lambda state: problem.heuristic(state))
        if problem.heuristic(best_neighbor) <= problem.heuristic(current_state):
            break
        current_state = best_neighbor
    return current_state

# Example usage
class Problem:
    def initial_state(self):
        return random.randint(1, 100)
    
    def get_neighbors(self, state):
        return [state - 1, state + 1]
    
    def heuristic(self, state):
        return abs(state - 50)

problem = Problem()
max_iterations = 1000

solution = hill_climbing(problem, max_iterations)
print(f"Best solution found: {solution}")
