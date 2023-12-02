text_file = "assignment2.txt"
with open(text_file,"r") as file:
    data = file.readlines()

total = 0
replacements = {'one':1, 'two':2, 'three':3, 'four': 4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for line in data:
    occurrences = []
    for key in replacements.keys():
        start = 0
        while start < len(line):
            start = line.find(key, start)
            if start == -1:
                break
            occurrences.append((start, key))
            start += len(key)
    occurrences.sort(key=lambda x: x[0])
    str_line1 = line
    positions = {key: line.find(key) for key in replacements.keys() if line.find(key) != -1}
    sorted_keys = sorted(positions, key=positions.get)
    for key in sorted_keys:
        str_line1 = str_line1.replace(key,str(replacements[key]))
    firstints = []
    for x in str_line1:
        if x.isdigit(): firstints.append(int(x))

    str_line2 = line[::-1]
    reversed_keys = [key[::-1] for key in replacements.keys()]
    found_num = 2*len(str_line2)
    for i_key, key in enumerate(reversed_keys):
        if str_line2.find(key) !=-1:
            num = str_line2.find(key)
            if num < found_num:
                found_num = num
                found_key = key
                number = i_key+1
    str_line2 = str_line2.replace(found_key,str(number))[::-1]
    lastints = []
    for x in str_line2:
        if x.isdigit(): lastints.append(int(x))

    if firstints != lastints:
        print("line",line)
        print("str_line1", str_line1)
        print("str_line2", str_line2)
        print(firstints, lastints)
        print(firstints[0]*10 + lastints[-1])
    total +=  firstints[0]*10 + lastints[-1]
print(total)