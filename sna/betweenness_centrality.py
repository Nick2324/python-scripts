'''
Created on 5/02/2014

@author: nicolas
'''

import networkx as net
import main
from matplotlib import pyplot

if __name__ == '__main__':
    g = net.read_pajek('/media/Archivos/russians.net')
    g = main.podar_red_hasta(g, 1000)
    bc = main.sorted_map(net.betweenness_centrality(g))
    print bc[:10]
    h = pyplot.hist(dict(bc).values())
    pyplot.show()
    