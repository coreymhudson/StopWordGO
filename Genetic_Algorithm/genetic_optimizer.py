'''Optimize the genetics'''
from random import sample, random, randint
from StopWordGO.Graph import algorithms as algos


def create_individual(sorted_nodes, rate):
    sorted_list = [x[0] for x in sorted_nodes]
    k = int(round(len(sorted_list) * rate))
    individual = sample(sorted_list, k)
    return individual


def create_population(pop_size, sorted_nodes, rate):
    return [create_individual(sorted_nodes, rate) for x in xrange(pop_size)]


def fitness(Graph, individual, target):
    duplicated = duplicate_and_reduce_graph(Graph, individual)
    score = algos.sparse_transitivity(duplicated)
    return abs(score - target)


def grade(Graph, population, target):
    summed = sum([fitness(x, target) for x in population])
    return summed / len(population)


def duplicate_and_reduce_graph(Graph, individual):
    Duplicated = Graph.copy()
    Duplicated.remove_nodes_from(individual)
    return Duplicated


def evolve(sorted_nodes, population, target, Graph, retain, random_select, mutate):
    graded = [(fitness(Graph, individual, target), individual) for individual in population]
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual) - 1)
            change_to = sample((set(sorted_nodes) - set(individual)), 1)
            individual[pos_to_mutate] = change_to
    parents_length = len(parents)
    desired_length = len(pop_size) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length - 1)
        female = randint(0, parents_length - 1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:half] + female[half:]
            seen = set()
            for count, node in enumerate(child):
                if node in seen():
                    change_to = sample((set(sorted_nodes) - set(child)), 1)
                    child[count] = change_to
                else:
                    seen.add(node)
            children.append(child)
    parents.extend(children)
    return parents


class Optimize(object):
    """Optimize graph"""
    def __init__(self, object, pop_size=100, rate=0.1, target=1.0, retain=0.2,
                 random_select=0.05, mutate=0.01):
        self.graph = object.graph
        self.initial_transitivity = object.transitivity
        self.sorted_nodes = algos.sort_by_degree(self.graph)
        self.pop_size = pop_size
