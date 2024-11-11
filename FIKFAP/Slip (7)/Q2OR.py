
HUMAN = -1
AI = +1


WIN_POSITIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]              
]


def evaluate(state):
    for pos in WIN_POSITIONS:
        if state[pos[0]] == state[pos[1]] == state[pos[2]]:
            if state[pos[0]] == AI:
                return +1
            elif state[pos[0]] == HUMAN:
                return -1
    return 0


def available_spots(state):
    return [i for i, val in enumerate(state) if val == 0]


def is_terminal(state):
    return evaluate(state) != 0 or all(val != 0 for val in state)


def minimax(state, depth, player):
    if is_terminal(state):
        return evaluate(state)

    if player == AI:
        best = -float('inf')
        for move in available_spots(state):
            state[move] = AI
            best = max(best, minimax(state, depth + 1, HUMAN))
            state[move] = 0
        return best
    else:
        best = float('inf')
        for move in available_spots(state):
            state[move] = HUMAN
            best = min(best, minimax(state, depth + 1, AI))
            state[move] = 0
        return best


def best_move(state):
    best_val = -float('inf')
    move = -1
    for spot in available_spots(state):
        state[spot] = AI
        move_val = minimax(state, 0, HUMAN)
        state[spot] = 0
        if move_val > best_val:
            best_val = move_val
            move = spot
    return move


initial_state = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]

move = best_move(initial_state)
print(f"The best move for AI is: {move}")