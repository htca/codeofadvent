import numpy as np
import re
import pandas as pd
import math
from collections import Counter
from collections import defaultdict
import matplotlib.path as mpath
import matplotlib.patches as mpatches

def parse_input(data):
    start = None
    edges = defaultdict(list)
    points = []
    fullmap = []
    for y, line in enumerate(data):
        row =[]
        for x, c in enumerate(line.strip()):
            if c == "S":
                start = (x, y)
                edges[(x, y)] = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            if c == "|":
                edges[(x, y)] = [(x, y - 1), (x, y + 1)]
            if c == "F":
                edges[(x, y)] = [(x, y + 1), (x + 1, y)]
            if c == "-":
                edges[(x, y)] = [(x + 1, y), (x - 1, y)]
            if c == "7":
                edges[(x, y)] = [(x - 1, y), (x, y + 1)]
            if c == "L":
                edges[(x, y)] = [(x + 1, y), (x, y - 1)]
            if c == "J":
                edges[(x, y)] = [(x - 1, y), (x, y - 1)]
            if c == ".":
                points.append([x,y])
            row.append(c)
        fullmap.append(row)
    return start, edges, points, fullmap

def get_loop(start, edges):
    current = start
    visited = set()
    loop = []

    while current not in visited:
        loop.append(current)
        visited.add(current)
        for target in edges.get(current, []):
            if current in edges.get(target, []) and target not in visited:
                current = target

    return loop



if __name__ == "__main__":
    from doctest import testmod
    from sys import stdin

    testmod()
    text_file = "assignment.txt"
    with open(text_file, "r") as file:
        data = file.readlines()
    start, edges, points, fullmap = parse_input(data)
    path = get_loop(start,edges)
    print("part 1: ",int(len(path)/2))
    # fullmap[1][1] = "F" # test1.txt
    # fullmap[2][0] = "F"  # test2.txt
    # fullmap[1][1] = "F"  # test3.txt
    # fullmap[4][12] = "F"  # test4.txt
    # fullmap[0][4] = "7"  # test5.txt
    fullmap[start[1]][start[0]] = "J"  # assignment.txt
    for i_row in range(len(fullmap)):
        for i_col in range(len(fullmap[i_row])):
            if not (i_col,i_row) in path:
                fullmap[i_row][i_col] = "."


    enclosed = 0
    for row in fullmap[1:-1]:
        if "." in row:
            for i_x in range(1, len(row)-1):
                if "." == row[i_x]:
                    count = row[:i_x].count("|") + row[:i_x].count("J") + row[:i_x].count("L")
                    if count % 2 != 0: enclosed +=1
    print("part 2: ", enclosed)
