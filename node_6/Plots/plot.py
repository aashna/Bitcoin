import matplotlib.pyplot as plt

Bitcoin = [] 
Timestamp=[]
Timestamp_labels=[]

months=["January","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]

file = open('6to447_sorted.txt', 'r') 
data = file.readlines() 
for i in range(1,len(data)-1): 
 date_string=""
 date=int(float(data[i].split(',')[2]))
 date=date/100000000
 month=date%100 
 Timestamp.append(month)
 Timestamp_labels.append(months[month-1])
 Bitcoin.append((float(data[i].split(',')[3]))) 

f=plt.figure()
ax=f.add_subplot(211)
ax.set_title('Plot between no. of Bitcoins and Month for 2012')
ax.set_xticks(Timestamp)
ax.set_xticklabels(Timestamp_labels)
ax.plot(Timestamp,Bitcoin,'r:^',linewidth=6.0,label="Bitcoins sent to node 447")
ax.annotate('Maximum Bitcoins',xy=(6,7.9), xytext=(2,7),arrowprops=dict(facecolor='black',shrink=0.05))
ax.legend(fontsize=11)

file = open('447to6_sorted.txt', 'r') 
data = file.readlines() 
for i in range(1,len(data)-1): 
 date_string=""
 date=int(float(data[i].split(',')[2]))
 date=date/100000000
 month=date%100 
 Timestamp.append(month)
 Timestamp_labels.append(months[month-1])
 Bitcoin.append((float(data[i].split(',')[3]))) 

ax=f.add_subplot(212)
ax.set_xticks(Timestamp)
ax.set_xticklabels(Timestamp_labels)
ax.plot(Timestamp,Bitcoin,'g:^',linewidth=6.0,label="Bitcoins received from node 447")
ax.annotate('Maximum Bitcoins',xy=(6,240), xytext=(3,180),arrowprops=dict(facecolor='black',shrink=0.05))

#ax.plot(B,A,'gx',label="Bitcoins")
ax.legend(fontsize=11)
ax.set_xlabel('Month')
ax.set_ylabel('Bitcoins')

plt.show()
