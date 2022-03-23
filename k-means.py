
from sklearn.cluster import KMeans
import pandas as pd
import os
path='./CSV'
path_for_saving_clustering='./CLUSTERING_KMEANS'
list_of_files=os.listdir(path)
#print(list_of_files)
if(os.path.isdir(path_for_saving_clustering)==False):
        os.mkdir(path_for_saving_clustering)
def clustering(path_file):
    
    df=pd.read_csv(path+'/'+path_file)
    #print(df.head())

    cf=KMeans(5)
    
    #print(f"Shape of my dataframe before dropping method names: {(df.shape)}")
    method_names=df[df.columns[0]]
    #print(method_names)
    df=df.drop(df.columns[0], axis=1)
    #print(df.head())
    #print(df.shape)
    array_1=df.values
    #print(array_1)

  

    cf.fit(array_1)
    labels=cf.labels_
    #print(cf.labels_)

    my_dict = {k: [] for k in method_names}
    #print(f"len method names: {len(method_names)} and len of labels: {len(labels)}")
    count=0
    for key in my_dict:
        
        my_dict[key].append(labels[count])
        count+=1
    #print(my_dict)

    cluster=pd.DataFrame(my_dict)
    cluster.insert(0, column='method_name', value='cluster_id')
    cluster=cluster.T
    #print(cluster.head)
    
    cluster.to_csv(path_for_saving_clustering+'/kmeans_'+path_file)


for i in list_of_files:
    #print(i)
    clustering(i)
#clustering(list_of_files[0])