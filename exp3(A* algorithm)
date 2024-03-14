import heapq

# Define the goal state
goal_state = (5, 3, 6, 7, 0, 2, 4, 1, 8)  # 0 represents the blank space

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            if tile != 0:  # Skip blank tile
                goal_row = (tile - 1) // 3
                goal_col = (tile - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
                
    return distance

# Define possible moves
def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor = list(state)
            neighbor[blank_index], neighbor[new_row * 3 + new_col] = neighbor[new_row * 3 + new_col], neighbor[blank_index]
            neighbors.append(tuple(neighbor))
            
    return neighbors

# A* search algorithm
def a_star_search(start_state):
    open_set = [(heuristic(start_state), start_state)]  # Priority queue
    g_score = {start_state: 0}
    parent = {start_state: None}

    while open_set:
        _, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]

        for neighbor in get_neighbors(current_state):
            tentative_g_score = g_score[current_state] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))
                parent[neighbor] = current_state

    return None  # No path found

# Test the solver
initial_state = (3, 7, 6, 5, 1, 2, 4, 0, 8)  # Initial state, 0 is the blank space
print("Intial state")
print(initial_state[0:3])
print(initial_state[3:6])
print(initial_state[6:9])
print()

solution = a_star_search(initial_state)

if solution:
    print("Solution found:")
    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found.")
