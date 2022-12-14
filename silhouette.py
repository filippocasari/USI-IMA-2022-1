import sys
from sklearn.metrics import silhouette_score
import pandas as pd
import os
from hierarchical import hier_clustering
from kmeans import kmeans_clustering
path = './CSV'
import numpy as np
import matplotlib.pyplot as plt
list_of_files = os.listdir(path)

path_for_silhouette = './SIHLOUETTE'
if(os.path.isdir(path_for_silhouette) == False):
    os.mkdir(path_for_silhouette)


def silhouette(path, make_csv=False):
    array_k = []
    array_score_kmeans = []
    array_score_hier = []
    max_k_kmeans = 0
    max_k_hier = 0
    max_cluster_kmeans = -1
    max_cluster_hier = -1
    array_inertia_kmeans=[]
    
    for k in range(2, 61, 1):
        
        X, cluster = hier_clustering(path, k, True)
        array_k.append(k)
        out = silhouette_score(X, cluster['cluster_id'])

        if(out > max_cluster_hier):
            max_cluster_hier = out
            max_k_hier = k

        array_score_hier.append(out)
        #print(f"\nfor hierarchical clustering with k= {k} the shiluette score is: {out}\n")
        X, cluster, intertia_kmeans = kmeans_clustering(path, k, True)
        array_inertia_kmeans.append(intertia_kmeans)
        out = silhouette_score(X, cluster['cluster_id'])

        if(out > max_cluster_kmeans):
            max_cluster_kmeans = out
            max_k_kmeans = k
        array_score_kmeans.append(out)

        #print(f"\nfor kmeans clustering with k= {k} the shiluette score is: {out}\n")

    kmeans_out_data = pd.DataFrame({'k': array_k, 'score': array_score_kmeans})
    hier_out_data = pd.DataFrame({'k': array_k, 'score': array_score_hier})
    if(make_csv == True):
        kmeans_out_data.to_csv(path_for_silhouette+'/kmeans_'+'_k'+str(k)+path)
        hier_out_data.to_csv(path_for_silhouette+'/hier_'+'_k'+str(k)+path)
    return max_k_kmeans, max_cluster_kmeans, max_k_hier, max_cluster_hier, array_inertia_kmeans


def plot_intertia_kmeans(inertia, title):
    #print("len inertia: ", len(inertia))
    plt.figure(figsize=(12,8))
    title='intertia kmeans, '+title
    plt.plot(np.arange( 2,len(inertia)+2), inertia, 'o')
    plt.plot(np.arange(2, len(inertia)+2), inertia, '-', alpha=0.5)
    plt.xlabel('Number of Clusters'), plt.ylabel('Inertia')
    plt.title(title)
    plt.xticks(np.arange( 2,len(inertia)+2), rotation='vertical')
    plt.tight_layout()
    plt.show()


path_for_results = './RESULTS'
if(os.path.isdir(path_for_results) == False):
    os.mkdir(path_for_results)


csv = (input("Making CSV for clustering files? Write yes or no: "))
if(csv == 'yes'):
    csv = True
elif(csv == 'no'):
    csv = False
else:

    print("answer not allowed", file=sys.stderr)
    exit(-1)
print(f"Does Csv have to be written? {csv}")

txt = (input("Making a txt result files? Write yes or no: "))
if(txt == 'yes'):
    txt = True
elif(txt == 'no'):
    txt = False
else:

    print("answer not allowed", file=sys.stderr)
    exit(-2)
print(f"Does Txt result have to be written? {txt}")

assert(csv == True or csv == False)
assert(txt == True or txt == False)
for i in list_of_files:
    max_k_kmeans, max_cluster_kmeans, max_k_hier, max_cluster_hier, array_interia_kmeans = silhouette(
        i, csv)
    string = "\nFor god class "+str(i).replace('.csv', '')
    print("\nFor god class "+str(i).replace('.csv', ''))
    string += f'\nFor K-means, best score: {max_cluster_kmeans} with k= {max_k_kmeans}'
    print(
        f'For K-means, best score: {max_cluster_kmeans} with k= {max_k_kmeans}')
    
    print(
        f'For Hierarchical clustering, best score: {max_cluster_hier} with k= {max_k_hier}')
    string += f'\nFor Hierarchical clustering, best score: {max_cluster_hier} with k= {max_k_hier}'
    print("\n------------------------------------")

    with open('./RESULTS/final_results.txt', 'a') as f:
        f.write(string)
    plot_intertia_kmeans(array_interia_kmeans, str(i).replace('.csv', ''))





