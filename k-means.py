from sklearn.cluster import KMeans
import pandas as pd

df=pd.read_csv('./XIncludeHandler.csv')
#print(df.head())

cf=KMeans(5)

print(f"Shape of my dataframe before dropping method names: {(df.shape)}")
method_names=df[df.columns[0]]
print(method_names)
df=df.drop(df.columns[0], axis=1)
print(df.shape)
array_1=df.values
print(array_1)

cf.fit(array_1)
labels=cf.labels_
print(cf.labels_)

my_dict = {k: [] for k in method_names}

count=-1
for key in my_dict:
    count+=1
    my_dict[key].append(labels[count])
print(my_dict)

cluster=pd.DataFrame(my_dict)
cluster.insert(0, column='method_name', value='cluster_id')
cluster=cluster.T
print(cluster.head)

cluster.to_csv('clustering_file.csv')
