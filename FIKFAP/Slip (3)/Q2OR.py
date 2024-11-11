from queue import PriorityQueue


def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        start_idx = start.index(i)
        goal_idx = goal.index(i)
        distance += abs(start_idx // 3 - goal_idx // 3) + abs(start_idx % 3 - goal_idx % 3)
    return distance


def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3
    directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]  

    for new_row, new_col in directions:
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors


def a_star_8_puzzle(start, goal):
    open_set = PriorityQueue()
    open_set.put((0 + manhattan_distance(start, goal), 0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not open_set.empty():
        _, current_cost, current_state = open_set.get()

        if current_state == goal:
            path = []
            while current_state:
                path.append(current_state)
                current_state = came_from[current_state]
            path.reverse()
            return path

        for neighbor in get_neighbors(current_state):
            new_cost = current_cost + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                open_set.put((priority, new_cost, neighbor))
                came_from[neighbor] = current_state

    return None


start_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)  
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution_path = a_star_8_puzzle(start_state, goal_state)

if solution_path:
    print("Solution found!")
    for step in solution_path:
        print(step)
else:
    print("No solution exists.")