import random

tournament_size = 10

def roulette_wheel_selection(population):
    roulette_wheel = construct_roulette_wheel(population)
    selector = random.uniform(0, 1)
    keys = sorted(roulette_wheel.keys())
    for key in keys:
        if key >= selector:
            return roulette_wheel[key]
def construct_roulette_wheel(population):
    for individual in population.individuals:
        current_prob = 0
        wheel = dict()
        attribute = Individual.fitness() / Population.population_total_fitness()
        current_prob += attribute
        wheel[attribute] = individual
        return wheel

def tournament_selection(population):
    candidates = tournament_candidates(population)
    parent = fittest_in_tournament(candidates)
    return parent

def fittest_in_tournament(candidates):
    criteria = 0
    parent = None
    for individual in candidates:
        if individual.fitness > criteria:
            parent = individual
            criteria = individual.fitness
    return parent

def tournament_candidates(population):
    candidates = random.choices(population.individuals, k=tournament_size)
    return candidates