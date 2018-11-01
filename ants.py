from pandas import *
import sys
import os
import re
import random
import gen_matrix

ants = 5; beta = 1; alfa = 1;
#matrix = gen_matrix.generate("gr17.tsp", 17, "lower")
matrix = gen_matrix.generate("si175.tsp", 175, "upper")
len_rows = len(matrix)
len_cols = len(matrix[0])

print(len_rows, len_cols)
print(DataFrame(matrix))
