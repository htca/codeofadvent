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

class sym_loc:
    def __init__(self, row,col,mat):
        self.row = row
        self.col = col

        self.min_col = max(0, self.col - 1)
        self.max_col = min(self.col + 1, len(mat[0]))
        self.min_row = max(0, self.row - 1)
        self.max_row = min(self.row + 2, len(mat))
        sliced_matrix = np.array([row[self.min_col:self.max_col] for row in mat[self.min_row:self.max_row]])
        self.area = sliced_matrix

nums = []
mat = []
for i_line, line in enumerate(data):
    numbers = [x for x in re.split(delimiters,line.strip()) if x!=""]
    mat.append(list(line.strip()))
    pos = 0
    for num in numbers:
        pos = line.find(num,pos)

        nums.append(number(num,i_line,pos,len(num)))
        pos+=len(num)

mat = np.array(mat)
for num in nums:
    num.getsliced(mat)

symbs = []
for i_row, row in enumerate(mat):
    for i_col, col in enumerate(row):
        if col in dels:
            symbs.append(sym_loc(i_row,i_col, mat))



sum_of_parts = 0
for num in nums:
    if num.number <=70:
        m=1
    for dls in dels:

        if dls in num.area:
            sum_of_parts += num.number
            break
print(sum_of_parts)

