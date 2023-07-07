import random
import string

from Individual import Individual
from statistics import mean

class Population:
    def __init__(self, population_size: int, target: str):
        self.population_size = population_size
        self.target = target
        self.individuals = []

    def initialize_population(self):
        for i in range(self.population_size):
            genetics = self.random_genetic()
            self.individuals.append(Individual(genetics, self.target)) #why self.target?
    def random_genetic(self) -> str:
        genetic_choices = random.choices(string.ascii_lowercase + " ", k=len(self.target))
        genetics = "".join(genetic_choices)
        return genetics
    def print_population(self):
        for individual in self.individuals:
            print(individual)
    def population_fitness_average(self):
        scores = []
        for individual in self.individuals:
            scores.append(individual.fitness)
        return mean(scores)