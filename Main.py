from Population import Population

if __name__ == "__main__":
    target = "with enough probability anything is possible"
    population_size = 50

    population = Population(population_size=population_size, target=target)
    population.initialize_population()
    population.print_population()
    print("Population avg fitness: ", population.population_fitness_average())