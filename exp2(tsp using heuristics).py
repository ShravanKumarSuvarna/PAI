import heapq

def heuristic(current, goal):
    # Calculate the Euclidean distance between current and goal city
    return ((current[0] - goal[0])**2 + (current[1] - goal[1])**2) ** 0.5

def a_star(start, cities):
    # Priority queue to store the cities to be explored
    open_list = []
    # Closed set to store visited cities
    closed_set = set()
    # Dictionary to store the parent of each city
    parents = {}

    # Initialize the start city
    g = 0
    h = heuristic(start, cities[0])
    f = g + h
    heapq.heappush(open_list, (f, g, start))

    # Loop until all cities are visited
    while open_list:
        # Get the city with the smallest f value from the priority queue
        f, g, current = heapq.heappop(open_list)
        # Add the current city to the closed set
        closed_set.add(current)

        # If all cities are visited, return the path
        if len(closed_set) == len(cities):
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path

        # Explore neighbors of the current city
        for neighbor in cities:
            if neighbor != current and neighbor not in closed_set:
                # Calculate the cost to reach the neighbor
                g_neighbor = g + heuristic(current, neighbor)
                # Calculate the heuristic value for the neighbor
                h_neighbor = heuristic(neighbor, cities[0])
                # Calculate the f value for the neighbor
                f_neighbor = g_neighbor + h_neighbor

                # If the neighbor is not in the open list, or if the new path to the neighbor is shorter
                if (f_neighbor, g_neighbor, neighbor) not in open_list:
                    # Add the neighbor to the open list
                    heapq.heappush(open_list, (f_neighbor, g_neighbor, neighbor))
                    # Update the parent of the neighbor
                    parents[neighbor] = current

    return None

# Example usage
start_city = (0, 0)
cities_to_visit = [(1, 2), (3, 1), (2, 3), (1, 1)]
optimal_path = a_star(start_city, cities_to_visit)
print("Optimal path:", optimal_path)
