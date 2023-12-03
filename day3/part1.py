import numpy as np
import re
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()
delimiters = "["
#get delimiters:
dels = []
for line in data:
    for x in line.strip():
        if not x.isdigit() and not "." in x and x not in delimiters:
            delimiters += r"\{}".format(x)
            dels.append(x)
delimiters += "\.]"

class number:
    def __init__(self, number, line, pos, length):

        self.number = int(number)
        self.row = line
        self.col = pos
        self.length = length

    def getsliced(self,mat):
        self.min_col = max(0, self.col - 1)
        self.max_col = min(self.col + self.length + 1, len(mat[0]))
        self.min_row = max(0, self.row - 1)
        self.max_row = min(self.row + 2, len(mat))
        sliced_matrix = np.array([row[self.min_col:self.max_col] for row in mat[self.min_row:self.max_row]])
        self.area = sliced_matrix


nums = []
mat = []
for i_line, line in enumerate(data):
    numbers = [x for x in re.split(delimiters,line.strip()) if x!=""]
    mat.append(list(line.strip()))
    for num in numbers:
        pos = line.find(num)
        nums.append(number(num,i_line,pos,len(num)))

mat = np.array(mat)
for num in nums:
    num.getsliced(mat)


sum_of_parts = 0
for num in nums:
    for dls in dels:
        if dls in num.area:
            sum_of_parts += num.number
            break
print(sum_of_parts)

