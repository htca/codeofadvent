import numpy as np
import re
import pandas as pd
import math
from collections import Counter
import itertools
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

def get_score(cards):

    unique_count = Counter(array)
    type = sorted(unique_count.values())[::-1]
    type_score = 0
    if type == [5]:
        print("five of a kind")
        type_score = 7
    elif type == [4, 1]:
        print("four of a kind")
        type_score = 6
    elif type == [3, 2]:
        print("full house")
        type_score = 5
    elif type == [3, 1, 1]:
        print("three of a kind")
        type_score = 4
    elif type == [2, 2, 1]:
        print("two pair")
        type_score = 3
    elif type == [2, 1, 1, 1]:
        print("one pair")
        type_score = 2
    elif type == [1, 1, 1, 1, 1]:
        print("High card")
        type_score = 1
    else:
        print("error")
    return type_score

def get_scor_part2(cards):
    if not "J" in cards:
        unique_count = Counter(cards)
        type = sorted(unique_count.values())[::-1]
        type_score = 0
        if type == [5]:
            type_score = 7
        elif type == [4, 1]:
            type_score = 6
        elif type == [3, 2]:
            type_score = 5
        elif type == [3, 1, 1]:
            type_score = 4
        elif type == [2, 2, 1]:
            type_score = 3
        elif type == [2, 1, 1, 1]:
            type_score = 2
        elif type == [1, 1, 1, 1, 1]:
            type_score = 1
        else:
            print("error")
    else:
        unique_count = Counter(array)
        n_J = unique_count['J']
        array_to_place = ["A", "K", "Q", "T",9,8,7,6,5,4,3,2]
        unique_subarrays = set()
        for combination in itertools.combinations_with_replacement(array_to_place, n_J):
            sorted_combination = tuple(sorted(str(element) for element in combination))
            unique_subarrays.add(sorted_combination)
        type_score =0
        for alternative in unique_subarrays:
            replacement_count = 0
            modified_array = []
            for item in array:
                if item == "J":
                    modified_array.append(alternative[replacement_count])
                    replacement_count += 1
                else:
                    modified_array.append(item)
            if get_scor_part2(''.join(modified_array)) > type_score:
                type_score = get_scor_part2(''.join(modified_array))
    return type_score



replace = {"A":14,"K":13,"Q":12, "J":-1, "T":10}
total_scores =[]
total_scores2 =[]
for line in data:
    array = line.split()[0]
    type_score2 = get_scor_part2(array)
    cards = [x for x in array]
    cards_replaced = [int(x) for x in [replace.get(item, item) for item in cards]]
    bet = int(line.split()[1])
    unique_count = Counter(array)
    type = sorted(unique_count.values())[::-1]
    # print(type)
    type_score = 0
    if type == [5]:
        type_score = 7
    elif type == [4,1]:
        type_score = 6
    elif type == [3,2]:
        type_score = 5
    elif type == [3,1,1]:
        type_score = 4
    elif type == [2,2,1]:
        type_score = 3
    elif type == [2,1,1,1]:
        type_score = 2
    elif type == [1,1,1,1,1]:
        type_score = 1
    else:
        print("error")
    scorecard = [type_score]
    scorecard2 = [type_score2]
    for c in cards_replaced:
        scorecard.append(c)
        scorecard2.append(c)
    scorecard.append(bet)
    scorecard2.append(bet)
    total_scores.append(scorecard)
    total_scores2.append(scorecard2)


sorted_array = np.array(sorted(total_scores, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5])))
sorted_array2 = np.array(sorted(total_scores2, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5])))

ranked_array = [(rank + 1, row) for rank, row in enumerate(sorted_array)]
ranked_array2 = [(rank + 1, row) for rank, row in enumerate(sorted_array2)]

totalscore = 0
for row in ranked_array:
    totalscore += row[0]*row[1][-1]
print("part 1:",totalscore)
totalscore2 = 0
for row in ranked_array2:
    totalscore2 += row[0]*row[1][-1]
print("part 2:",totalscore2)