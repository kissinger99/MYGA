import random
from Individual import Individual
from Population import Population

crossover_probability = 0.98
def crossover(parent_1: Individual, parent_2: Individual, population: Population, method: str):
    prob = random.uniform(0,1)

    child_1 = parent_1
    child_2 = parent_2

    if prob <= crossover_probability:
        match method:
            case "Single":
                child_1, child_2 = one_point_crossover(parent_1, parent_2, Population)
            case "Double":
                child_1, child_2 = two_point_crossover(parent_1, parent_2, Population)
    return child_1, child_2

#ONE-POINT CROSSOVER
def one_point_crossover(parent_1: Individual, parent_2: Individual, population: Population):
    # select randomly one crossover point
    cop = random.randint(0, len(parent_1.genetics) - 1)
    #divide and swap
    child_1 = parent_1.genetics[:cop] + parent_2.genetics[cop:]
    child_2 = parent_2.genetics[:cop] + parent_1.genetics[cop:]

    population.individuals.append(child_1)
    population.individuals.append(child_2)

#TWO-POINT CROSSOVER
def two_point_crossover(parent_1: Individual, parent_2: Individual, population: Population):
    #select randomly two crossover points
    cop1 = random.randint(1, len(parent_1.genetics)-1)
    cop2 = random.randint(cop1, len(parent_1.genetics)-1)
    #divide and swap
    child_1 = parent_1.genetics[:cop1] + parent_2.genetics[cop1:cop2] + parent_1.genetics[cop2:]
    child_2 = parent_2.genetics[:cop1] + parent_1.genetics[cop1:cop2] + parent_2.genetics[cop2:]

    population.individuals.append(child_1)
    population.individuals.append(child_2)