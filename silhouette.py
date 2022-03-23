


from statistics import mean
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
import pandas as pd
import os
from hierarchical import hier_clustering
from kmeans import kmeans_clustering
path='./CSV'
list_of_files=os.listdir(path)

path_for_silhouette='./SIHLOUETTE'
if(os.path.isdir(path_for_silhouette)==False):
        os.mkdir(path_for_silhouette)

def silhouette(path, make_csv=False):
    array_k=[]
    array_score_kmeans=[]
    array_score_hier=[]
    for k in range(2, 61,1):
        
        X, cluster=hier_clustering(path, k, True)
        array_k.append(k)
        out=silhouette_score(X, cluster['cluster_id'])
        array_score_hier.append(out)
        print(f"\nfor hierarchical clustering with k= {k} the shiluette score is: {out}\n")
        X, cluster=kmeans_clustering(path, k, True)
        
        out=silhouette_score(X, cluster['cluster_id'])
        array_score_kmeans.append(out)
        
        print(f"\nfor kmeans clustering with k= {k} the shiluette score is: {out}\n")
    kmeans_out_data=pd.DataFrame({'k': array_k, 'score': array_score_kmeans})
    hier_out_data=pd.DataFrame({'k': array_k, 'score': array_score_hier})
    if(make_csv==True):
        kmeans_out_data.to_csv(path_for_silhouette+'/kmeans_'+'_k'+str(k)+path)
        hier_out_data.to_csv(path_for_silhouette+'/hier_'+'_k'+str(k)+path)
    
for i in list_of_files:
    silhouette(i, True)
    
    
    
    
    