import random
import numpy

inf = numpy.inf

def generator(amount):
    cases = []
    for i in range(amount):
        vertex_number = random.randint(2, 5)
        graph = [[inf for i in range(vertex_number)] for j in range(vertex_number)]

        for j in range(vertex_number):
            for k in range(vertex_number):
                if j !=k:
                    r = random.choices([True, False])[0]
                    if r:
                        cost = random.randint(1, 10)
                        graph[j][k] = cost
                else:
                    graph[j][k] = 0

        cases.append(graph)

    return cases

        

cases = generator(10)