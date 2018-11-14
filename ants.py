from pandas import DataFrame
import sys
import os
import re
import random
import time
import gen_matrix
from aco import ACO
from graph import Graph

# Params
ants_factor = 0.8
iterations = 500
beta = 5.0
alfa = 1.0
rho = 0.99
Q = 0.5

# matrix = gen_matrix.generate("gr17.tsp", 17, "lower")
# matrix = gen_matrix.generate("gr24.tsp", 24, "lower")
# matrix = gen_matrix.generate("gr48.tsp", 48, "lower")

matrix = gen_matrix.generate("si175.tsp", 175, "upper")
# matrix = gen_matrix.generate("si535.tsp", 535, "upper")
# matrix = gen_matrix.generate("si1032.tsp", 1032, "upper")
len_rows = len(matrix)
len_cols = len(matrix[0])

print(len_rows, len_cols)
print(DataFrame(matrix))
cost_matrix = []
for i in range(len_rows):
    row = []
    for j in range(len_rows):
        if i == j:
            row.append(matrix[i][j])
        elif matrix[i][j] != 0:
            row.append(matrix[i][j])
        else:
            row.append(matrix[j][i])
    cost_matrix.append(row)

t = time.process_time()
aco = ACO(int(ants_factor * len_rows), iterations, alfa, beta, rho, Q)
graph = Graph(cost_matrix, len_rows)
path, cost = aco.solve(graph)
elapsed_time = time.process_time() - t
print('custo: {}\nmelhor caminho: {}\ntempo: {}'.format(cost, path, elapsed_time))
