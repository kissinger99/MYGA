target = ""

class Individual:
    def __init__(self, genetics: str, target_string: str):
        global target

        if target == "":
            target = target_string

        self.genetics = genetics
        self.fitness = self.fitness_score()
    def fitness_score(self):
        score = 0
        genetic_breakdown = list(self.genetics)
        target_breakdown = list(target)
        for component_pos in range(len(genetic_breakdown)):
            if genetic_breakdown[component_pos] == target_breakdown[component_pos]:
                score += 1
        return score
    def __str__(self):
        return "Genetics: " + self.genetics + " | Fitness = " + str(self.fitness)