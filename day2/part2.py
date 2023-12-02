text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()

sum_of_games = 0
max_cubes = {"red":12, "green":13, "blue":14}
for line in data:
    gamevalid = True
    game = int(line.split(":")[0].split(" ")[-1])
    if game == 99:
        m = 1
    sets = line.split(":")[1].split(";")
    print(sets)
    set_dict_m = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        set_dict = {"red": 0, "green": 0, "blue": 0}
        subsets = set.split(",")
        for subset in subsets:
            set_dict[subset.strip().split(" ")[1]] += int(subset.strip().split(" ")[0])
        for key in set_dict.keys():
            if set_dict[key] > set_dict_m[key]:
                set_dict_m[key] = set_dict[key]
    print(set_dict_m)
    multiplied = set_dict_m["red"] * set_dict_m["blue"] * set_dict_m["green"]
    sum_of_games+=multiplied
print(sum_of_games)