import numpy
import pygad

labirynth = [
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

gene_space = [0, 1, 2, 3]
num_genes = 30

def fitness_func(ga_instance, solution, solution_idx):
    x, y = 0, 0
    for move in solution:
        if move == 0 and x > 0 and labirynth[x - 1][y] == 1:
            x -= 1
        elif move == 1 and x < 9 and labirynth[x + 1][y] == 1:
            x += 1
        elif move == 2 and y > 0 and labirynth[x][y - 1] == 1:
            y -= 1
        elif move == 3 and y < 9 and labirynth[x][y + 1] == 1:
            y += 1

        if (x, y) == (9, 9):
            return 100

    dist = abs(9 - x) + abs(9 - y)
    return 100 - dist

sol_per_pop = 200
num_parents_mating = 20
num_generations = 400
mutation_percent_genes = 15

ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type="tournament",
    mutation_type="random",
    mutation_percent_genes=mutation_percent_genes,
)

# Uruchomienie algorytmu
ga_instance.run()

# Podsumowanie wyników
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Best solution fitness: {solution_fitness}")
print("Best solution reshaped:")
print(solution)

# Wizualizacja
ga_instance.plot_fitness()

