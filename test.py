from genlib import *

g = Genetics()
population = g.create_population(5)
for entity in population:
    print(entity)