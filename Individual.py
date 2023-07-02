import random
import string

genetic_length = 44

class Individual:
    def __init__(self):
        self.genetics = self.random_genetics()
    def random_genetics(self):
        random_string = ""
        for i in range(genetic_length):
            letters = string.ascii_lowercase + " "
            random_string = random_string + random.choice(letters)
        return random_string

    def __str__(self):
        return "Genetics: " + self.genetics  # + " | Fitness = " + str(self.fitness)