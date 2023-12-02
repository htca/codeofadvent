text_file = "assignment2.txt"
with open(text_file,"r") as file:
    data = file.readlines()

total = 0
digitreplace = {'one':1, 'two':2, 'three':3, 'four': 4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for line in data:
    ints = []
    str_line = line
    print(line)
    positions = {key: line.find(key) for key in digitreplace.keys() if line.find(key) != -1}
    print(positions)
    sorted_keys = sorted(positions, key=positions.get)
    print(sorted_keys)
    for key in sorted_keys:
        str_line = str_line.replace(key, str(digitreplace[key]))
    firstints = []
    for x in str_line:
        if x.isdigit(): firstints.append(int(x))
    print(str_line,"\n")
    print(line)


    str_line = line
    for key in sorted_keys[::-1]:

        str_line = str_line.replace(key, str(digitreplace[key]))
    print(str_line,"\n")
    lastints = []
    for x in str_line:
        if x.isdigit(): lastints.append(int(x))
    print(firstints,lastints)
    total +=  firstints[0]*10 + lastints[-1]
print(total)