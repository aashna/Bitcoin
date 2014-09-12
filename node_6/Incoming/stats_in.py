import sys
import numpy as np

btcs=[]

with open('sorted_clubbed_out_btc.txt', 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        btcs.append(float(columns[3]))

btcs.sort()

print("max")
print max(btcs)
print("min")
print min(btcs)
print("sum")
print sum(btcs)
print("avg")
print np.average(btcs)
print("median")
print np.median(btcs)
