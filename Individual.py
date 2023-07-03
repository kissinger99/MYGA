import random
import string

genetic_length = 44

class Individual:
    def __init__(self):
        self.genetics = self.random_genetics()
        self.fitness = self.fitness_score()
    def random_genetics(self):
        random_string = ""
        for i in range(genetic_length):
            letters = string.ascii_lowercase + " "
            random_string = random_string + random.choice(letters)
        return random_string
    def fitness_score(self):
        score = 0
        target = "with enough probability anything is possible"
        for i in range(len(self.genetics)):
            if self.genetics[i] == target[i]:
                score += 1
        return score
    def __str__(self):
        return "Genetics: " + self.genetics + " | Fitness = " + str(self.fitness)
    def __repr__(self):
        return "Individual (Genetics: " + self.genetics + " | Fitness = " + str(self.fitness) + ")"