# install graphviz
# add path
# C:\Program Files (x86)\Graphviz2.38\bin
# gvgen
# close pycharm, open again
# under terminal gvgen
# pip install graphviz

import graphviz as gv
import itertools

# g1 = gv.Graph(format='svg')
# g1 = gv.Digraph(format='svg')
# g1 = gv.Digraph(format='pdf')
g1 = gv.Digraph(format='png')
nodes = ['apple', 'samsung', 'htc', 'google']
for node in nodes:
    g1.node(node)
# edges = itertools.combinations(nodes,2)
edges = itertools.permutations(nodes, 2)
for n1, n2 in edges:
    g1.edge(n1, n2)
g1.render(".\\graph\\lab63")
