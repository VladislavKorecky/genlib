from genlib import *

g = Genetics()
population = g.create_population(5)
for entity in population:
    entity.fitness = r.random()
    entity.genes.append(1)
    entity.genes.append(2)

g.set_pick_probabilities(population)
population = g.select_population(population, len(population))
g.mutate(population, 2, 0.5, 1)
population = g.crossover(population, len(population))