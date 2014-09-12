###Some Linux Commands Used to Generate Files####

1. Sorting numerically
   sort -t ',' -k<column no.> -n <input file> > <output file>

2. Unique lines in input file
   awk -F, 'FNR==NR{a[$<column no.>]++; next} {if (a[$<column no.>]>1) {print}}' <input file> <input file> > <output file>

 
