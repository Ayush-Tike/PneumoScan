import random
from .cnn_model import build_cnn

POP_SIZE = 6
GENERATIONS = 4
MUTATION_RATE = 0.2

def create_chromosome():

    return [
        random.choice([16,32,64]),
        random.choice([32,64,128]),
        random.choice([64,128,256]),
        random.choice([0.001,0.0005]),
        random.choice([0.2,0.3,0.4])
    ]

def create_population():

    return [create_chromosome() for _ in range(POP_SIZE)]

def fitness(chromosome):

    model = build_cnn(chromosome)

    # simulated fitness for demo
    import random
    acc = random.uniform(0.80,0.95)

    return acc

def selection(population,scores):

    sorted_pop = [x for _,x in sorted(zip(scores,population),reverse=True)]

    return sorted_pop[:2]

def crossover(parent1,parent2):

    point = random.randint(1,3)

    return parent1[:point] + parent2[point:]

def mutation(chromosome):

    if random.random() < MUTATION_RATE:

        gene = random.randint(0,4)

        chromosome[gene] = create_chromosome()[gene]

    return chromosome


def genetic_algorithm():

    population = create_population()

    best_solution = None
    best_score = 0

    for generation in range(GENERATIONS):

        scores = []

        for chromosome in population:

            score = fitness(chromosome)

            scores.append(score)

        parents = selection(population,scores)

        new_population = parents.copy()

        while len(new_population) < POP_SIZE:

            child = crossover(parents[0],parents[1])

            child = mutation(child)

            new_population.append(child)

        population = new_population

        gen_best = max(scores)

        if gen_best > best_score:

            best_score = gen_best

            best_solution = population[scores.index(gen_best)]

    return best_solution,best_score