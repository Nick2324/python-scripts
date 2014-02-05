'''
Created on 25/01/2014

@author: nicolas
'''

import networkx as nx
import networkx.generators.small as ns
import networkx.algorithms.traversal as tr
import matplotlib.pyplot as pyplot

def dibujar_grafo(g):
    nx.draw(g)
    pyplot.show()

def guardar_grafo(g,path):
    nx.write_pajek(g, path)
    
def sorted_map(map):
    ms = sorted(map.iteritems(), key=lambda (k,v): (-v,k))
    return ms

def trim_degrees(g,degree=1):
    d = nx.degree(g)
    for n in g.nodes():
        if d[n] <= degree:
            g.remove_node(n)
    return g

def podar_red_hasta(g, n_nodos):
    for i in range(1,10):
        g = trim_degrees(g, i)
        if len(g) <= n_nodos:
            break
    return g

if __name__ == '__main__':
    g = ns.krackhardt_kite_graph()
    print g.number_of_edges()
    print g.number_of_nodes()
    print g.adjacency_list()
    print g.edges()
    print dict((x, g.neighbors(x)) for x in g.nodes())
    print list(tr.bfs_edges(g,0))
    print list(tr.dfs_edges(g,0))
    nx.draw_circular(g)
    #nx.draw_graphviz(g)