import numpy as np
import re
import pandas as pd
import math
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

times = [int(x) for x in data[0].split(":")[-1].split()]
distances = [int(x) for x in data[1].split(":")[-1].split()]
prod = 0
for time, distance in zip(times,distances):
    a = 1
    b = -time
    c = distance
    st_min = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    st_max = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    if st_min == int(st_min):
        st_min +=1
    if st_max == int(st_max):
        st_max -=1
    diff = math.floor(st_max) - math.ceil(st_min) + 1

    if prod ==0:
        prod = diff
    else:
        prod *= diff
print("part 1:",prod)

time = int(data[0].split(":")[-1].replace(" ",""))
distance = int(data[1].split(":")[-1].replace(" ",""))

a = 1
b = -time
c = distance
st_min = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
st_max = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
if st_min == int(st_min):
    st_min +=1
if st_max == int(st_max):
    st_max -=1
diff = math.floor(st_max) - math.ceil(st_min) + 1

print("part 2:",diff)