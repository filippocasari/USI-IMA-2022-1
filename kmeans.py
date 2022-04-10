
from sklearn.cluster import KMeans
import pandas as pd
import os
path = './CSV'
path_for_saving_clustering = './CLUSTERING_KMEANS'
list_of_files = os.listdir(path)
# print(list_of_files)
if(os.path.isdir(path_for_saving_clustering) == False):
    os.mkdir(path_for_saving_clustering)


def kmeans_clustering(path_file, k=5, make_csv=False):

    df = pd.read_csv(path+'/'+path_file)
    #print(df.head())

    cf = KMeans(k)

    #print(f"Shape of my dataframe before dropping method names: {(df.shape)}")
    method_names = df[df.columns[0]]
    #print(method_names)
    #print(df.columns[0])
    df = df.drop(df.columns[0], axis=1)
    #print(df.head())
    # print(df.shape)
    array_1 = df.values
    #print(array_1)
    #print(df.tail())

    cf.fit(array_1)
    labels = cf.labels_
    # print(cf.labels_)

    '''my_dict = {k: [] for k in method_names}
    #print(f"len method names: {len(method_names)} and len of labels: {len(labels)}")
    count=0
    for key in my_dict:
        
        my_dict[key].append(labels[count])
        count+=1
    #print(my_dict)

    cluster=pd.DataFrame(my_dict)
    '''
    cluster = pd.DataFrame({'method_name': method_names, 'cluster_id': labels})

    # print(cluster.head)
    if(make_csv == True):
        cluster.to_csv(path_for_saving_clustering +
                       '/kmeans'+'_k_'+str(k)+path_file)
    return array_1, cluster, cf.inertia_


for i in list_of_files:
    # print(i)
    kmeans_clustering(i)
# clustering(list_of_files[0])
