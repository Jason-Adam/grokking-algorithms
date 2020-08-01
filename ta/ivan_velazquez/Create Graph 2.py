# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:02:14 2020

@author: ivan_
"""


import random
import string
from pprint import pprint


def randstring(length, size):
    item = [
        "".join(random.choices(string.ascii_letters, k=length)) for _ in range(size)
    ]
    item = list(set(item))
    if size != len(item):
        randstring(length, size)
    else:
        return item


names0 = randstring(5, 157)  # 3905)

# Define layers
names_layer1 = names0[0:5]
names_layer2 = names0[6:31]
names_layer3 = names0[32:157]
# names_layer4 = names0[158:783]
# names_layer5 = names0[784:3909]


# Create Nodes
graph = {}

for name in names0:
    graph[name] = ""

# Create Edges
def createedges(currentlayer, nextlayer):
    n = 0
    for name in currentlayer:
        x = 0
        edges = []
        while x < 5:
            # temp = list(dic)
            try:
                edge = nextlayer[0 + n]
                edges.append(edge)
            except (ValueError, IndexError):
                edge = "blank"
            x = x + 1
            n = n + 1
        else:
            graph[name] = edges


createedges(names_layer1, names_layer2)
createedges(names_layer2, names_layer3)

pprint(graph)

