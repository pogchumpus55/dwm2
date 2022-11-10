import random 

datapoints=list(map(int,input("Enter the datapoints: ").split()))
k=int(input("Specify the number of clusters: "))
mean=[(random.randint(0,max(datapoints)))  for _ in range(k)] 

while True:
    near=list() 
    clusters=[list() for _ in range(k)] 
    for m in mean:
        near.append([abs(point-m) for point in datapoints])
    for i in range(len(datapoints)):
        calc=[near[j][i] for j in range(k)] 
        belongs=calc.index(min(calc)) 
        clusters[belongs].append(datapoints[i]) 
    nm=list()
    for cluster in clusters:
        try:
            nm.append(sum(cluster)/len(cluster)) 
        except:
            nm.append(0) 
    if nm==mean:
        break
    mean=nm

print("\nThe clusters formed are:")
for i in range(k):
    print(f"Cluster{i+1} : ",end="")
    print(*clusters[i])