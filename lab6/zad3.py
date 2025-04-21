import numpy
import pygad

labirynth = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

gene_space = [0, 1]
num_genes = 144

def if_path_correct(i, j, checked, solution):
    if i == 10 and j == 10:
        return True
    checked.add((i, j))
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < 12 and 0 <= nj < 12 and solution[ni][nj] == 1 and (ni, nj) not in checked:
            if if_path_correct(ni, nj, checked, solution):
                return True
    return False

def fitness_func(ga_instance, solution, solution_idx):
    solution = numpy.reshape(solution, (12, 12))
    if solution[10][10] == 0 or solution[1][1] == 0:
        return -1000

    for i in range(12):
        for j in range(12):
            if labirynth[i][j] == 0 and solution[i][j] == 1:
                solution[i][j] = 0

    for i in range(12):
        for j in range(12):
            if solution[i][j] == 1:
                if solution[i+1][j] == 0 and solution[i][j+1] == 0 and solution[i-1][j] == 0 and solution[i][j-1] == 0:
                    return -1000

    if not if_path_correct(1, 1, set(), solution):
        return -1000

    arr = numpy.array(solution)
    fitness = numpy.sum(arr)

    if fitness > 30:
        return -fitness * 2
    return -fitness

sol_per_pop = 100
num_parents_mating = 40
num_generations = 20000
keep_parents = 2
mutation_percent_genes = [20, 5]

ga_instance = pygad.GA(
    gene_space=[0, 1],
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=144,  # 12x12
    parent_selection_type="tournament",
    keep_parents=keep_parents,
    crossover_type="uniform",
    mutation_type="adaptive",
    mutation_percent_genes=mutation_percent_genes,
)

# Uruchomienie algorytmu
ga_instance.run()

# Podsumowanie wyników
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Best solution fitness: {solution_fitness}")
print("Best solution reshaped:")
print(numpy.reshape(solution, (12, 12)))

# Wizualizacja
ga_instance.plot_fitness()

