import numpy as np
import re
import pandas as pd
import math
from collections import Counter
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

replace = {"A":14,"K":13,"Q":12, "J":11, "T":10}
total_scores =[]
for line in data:
    print (line)
    array = line.split()[0]
    cards = [x for x in array]
    print(cards)
    cards_replaced = [int(x) for x in [replace.get(item, item) for item in cards]]
    print(cards_replaced)
    bet = int(line.split()[1])
    unique_count = Counter(array)
    type = sorted(unique_count.values())[::-1]
    print(type)
    type_score = 0
    if type == [5]:
        print("five of a kind")
        type_score = 7
    elif type == [4,1]:
        print("four of a kind")
        type_score = 6
    elif type == [3,2]:
        print("full house")
        type_score = 5
    elif type == [3,1,1]:
        print("three of a kind")
        type_score = 4
    elif type == [2,2,1]:
        print("two pair")
        type_score = 3
    elif type == [2,1,1,1]:
        print("one pair")
        type_score = 2
    elif type == [1,1,1,1,1]:
        print("High card")
        type_score = 1
    else:
        print("error")
    scorecard = [type_score]
    for c in cards_replaced:
        scorecard.append(c)
    scorecard.append(bet)
    total_scores.append(scorecard)
print(np.array(total_scores))
sorted_array = np.array(sorted(total_scores, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5])))
print(sorted_array)
ranked_array = [(rank + 1, row) for rank, row in enumerate(sorted_array)]
print(ranked_array)
totalscore = 0
for row in ranked_array:
    totalscore += row[0]*row[1][-1]
print(totalscore)