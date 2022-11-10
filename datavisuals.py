import pandas as pd, matplotlib.pyplot as plt

data=pd.read_csv('./visuals_data.csv')
head=list(data)
data=data.values.tolist()
df=pd.DataFrame(data,columns=head)
df.hist()
plt.show()