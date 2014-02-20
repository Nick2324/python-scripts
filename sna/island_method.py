'''
Created on 17/02/2014

@author: nicolas
'''

import networkx as nx
import matplotlib.pyplot as plot
import main


def trim_edges(g,weight=1):
    g2 = nx.Graph()
    for f, to, edata in g.edges(data=True):
        if edata['weight'] > weight:
            g2.add_edge(f, to, edata)
    return g2


def island_method(g, iterations=5):
    weights= [edata['weight'] for f, to, edata in g.edges(data=True)]
    mn=int(min(weights))
    mx=int(max(weights))
    step=int((mx-mn)/iterations)
    return [[threshold, trim_edges(g, threshold)] for threshold in range(mn,mx,step)]

if __name__ == '__main__':
    g = nx.read_pajek('egypt_retweets.net')
    cc = nx.connected_component_subgraphs(g)[0]
    islands = island_method(cc)
    for i in islands:
        print i[0], len(i[1]), len(nx.connected_component_subgraphs(i[1]))
