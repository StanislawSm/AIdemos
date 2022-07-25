import numpy as np
import random
from utils import fitness


class Genetic:
    def __init__(self, coords, population_size=100, elite_size=10, mutation_rate=0.01):
        self.coords = coords
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            # 1/fitness -> change to maximization problem
            population_fitness[i] = 1/fitness(self.coords, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(self.coords))
            population.append(solution)

        return population

    def selection(self, population):
        result = []
        popFit = self.population_fitness(population)
        elite = []
        prob = {}
        probPrev = 0
        fitSum = sum(popFit.values())
        for k, v in popFit.items():
            if len(elite) <= 10:
                elite.append(k)
            prob[k] = probPrev + (v / fitSum)
            probPrev = prob[k]
        for i in range(0, self.population_size):
            if i < 10:
                result.append(population[elite[i]])
                continue
            rand = random.random()
            for k, v in prob.items():
                if rand <= v:
                    result.append(population[k])
                    break

        return result

    def crossover_population(self, population):
        children = []
        for i in range(0, self.population_size):
            children.append(population[i])
            if i < 10:
                continue
            j = (i + 1) % self.population_size
            r1 = random.randint(0, len(population[j]) - 2)
            r2 = random.randint(r1 + 1, len(population[j]) - 1)
            pivot = population[j][r1:r2]
            for p in pivot:
                children[i] = np.delete(children[i], np.where(children[i] == p))
            children[i] = np.concatenate([children[i][0: r1], pivot, children[i][r1:]])

        return children

    def mutate_population(self, population):
        mutation_rate = 0.1
        for j in range(0, self.population_size):
            if j <= 10:
                continue
            p = population[j]
            for j in range(0, len(p)):
                if random.random() <= mutation_rate:
                    swap = random.randint(0, len(p) - 1)
                    p[j], p[swap] = p[swap], p[j]
        return population

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
