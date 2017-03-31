import csv
import networkx as nx
import matplotlib.pyplot as plt

with open('./csv/VOIES_NM.csv', newline='') as csvfile:
    lectureCsv = csv.reader(csvfile, delimiter=',')

    for ligne in lectureCsv:
        print(ligne)

print(lectureCsv)
G = nx.Graph()
G.add_node(1)
G.add_edge(1,2)
nx.draw(G)
nx.draw_spectral(G)
plt.show()
