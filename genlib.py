import random as r
import math
import copy


class Entity:
    def __init__(self):
        self.genes = []
        self.fitness = 0
        self.pick_probability = 0


class Genetics:
    def create_population(self, count: int) -> []:
        population = []
        for i in range(count):
            population.append(Entity())
        return population

    def set_pick_probability(self, population: [], target_entity: Entity):
        sum = 0
        for entity in population:
            sum += entity.fitness

        x = math.pow(math.e, target_entity.fitness)
        target_entity.pick_probability = x / sum

    def set_pick_probabilities(self, population: []):
        sum = 0
        for entity in population:
            sum += entity.fitness

        for entity in population:
            x = math.pow(math.e, entity.fitness)
            entity.pick_probability = x / sum

    def select_entity(self, population: []) -> Entity:
        index = 0
        r_num = r.random()

        while r_num > 0:
            r_num -= population[index].pick_probability
            index += 1

        index -= 1
        return copy.deepcopy(population[index])

    def select_population(self, population: [], count: int) -> []:
        new_population = []
        for i in range(count):
            new_population.append(self.select_entity(population))
        return new_population

    def mutate(self, population, mutationAmount: int, mutationRate: float, mutationValue: float):
        for entity in population:
            for i in range(mutationAmount):
                if r.random() <= mutationRate:
                    if r.random() > 0.5:
                        entity.genes[r.randrange(0, len(entity.genes))] += mutationValue
                    else:
                        entity.genes[r.randrange(0, len(entity.genes))] -= mutationValue
