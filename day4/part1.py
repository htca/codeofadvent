import numpy as np
import re
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()
tot_score = 0
# part 1
cardsdata ={}
for line in data:
    card = int(line.strip().split(":")[0].split(" ")[-1])
    cardsdata[card] = 1
    winningnumbers = line.strip().split(":")[1].split("|")[0].split()
    havingnumbers = line.strip().split(":")[1].split("|")[1].split()
    first = True
    score = 0
    for h_num in havingnumbers:
        if h_num in winningnumbers:
            if first:
                score = 1
                first = False
            else:
                score *=2
    tot_score +=score
print(tot_score)
print(len(data))

# part 2
for line in data:
    card = int(line.strip().split(":")[0].split(" ")[-1])
    winningnumbers = line.strip().split(":")[1].split("|")[0].split()
    havingnumbers = line.strip().split(":")[1].split("|")[1].split()
    score = 0
    for h_num in havingnumbers:
        if h_num in winningnumbers:
            score +=1
    for i in range(card+1,card+1 + score):
        if i in cardsdata.keys():
            cardsdata[i] += 1*cardsdata[card]
    print(cardsdata)
print(cardsdata)
totalcards =0
for key in cardsdata.keys():
    totalcards +=cardsdata[key]
print(totalcards)