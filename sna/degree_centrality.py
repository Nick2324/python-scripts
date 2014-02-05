'''
Created on 5/02/2014

@author: nicolas
'''

import networkx as net
import matplotlib.pyplot as plot
import main


def plot_histogram(p,n):
    histogram = plot.hist(p, n)
    plot.loglog(histogram[1][1:],histogram[0])
    plot.show()

if __name__ == '__main__':
    g = net.read_pajek('/media/Archivos/russians.net')
    degree = net.degree(g)
    sorted_degree = main.sorted_map(degree)
    print sorted_degree[:10]
    plot_histogram(degree.values(),100)
    