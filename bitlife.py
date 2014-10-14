import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,uniform
import subprocess
import sys

G=nx.DiGraph()
G=nx.read_edgelist("toy.txt",delimiter=',', data=(('date',int),('btc',float),('txkey',int)))

lifetimes=[]

def find_life(d1,d2):
 #20130102162906
 #2013/01/02/162906
 d1=d1/1000000
 d2=d2/1000000
 day1=d1%100
 day2=d2%100
 d1=d1/100
 d2=d2/100
 month1=d1%100
 month2=d2%100
 d1=d1/100
 d2=d2/100
 year1=d1
 year2=d2
 
 seconds=(day2-day1)*86400+(month2-month1)*30*86400+(year2-year1)*365*30*86400
 return seconds  


with open('miners.txt', 'r') as my_file1:
 for miner in my_file1:
  print miner

  lives=[]
  with open('stores.txt', 'r') as my_file2:

  for store in my_file2:   
	  command1="grep ^%s, %s"%(str(int(miner)),"toy.txt")
	  command2="grep ,%s, %s"%(str(int(store)),"toy.txt")
	  o1=subprocess.check_output(command1,shell=True)
	  o2=subprocess.check_output(command2,shell=True)
	  date1 = int(str(o1).strip().split(',')[2])
	  date2 = int(str(o2).strip().split(',')[2])
      
  if(nx.has_path(G,str(int(miner)),str(int(store))) and date1<date2):	  
   life=find_life(date1,date2)         
   if(life!=0):
    lives.append(life)
	  
lives.sort()
lifetimes.append(np.average(lives))

print "MEAN"
print np.average(lifetimes)

plt.hist(lifetimes, histtype='stepfilled', color='y',alpha=0.5)
plt.title("Average Lifetime of Bitcoin")
plt.xlabel("Lifetime")
plt.ylabel("Frequency")
plt.legend()
plt.show()
