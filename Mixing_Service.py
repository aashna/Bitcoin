from Utility import *

G=nx.DiGraph()
parse_graph(G,"toy.txt")

for n in G.nodes():
 if(Find_Mixing_Service(n,1000,1000,"toy.txt")):
  print n

