import networkx as nx
import subprocess
import matplotlib.pyplot as pl

mixes=[]
loops=[]

with open('1000+mix.txt', 'r') as my_file:
   for mix in my_file:
	 command1="grep ^%s,%s, output.txt|wc -l"%(str(int(mix)),str(int(mix)))
	 command2= "grep ,%s, output.txt|wc -l"%(str(int(mix)))
	 command3= "grep ^%s, output.txt|wc -l"%(str(int(mix)))
	 o1=subprocess.check_output(command1,shell=True)
         o2=subprocess.check_output(command2,shell=True)
	 o3=subprocess.check_output(command3,shell=True)

         total=int(o2)+int(o3)
         ratio=(total/int(o1))
         mixes.append(int(total))
         loops.append(ratio)

pl.plot(loops,mixes,'bs',linestyle='--')
pl.grid(True)
pl.title("Self Versus Total transactions of mixing sevices")
pl.xlabel("Total Transactions/Self transactions")
pl.ylabel("Total Transactions")
pl.show()
