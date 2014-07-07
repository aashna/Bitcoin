import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

def parse_graph(G): 
 for line in open("toy.txt"):
  G.add_edge(line.strip().split(',')[0], line.strip().split(',')[1], Date=line.strip().split(',')[2], BTC=line.strip().split(',')[3],     TxKey=line.strip().split(',')[4])
 
def draw_graph(G):
 pos=nx.circular_layout(G)
 labels=nx.draw_networkx_labels(G,pos)
 draw_edges=nx.draw_networkx_edges(G,pos)
 #draw_edge_labels=nx.draw_networkx_edge_labels(G,pos)
 nodes=nx.draw_networkx_nodes(G,pos)
 plt.show()


