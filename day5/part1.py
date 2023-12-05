import numpy as np
import re
import pandas as pd
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

seq = []
translater = {}
translater2 = {}
part = 1
for line in data:
    if "seeds:" in line:
        if part == 1:
            seeds = [int(x) for x in line.split(":")[-1].split()]
        else:
            seeddef = np.array([int(x) for x in line.split(":")[-1].split()])
            seeddef = seeddef.reshape((int(len(seeddef)/2),2))
            # seeds =np.array([])
            # for dd in seeddef:
            #     print(dd)
            #     seeds = np.hstack([seeds,np.arange(dd[0],dd[0]+dd[1])])
            #     seeds = np.unique(seeds)
    elif "map" in line:
        if len(seq) == 0:
            seq.append(line.split(" ")[0].split("-")[0])
        seq.append(line.split(" ")[0].split("-")[-1])
        item1 = line.split(" ")[0].split("-")[0]
        item2 = line.split(" ")[0].split("-")[-1]
        key = item1+item2
        translater[key] = [[],[]]
        translater2[key] = []
        print(key)
    elif len(line.strip()) > 2:
        startitem1 = int(line.split()[0])
        startitem2 = int(line.split()[1])
        length = int(line.split()[2])
        for i in np.arange(startitem1,startitem1+ length):
            translater[key][0].append(i)
        for i in np.arange(startitem2,startitem2+ length):
            translater[key][1].append(i)

memory = {}
for se in seq:
    memory[se] = []


m = 1
#try 1
lowest_loc = np.inf
for seed in seeds:
    curval = seed

    for i_item, item in enumerate(seq[:-1]):
        key = seq[i_item]+seq[i_item+1]

        translate_table = np.array(translater[key])
        if curval in np.array(translater[key][1]):
            index, = np.where(np.array(translater[key][1])==curval)
            curval = np.array(translater[key][0])[index][0]
        else:
            curval = curval
    if curval < lowest_loc:
        lowest_loc = curval
print(lowest_loc)


