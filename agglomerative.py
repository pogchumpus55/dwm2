import csv,matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

with open('./agglo_data.csv', 'r') as file:
    data=list(csv.reader(file))
    del data[0]
file.close()

linkage_data = linkage(data, metric='euclidean',method='ward')
dendrogram(linkage_data,labels=[f'p{i+1}' for i in range(len(data))])
plt.title("Hierarchical Clustering : Aglomerative")
plt.show()