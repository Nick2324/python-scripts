'''
Created on 17/02/2014

@author: nicolas
'''

import networkx as nx
import matplotlib.pyplot as plot
import main


if __name__ == '__main__':
    g = nx.read_pajek('egypt_retweets.net')
    bieber = nx.ego_graph(g, 'justinbieber', radius=2)
    ghonim = nx.ego_graph(g, 'Ghonim', radius=2)
    print len(bieber), nx.average_clustering(bieber)
    print len(ghonim), nx.average_clustering(ghonim)