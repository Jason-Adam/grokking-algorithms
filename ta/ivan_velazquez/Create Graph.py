# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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


names0 = randstring(5, 25)  # 3905)


# Create Nodes
graph = {}

for name in names0:
    graph[name] = ""

# Create Edges
def createedges(dic):

    for name in dic.keys():
        x = 0
        edges = []
        while x < 6:
            temp = list(dic)
            try:
                edge = temp[temp.index(name) + 1 + x]
                edges.append(edge)
            except (ValueError, IndexError):
                edge = ""
                edges.append(edge)
            x = x + 1
        else:
            dic[name] = edges


#print(names0)

createedges(graph)

pprint(graph)

