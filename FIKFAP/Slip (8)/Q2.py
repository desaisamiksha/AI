import heapq
import itertools


goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)


moves = {
    0: [1, 3], 
    1: [0, 2, 4], 
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            target_x, target_y = divmod(state[i] - 1, 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
    return distance


def astar(start_state):
    open_set = []
    came_from = {}
    g_score = {start_state: 0}
    f_score = {start_state: manhattan_distance(start_state)}
    heapq.heappush(open_set, (f_score[start_state], start_state))
    
    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal_state:
            return reconstruct_path(came_from, current)
        
        zero_index = current.index(0)
        for move in moves[zero_index]:
            new_state = list(current)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state = tuple(new_state)
            
            tentative_g_score = g_score[current] + 1
            
            if new_state not in g_score or tentative_g_score < g_score[new_state]:
                came_from[new_state] = current
                g_score[new_state] = tentative_g_score
                f_score[new_state] = tentative_g_score + manhattan_distance(new_state)
                heapq.heappush(open_set, (f_score[new_state], new_state))
    
    return []


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


start_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
solution_path = astar(start_state)
print("Solution path:")
for step in solution_path:
    print(step)