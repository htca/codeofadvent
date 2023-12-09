import numpy as np
import re
import pandas as pd
import math
from collections import Counter

text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()
sequences = []
for line in data:
    sequences.append([int(x) for x in list(line.strip().split())])

part1_total_alt = 0
for seq in sequences:
    cur_seq = seq
    part1_total_alt += cur_seq[-1]
    while len(set(cur_seq)) !=1:
        cur_seq = [cur_seq[i+1] - cur_seq[i] for i in range(len(cur_seq)-1) ]
        part1_total_alt += cur_seq[-1]
print("part1: " ,part1_total_alt)

part2_total_alt = 0
for seq in sequences[::-1]:
    cur_seq = seq
    save = [cur_seq[0]]
    while len(set(cur_seq)) !=1:
        cur_seq = [cur_seq[i+1] - cur_seq[i] for i in range(len(cur_seq)-1) ]
        save.append(cur_seq[0])
    save.append(0)
    save = save[::-1]
    val = 0
    for i in range(len(save)-1):
        val = save[i+1] - val
    part2_total_alt +=val
print("part2: " ,part2_total_alt)