import random
import string

from Individual import Individual

class Population:
    def __init__(self, population_size: int, target: str):
        self.population_size = population_size
        self.target = target
        Individual.set_target(self.target)
        self.individuals = []

    def initialize_population(self):
        for i in range(self.population_size):
            genetics = self.random_genetic()
            self.individuals.append(Individual(genetics))
    def random_genetic(self) -> str:
        genetic_choices = random.choices(string.ascii_lowercase + " ", k=len(self.target))
        genetics = "".join(genetic_choices)
        return genetics
    def print_population(self):
        for individual in self.individuals:
            print(individual)
    def population_total_fitness(self):
        total_score = 0
        for individual in self.individuals:
            total_score += individual.fitness
        return total_score
    def population_fitness_average(self):
        tot_fitness = self.population_total_fitness()
        return tot_fitness/self.population_size