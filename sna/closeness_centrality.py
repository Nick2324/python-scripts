'''
Created on 5/02/2014

@author: nicolas
'''

import networkx as net
import matplotlib.pyplot as plot
import main

if __name__ == '__main__':
    g = net.read_pajek('/media/Archivos/russians.net')
    g = main.podar_red_hasta(g, 1000)
    cs = main.sorted_map(net.closeness_centrality(g))
    print cs[:10]
    h = plot.hist(dict(cs).values())
    plot.show()