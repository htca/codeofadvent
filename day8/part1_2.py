import numpy as np
import re
import pandas as pd
import math
from collections import Counter

class Pt2:
    def __init__(self, pos):
        self.start_pos = pos
        self.pos = pos
        self.steps = 0
        self.ends = dict()

    def __repr__(self):
        return f'Ghost at Position "{self.pos}"'

text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

route_c = [x for x in data[0].strip()]
conver = {"L":0,"R":1}
route = []
for dir in route_c:
    route.append(conver[dir])

pt2_paths =[]
pt2_finished =[]
points = {}
for line in data[2:]:
    point = line.strip().split("=")[0].strip()
    dirs = line.strip().split("=")[-1].strip()
    points[point] = [dirs.split(",")[0].replace("(","").strip(),dirs.split(",")[-1].replace(")", "").strip()]
    if len(points) == 1:
        start_route = point
    if point[-1] == 'A':
        pt2_paths.append(Pt2(point))
end_route = point


cur_point = "AAA"
route_index = 0
i = 0
while not  cur_point in "ZZZ":
    dir = route[route_index]
    cur_point = points[cur_point][dir]
    i+=1
    route_index += 1
    if route_index == len(route):
        route_index = 0

print(f'Part 1: {i}')
instructions = []
route_index = 0
while len(pt2_paths) != 0:
    if len(instructions) == 0:
        instructions = []
        for dir in route_c:
            instructions.append(conver[dir])
    dir = instructions.pop(0)
    for p in pt2_paths[:]:
        p.pos = points[p.pos][dir]
        p.steps += 1
        if p.pos[-1] == 'Z':
            p.ends[p.pos] = p.steps
            pt2_finished.append(p.steps)
            pt2_paths.remove(p)
print(f'Part 2: {math.lcm(*pt2_finished)}')
