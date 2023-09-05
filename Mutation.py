import random
from Individual import Individual

low_mutation_probability = 0.05
child_selection_probability = 0.5

def mutation(child_1: Individual, child_2: Individual):
    mutation_probability = random.uniform(0, 1)
    child = child_1

    if mutation_probability <= child_selection_probability:
        child = child_2

    if mutation_probability <= low_mutation_probability:
        return mutation_operators
def mutation_operators():
    functions = [swap_mutation, scramble_mutation, inversion_mutation]
    random_function = random.choice(functions)
    return random_function()

def swap_mutation(child: Individual):
    position_1 = random.randint(0, len(child.genetics) - 1)
    position_2 = random.randint(0, len(child.genetics) - 1)
    while position_2 == position_1:
        position_2 = random.randint(0, len(child.genetics) - 1)
    temp = child.genetics[position_2]
    child.genetics[position_2] = child.genetics[position_1]
    child.genetics[position_1] = temp

def scramble_mutation(child: Individual):
    position_1 = random.randint(0, len(child.genetics[0]) - 1)
    position_2 = random.randint(0, len(child.genetics[0]) - 1)
    if position_2 < position_1:
        position_1, position_2 = position_2, position_1
    subset = list(child.genetics[position_1:position_2 + 1])
    random.shuffle(subset)
    child.genetics[position_1:position_2 + 1] = ''.join(subset)

def inversion_mutation(child: Individual):
    position_1 = random.randint(0, len(child.genetics[0]) - 1)
    position_2 = random.randint(0, len(child.genetics[0]) - 1)
    if position_2 < position_1:
        position_1, position_2 = position_2, position_1
    subset = child.genetics[position_1:position_2 + 1]
    inversed_subset = subset[::-1]
    child.genetics[position_1:position_2 + 1] = inversed_subset