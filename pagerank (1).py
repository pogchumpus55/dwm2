import networkx as nx, pylab as plt, pandas as pd

data=pd.read_csv('./rank_data.csv')
data=data.values.tolist()

D=nx.DiGraph()
D.add_weighted_edges_from(data)
pagerank=nx.pagerank(D)
for node in pagerank:
    print(f'Pagerank for {node} : {pagerank[node]}')
nx.draw(D,with_labels=True)
plt.show()