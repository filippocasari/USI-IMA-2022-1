
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import os
path = './CSV'
path_for_saving_clustering = './CLUSTERING_HIERARCHICAL'
list_of_files = os.listdir(path)
if(os.path.isdir(path_for_saving_clustering) == False):
    os.mkdir(path_for_saving_clustering)


def hier_clustering(path_file, k=5, make_csv=False):
    df = pd.read_csv(path+'/'+path_file)
    # print(df.head())

    cf = AgglomerativeClustering(k)

    #print(f"Shape of my dataframe before dropping method names: {(df.shape)}")
    method_names = df['name_method']
   
    df = df.drop(['name_method', 'Unnamed: 0'], axis=1)
    array_1 = df.values
    cf.fit(array_1)
    labels = cf.labels_
    # print(cf.labels_)

    cluster = pd.DataFrame({'method_name': method_names, 'cluster_id': labels})

    # print(cluster.head)
    if(make_csv == True):
        cluster.to_csv(path_for_saving_clustering +
                       '/hier_'+'k'+str(k)+'_'+path_file)
    return array_1, cluster


for i in list_of_files:
   
    hier_clustering(i)
