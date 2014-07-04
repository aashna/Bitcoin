import networkx as nx

G=nx.DiGraph()
path='/home/aashna/Desktop/xyz.txt'
f=open(path,'rb')

G=nx.read_edgelist(path,comments='#',create_using=nx.DiGraph(),delimiter=',',nodetype=int,data=(('DATE',int),('BTC',float),('TxKey',int)),edgetype=None,encoding='utf-8')
#nx.write_edgelist(G,f)

print(G.edges(data=True))
print "No of edges=%d"%(G.number_of_edges())
print "Nodes"
print(G.nodes())
print "Out Degree"
print(G.out_degree())

print("Is strongly connected?")
print(nx.is_strongly_connected(G))
print "No of strongly connected components=%d"%(nx.number_strongly_connected_components(G))

#printing strongly connected subgraphs
print("Strongly connected subgraphs")
for sd in nx.strongly_connected_component_subgraphs(G):
  print(sd.edges(data=True))

print("Is weakly connected?")
print(nx.is_weakly_connected(G))
print "No of weakly connected components=%d"%(nx.number_weakly_connected_components(G))

#printing weakly connected components
print("Weakly connected subgraphs")
for wc in nx.weakly_connected_component_subgraphs(G):print(wc.edges(data=True))

