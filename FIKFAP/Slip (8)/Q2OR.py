import random
import numpy as np


cities = np.array([
    [0, 0], [1, 5], [5, 6], [6, 1],
    [7, 8], [10, 10], [10, 0], [15, 15]
])

def calculate_total_distance(tour):
    return np.sum([np.linalg.norm(cities[tour[i]] - cities[tour[i - 1]]) for i in range(len(tour))])

def create_initial_population(pop_size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]

def select_parents(population, fitness):
    idx = np.random.choice(range(len(population)), size=2, p=fitness/fitness.sum(), replace=False)
    return population[idx[0]], population[idx[1]]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [-1]*size
    child[start:end] = parent1[start:end]
    pointer = end
    for p in parent2:
        if p not in child:
            if pointer >= size:
                pointer = 0
            child[pointer] = p
            pointer += 1
    return child

def mutate(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(pop_size, num_cities, generations, mutation_rate):
    population = create_initial_population(pop_size, num_cities)
    for gen in range(generations):
        population = sorted(population, key=calculate_total_distance)
        fitness = np.array([1 / calculate_total_distance(ind) for ind in population])
        new_population = population[:2]  
        while len(new_population) < pop_size:
            parent1, parent2 = select_parents(population, fitness)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_solution = min(population, key=calculate_total_distance)
    return best_solution, calculate_total_distance(best_solution)


population_size = 100
generations = 200
mutation_rate = 0.1
num_cities = len(cities)

solution, distance = genetic_algorithm(population_size, num_cities, generations, mutation_rate)
print("Best solution found:", solution, "with total distance:", distance)