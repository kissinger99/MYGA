from Individual import Individual
from statistics import mean

population_size = 10
class Population:
    def __init__(self):
        self.population = [] #I had it like this before and I had an error
        self.average = self.fitness_average()
    def random_population(self):
        for i in range(population_size):
            individual_random = Individual()
            self.population.append(individual_random)
        return self.population
    def fitness_average(self):
        sum_scores = 0
        for i in self.population:
            sum_scores += Individual.fitness
        return mean(sum_scores)
    def __str__(self):
        return "Population Fitness Average = " + str(self.average)

pop_one = Population()
pop_one.fitness_average()

print(pop_one)