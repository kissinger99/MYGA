import Crossover
import Mutation
import Selection
from Population import Population

if __name__ == "__main__":
    target = "with enough probability anything is possible"
    population_size = 50

    # POPULATION CREATION
    population = Population(population_size=population_size, target=target)
    population.initialize_population()
    population.print_population()
    print("Population avg fitness: ", population.population_fitness_average())

    # SELECTION ROULETTE WHEEL
    parent_1 = Selection.roulette_wheel_selection(population)
    parent_2 = Selection.roulette_wheel_selection(population)
    print("The Roulette Wheel method selected: ")
    print(parent_1)
    print(parent_2)

    # SELECTION TOURNAMENT
    parent_1 = Selection.tournament_selection(population)
    parent_2 = Selection.tournament_selection(population)
    print("The Tournament method selected: ")
    print(parent_1)
    print(parent_2)

    # ONE-POINT CROSSOVER
    child_1, child_2 = Crossover.crossover(parent_1, parent_2, Population, "Single")

    # MUTATION CHECK
    Mutation.mutation(child_1, child_2)