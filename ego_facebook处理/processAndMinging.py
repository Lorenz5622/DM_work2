import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from efficient_apriori import apriori
facebook = pd.read_csv(
    "dataset\\facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

gra = nx.from_pandas_edgelist(facebook, "start_node", "end_node")


pos = nx.spring_layout(gra, iterations=15, seed=2500)

colors = ["" for x in range(gra.number_of_nodes())]
counter = 0
for com in nx.community.label_propagation_communities(gra):
    color = "#%06X" % randint(0, 0xFFFFFF)
    counter += 1
    for node in list(
        com
    ):
        colors[node] = color
print(counter)

plt.figure(figsize=(15, 9))
plt.axis("off")
nx.draw_networkx(
    gra, pos=pos, node_size=10, with_labels=False, width=0.15, node_color=colors
)
plt.savefig('result1.png')
plt.show()
