import sys
import os
import re

def generate(filename, cities, mode):
    distances = []
    # reading file to get matrix
    for row in open(filename):
        if row[0] == ' ':
            #treat string to remove non_numerical chars
            row = row.split(" ")
            del row[0]
            row[-1] = re.sub('[^0-9]', '', row[-1])
            if row[-1] == '':
                del row[-1]
            #transform string to integer
            row = list(map(int, row))
            distances += row
    return insert_in_matrix(distances, cities, mode)

def insert_in_matrix(distances, cities, mode):
    if mode == "lower":
        return insert_lower(distances, cities, mode)
    else:
        return insert_upper(distances, cities, mode)

def insert_lower(distances, cities, mode):
    matrix = []; tmp_row = [];
    # insert to tmp_row until a zero is found
    for i in range(0, len(distances)):
        if distances[i] != 0:
            tmp_row.append(distances[i])
        else:
            tmp_row.append(distances[i])
            # add missing zeroes and append row to matrix
            tmp_row = add_zeroes(tmp_row, cities, mode)
            matrix.append(tmp_row)
            tmp_row = []
    return matrix

def insert_upper(distances, cities, mode):
    matrix = []; tmp_row = [];
    # insert in a row until a zero is found
    for i in range(0, len(distances)):
        if distances[i] != 0 and distances[i+1] == 0:
            tmp_row.append(distances[i])
            # add missing zeroes and append row to matrix
            tmp_row = add_zeroes(tmp_row, cities, mode)
            matrix.append(tmp_row)
            tmp_row = []
        else:
            tmp_row.append(distances[i])
    #insert last row of zeroes
    matrix.append([0] * cities)
    return matrix

def add_zeroes(row, cities, mode):
    zeroes = [0] * (cities - len(row))
    if mode == "lower":
        result = row + zeroes
    elif mode == "upper":
        result = zeroes + row
    return result
