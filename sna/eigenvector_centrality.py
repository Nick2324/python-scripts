'''
Created on 17/02/2014

@author: nicolas
'''

import networkx as nx
import matplotlib.pyplot as plot

if __name__ == '__main__':
    g = nx.read_pajek('russians.net')
    ec = nx.eigenvector_centrality(g)
    print ec[:10]
    h = plot.hist(dict(ec).values())
    plot.show()