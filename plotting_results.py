from importlib.resources import path
from turtle import width
import matplotlib.pyplot as plt
from matplotlib.widgets import Widget
import numpy as np
import pandas as pd
import random
from os import listdir
from os.path import isfile, join

PATH_KMEANS = 'CLUSTERING_KMEANS'
PATH_HIER = 'CLUSTERING_HIERARCHICAL'


#god_classes = get_names_god_classes()
god_classes = ['CoreDocumentImpl', 'XIncludeHandler', 'XSDHandler', 'DTDGrammar']
files_kmeans = [f for f in listdir(
    PATH_KMEANS) if isfile(join(PATH_KMEANS, f))]
files_hier = [f for f in listdir(PATH_HIER) if isfile(join(PATH_HIER, f))]
print(god_classes)


def plotting_clustering(path, method):
    range_plotting = range(2, 5)
    len_r_p = len(range_plotting)
    fig, ax = plt.subplots(nrows=3, ncols=len_r_p, figsize=(12, 10))
    counter_rows = 0
    counter_cols = 0

    for i in range_plotting:
        sizes = []
        count = -1
        for name in god_classes:
            count += 1
        #print("----- CLASS: "+name+" ----------------")

            df = pd.read_csv(path+method+str(i)+name+'.csv')

            size = (df['cluster_id'].value_counts())

            #print("K = " + str(i))
            # print(sizes)
            sizes.append([size.to_numpy().tolist(), i, name])
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)
            ax[counter_rows % 3][counter_cols].bar(
                range(i), sizes[count][0], color=color)
            counter_rows += 1

            ax[counter_rows % 3][counter_cols].set_title(
                "God Class: "+name+", K ="+str(i))
            ax[counter_rows % 3][counter_cols].set_ylabel('number')
            ax[counter_rows % 3][counter_cols].set_xlabel('cluster ids')
            ax[counter_rows % 3][counter_cols].set_xticks((range(i)))
        counter_cols += 1
        print(sizes)
    fig.tight_layout()

    plt.show()

    del df


path_sihoulette = 'SIHLOUETTE'
# df=pd.read_csv(path_sihoulette+'/'+)

#plotting_clustering(PATH_KMEANS, '/kmeans_k_')
#plotting_clustering(PATH_HIER, '/hier_k')
path = 'SIHLOUETTE/hier__k60'

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
row = -1
col =0


for name in god_classes:
    if(col%2==0):
        col=0
        row+=1
    
    df = pd.read_csv(path+name+'.csv')
    r = random.random()
    b = random.random()
    g = random.random()
    color = (r, g, b)
    ax[row][col].plot(df['k'], df['score'], color=color)

    ax[row][col].set_xlabel('K')
    ax[row][col].set_ylabel('Sihlouette Score')
    x, y = df['score'].idxmax(axis=0)+2, max(df['score'])
    ax[row][col].text(x, y, '%.2f' % y, ha='left', va='top')
    ax[row][col].scatter(x, y, color='black', s=20)
    ax[row][col].set_title(name)
    col+=1


fig.tight_layout()
plt.show()
fig.savefig('sihlouette.png')


# print(files_kmeans)
