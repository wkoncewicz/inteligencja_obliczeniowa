import pygad
import time
import numpy

names = ["zegar", "obraz-pejzaż", "obraz-portret", "radio", "laptop",
         "lampka nocna", "srebrne sztućce", "porcelana", "figura z brązu",
         "skórzana torebka", "odkurzacz"]
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]

max_weight = 25
gene_space = [0, 1]

def fitness_func(ga_instance, solution, solution_idx):
    total_weight = numpy.sum(solution * weights)
    total_value = numpy.sum(solution * values)

    if total_weight > max_weight:
        return 0

    return total_value

sol_per_pop = 20
num_genes = len(values)

accuracy_count = 0
time_count = 0
for i in range(10):
    start = time.time()
    ga_instance = pygad.GA(
        gene_space=gene_space,
        num_generations=50,
        num_parents_mating=10,
        fitness_func=fitness_func,
        sol_per_pop=sol_per_pop,
        num_genes=num_genes,
        parent_selection_type="tournament",
        keep_parents=2,
        crossover_type="single_point",
        mutation_type="random",
        mutation_percent_genes=8,
        stop_criteria=["reach_1630"]
    )

    ga_instance.run()
    end = time.time()
    total_time = end - start
    time_count += total_time

    solution, solution_fitness, _ = ga_instance.best_solution()
    total_weight = numpy.sum(solution * weights)
    total_value = numpy.sum(solution * values)
    if total_value == 1630:
        accuracy_count += 1

print(f"Dokładność: {accuracy_count / 10 * 100}%")
print(f"Średni czas: {time_count / 10}")
# print("Najlepsze rozwiązanie (chromosom):", solution)
# print("Całkowita wartość:", total_value)
# print("Całkowita waga:", total_weight)
#
# print("\nWybrane przedmioty:")
# for i in range(len(solution)):
#     if solution[i] == 1:
#         print(f"- {names[i]} (wartość: {values[i]}, waga: {weights[i]})")
#
# ga_instance.plot_fitness()
