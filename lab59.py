# encoding=UTF-8
import functools
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g1 = graph()
g2 = digraph()
g3 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
            pass
        else:
            graph.node(n)
            pass
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
            pass
        else:
            graph.edge(*e)
    return graph


nodes1 = ['A', 'B', 'C']
edges1 = [('A', 'B'), ('A', 'C'), ('B', 'C')]

g1 = add_nodes(g1, nodes1)
g1 = add_edges(g1, edges1)
g1.render(".\\graph\\lab64-g1")

g2 = add_nodes(g2, nodes1)
g2 = add_edges(g2, edges1)
g2.render(".\\graph\\lab64-g2")

nodeA = ('A', {'label': 'Node A'})
nodeB = ('B', {'label': 'Node B'})
nodeC = ('C', {'label': u'中文'})
nodeD = ('D', {})
nodes2 = [nodeA, nodeB, nodeC, nodeD]
edge1 = (('A', 'B'), {'label': 'edge1'})
edge2 = (('A', 'C'), {'label': 'edge2'})
edge3 = (('B', 'C'), {'label': u'關聯1'})
edge4 = (('B', 'D'), {})
edges2 = [edge1, edge2, edge3, edge4]

g3 = add_nodes(g3, nodes2)
g3 = add_edges(g3, edges2)
g3.render(".\\graph\\lab64-g3")

styles = {
    'graph': {
        'label': u'某種關聯',
        'fontsize': '24',
        'fontcolor': '#882200',
        'bgcolor': '#FF88EE',
        'rankdir': 'TB',
        'fillcolor': '#C0FFEE'
    },
    'nodes':{
        'fontname':'Consolas',
        'shape':'box',
        'fontcolor':'green',
        'color':'black',
        'style':'filled',
        'fillcolor':'#EEFFC0'
    },
    'edges':{
        #'style':'dotted',
        'color':'#448822',
        'arrowhead':'open',
        'fontname':'Courier',
        'fontsize':'24',
        'fontcolor':'#882244',
        'penwidth':'2'
    }
}


def apply_style(graph, styles):
    graph.graph_attr.update(('graph' in styles
                             and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles
                            and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles
                            and styles['edges']) or {})
    return graph


g4 = apply_style(g3, styles)
g4.render('.\\graph\\lab64-g4')
