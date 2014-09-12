import networkx as nx
import matplotlib.pyplot as pl

G=nx.DiGraph()
G=nx.read_edgelist("0btc_in.txt",delimiter=',', data=(('date',int),('btc',float),('txkey',int)))
 
# positions for all nodes     
pos=nx.spring_layout(G) 

# nodes
nx.draw_networkx_nodes(G,pos,node_size=100)

nx.draw_networkx_edges(G,pos,arrows=True)
# labels
nx.draw_networkx_labels(G,pos,font_size=5,font_family='sans-serif')  
#nx.draw_networkx_edge_labels(G,pos)

pl.draw()
pl.show()
