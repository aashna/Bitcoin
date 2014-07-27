from Utility import *

G=pgv.AGraph(strict=True,directed=True)
parse_graph(G,"mix.txt")
G.node_attr['shape']='circle'
G.edge_attr['color']='red'
G.draw("graph.png",prog='circo')


