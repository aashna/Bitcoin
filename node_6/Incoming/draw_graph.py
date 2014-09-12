import networkx as nx
import matplotlib.pyplot as pl

G=nx.DiGraph()
G=nx.read_edgelist("sorted_clubbed_in.txt",delimiter=',', data=(('date',int),('btc',float),('txkey',int)))

node_sizes = []
labels={}

for u,v,d in G.edges(data=True):
 node_sizes.append( ( int(d['btc']) ))

for n in G.nodes():
 labels[n]=n

nx.draw_random(G, node_size = node_sizes,arrows=True)  
pl.draw()
pl.show()
