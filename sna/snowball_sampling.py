'''
Created on 5/02/2014

@author: nicolas
'''

import networkx as net
import main
import urllib

def snowball_sampling(g, center, max_depth=1, current_depth=0, taboo_list=[]):
    #print center, max_depth, current_depth, taboo_list
    if max_depth == current_depth:
        return taboo_list
    else:
        taboo_list.append(center)
    read_lj_friends(g, center)
    for next_center in g.neighbors(center):
        taboo_list = snowball_sampling(g, next_center, max_depth=max_depth, \
                                           current_depth=current_depth+1, taboo_list=taboo_list)
    return taboo_list

def read_lj_friends(g, name):
    response=urllib.urlopen('http://www.livejournal.com/misc/fdata.bml?user=' + name)
    for line in response.readlines():
        if line.startswith('#'): 
            continue
        parts = line.split()
        if len(parts) == 0: 
            continue
        if parts[0] == '<':
            g.add_edge(parts[1],name)
        else:
            g.add_edge(name,parts[1])

if __name__ == '__main__':
    g = net.Graph()
    print snowball_sampling(g,raw_input(),int(raw_input()))
    main.guardar_grafo(g,raw_input())
    main.dibujar_grafo(g)