from itertools import permutations

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    
    total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

def travelling_salesman_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = range(num_cities)

    
    all_possible_tours = permutations(cities)

    
    min_distance = float('inf')
    optimal_tour = None

    
    for tour in all_possible_tours:
        current_distance = calculate_total_distance(tour, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_tour = tour

    return list(optimal_tour), min_distance


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_tour, min_distance = travelling_salesman_bruteforce(distance_matrix)
print(f"Optimal tour: {optimal_tour}")
print(f"Minimal distance: {min_distance}")