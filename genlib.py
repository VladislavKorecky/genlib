class Entity:
    def __init__(self):
        self.genes = []
        self.fitness = 0


class Genetics:
    def create_population(self, count: int):
        population = []
        for i in range(count):
            population.append(Entity())
        return population
