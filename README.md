Bitcoin
===============
The code uses the tools and bitcoin dataset developed by http://compbio.cs.uic.edu/data/bitcoin/. It then parses "user_edges.txt" into a graph using Networkx module. Edges are created with attributes- date, number of bitcoins and transaction key. Finally, it prints information about the graph like edges, nodes, number of edges, indegree, outdegree, if the graph is strongly or weakly connected,number of strongly and weakly connected components and strongly and weakly connected subgraphs.

Steps:
1.Generate file user_edges.txt
2. Run "./run_user_edges.sh" to generate "output.txt"
3. "toy.txt"  is used in place of "output.txt" as sample data of 1000 transactions
4. Run "python Find_Graph_Stats.py"

To check for identity match, that is, distribution of balance among receivers keeping margin for error
Run python Chk_for_identity_match.py
