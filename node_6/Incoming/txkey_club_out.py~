total=0

entries = []
total_btc = []
with open('txkey_club_in.txt', 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if int(columns[4]) not in entries:
            entries.append(int(columns[4]))
            if total>0:
	 	    total_btc.append(total)
                    #print prev,total
            total=float(columns[3])                    
        else:
         total+=float(columns[3])
         prev=columns[4]

total_btc.append(total)

prev=0
      
if len(total_btc) > 0:
        with open('txkey_club_in.txt', 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if int(columns[4]) in entries:
                    index=entries.index(int(columns[4]))
                    if index!=prev:
                     print columns[0]+","+columns[1]+","+columns[2]+","+str(total_btc[index])+","+columns[4]
                    prev=index


                   


