from Individual import Individual
from statistics import mean

population_size = 10
class Population:
    def __init__(self):
        self.population = self.random_population()
        self.average = self.fitness_average()
    def random_population(self):
        population = []
        for i in range(population_size):
            individual_random = Individual()
            population.append(individual_random)
        return population
    def fitness_average(self):
        scores = []
        for individual in self.population:
            scores.append(individual.fitness)
        return mean(scores)

    def __str__(self):
        return "Population Fitness Average = " + str(self.average) + "\n" + \
            str(self.population)
    #why if I eliminate __repr__ in Individual I can't anymore see each Individual letters composition in the outcome?

pop_one = Population()

print(pop_one)