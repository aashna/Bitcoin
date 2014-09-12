import networkx as nx
import subprocess
import matplotlib.pyplot as pl

G=nx.DiGraph()
G=nx.read_edgelist("toy.txt",delimiter=',', data=(('date',int),('btc',float),('txkey',int)))

degree_list=[]
'''
for n in G.nodes():
 command="grep ^%s, %s|wc -l"%(n,"output.txt")
 o=subprocess.check_output(command,shell=True)
 print o
 #degree_list.append(o)

# print (n+","+o)
'''

#degree_list=[n for n in G.out_degree_iter()]
num=G.number_of_nodes()

degree_list = list(G.degree().values())
# compute and print average node degree
print ("Avg. Node Degree: %f" %
 (float(sum(degree_list))/num))
 
# generate a list degree distribution
degree_hist = nx.degree_histogram(G)

print ("Degree Fequency List:")
print ("Degree : # of Nodes")


# print the degree and number of nodes that have that degree
for degree,number_of_nodes in enumerate(degree_hist):
 print ("%i : %i" % (degree,number_of_nodes))
#else:
 #print ("Degree Frequency List Too Long to Print")

# generate x,y values for degree dist. scatterplot
x_list = []
y_list = []
for degree,num_of_nodes in enumerate(degree_hist):
 if num_of_nodes > 0:
  x_list.append(degree)
  y_list.append(num_of_nodes)
 
# label the graph
pl.title('Degree Distribution\nGNP Graph')
pl.xlabel('Degree')
pl.ylabel('Frequency')
 
# plot degree distribution
pl.scatter(x_list,y_list)
pl.show()






 
