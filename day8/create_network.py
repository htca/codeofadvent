import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8})
text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.readlines()
edges =[]
for line in data[2:]:
    point = line.strip().split("=")[0].strip()
    dirs = line.strip().split("=")[-1].strip()
    loc_1 = dirs.split(",")[0].replace("(","").strip()
    loc_2 = dirs.split(",")[-1].replace(")", "").strip()
    edges.append([point, loc_1])
    edges.append([point, loc_2])

g = nx.Graph()
g.add_edges_from(edges)
nx.spring_layout(g)
nx.draw(g,with_labels=True,arrows=True,arrowstyle="-|>",arrowsize=10)
plt.show()
