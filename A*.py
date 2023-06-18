from queue import PriorityQueue

# Define the heuristic function (estimated distance from current node to goal node)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star(start, goal, graph):
    # Initialize the open and closed sets
    open_set = PriorityQueue()
    open_set.put((0, start))  # (f-score, node)
    came_from = {}  # Dictionary to store the path
    g_score = {node: float('inf') for node in graph}  # Cost from start to node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # Cost from start to node + heuristic
    f_score[start] = heuristic(start, goal)

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for neighbor in graph[current]:
            # Calculate the tentative g-score
            tentative_g_score = g_score[current] + graph[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                # This path is better than any previous one, so update the scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                # Add neighbor to the open set if it's not already there
                if neighbor not in [node[1] for node in open_set.queue]:
                    open_set.put((f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # Reverse the path to get it from start to goal


# Example usage
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start_node = 'A'
goal_node = 'F'

path = a_star(start_node, goal_node, graph)
if path is not None:
    print(f"Path found: {path}")
else:
    print("No path found.")
