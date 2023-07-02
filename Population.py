population_size = 10

class Population:
    def __init__(self):
        self.population = []
    def random_population(self):
        for i in range(population_size):
            individual_random = Individual()
            self.population.append(individual_random)
        return self.population
pop_one = Population()
pop_one.random_population()