import networkx as nx

G=nx.DiGraph()
path='/home/aashna/Desktop/toy.txt'
f=open(path,'rb')

#parsing edge list into graph

G=nx.read_edgelist(path,comments='#',create_using=nx.DiGraph(),delimiter=',',nodetype=int,data=(('DATE',int),('BTC',float),('TxKey',int)),edgetype=None,encoding='utf-8')

prev_sender=-1

#calculating same sources in the graph

for u,v,d in G.edges(data=True):
 current_sender=u
 current_receiver=v
 if(current_sender==prev_sender):
  print "---------------"
  incoming=0
  for m,n,t in G.edges(data=True):
   if(current_sender==n):             #checking if the sender has received transactions before
     incoming+=G[m][n]['BTC'] #calculating total balance of sender 
     print "Incoming=%f"%incoming
  a=(G[current_sender][prev_receiver]['BTC'])
  b=(G[current_sender][current_receiver]['BTC']) 
  print "Outgoing=%f"%(a+b)
  if(incoming!=0):
   difference=incoming-(a+b)
   print "Difference=%f"%(difference)               #difference between BTC received and BTC spent
   if(difference<0.001):
    print("NODE FOUND!")
 prev_sender=current_sender
 prev_receiver=current_receiver

