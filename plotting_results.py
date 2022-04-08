import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from os import listdir
from os.path import isfile, join

PATH_KMEANS='CLUSTERING_KMEANS'
PATH_HIER='CLUSTERING_HIERARCHICAL'


#god_classes = get_names_god_classes()
god_classes=['CoreDocumentImpl', 'XIncludeHandler', 'XSDHandler']
files_kmeans = [f for f in listdir(PATH_KMEANS) if isfile(join(PATH_KMEANS, f))]
files_hier = [f for f in listdir(PATH_HIER) if isfile(join(PATH_HIER, f))]
print(god_classes)

range_plotting=range(2, 5)
len_r_p=len(range_plotting)


fig, ax=plt.subplots(nrows=3, ncols=len(range_plotting), figsize=(12,10))
counter_rows=0
counter_cols=0
colors=["r", "b", "k"]
for i in range_plotting:
    sizes=[]
    count=-1
    for name in god_classes:
        count+=1
    #print("----- CLASS: "+name+" ----------------")
    
        df = pd.read_csv(PATH_KMEANS+'/kmeans__k'+str(i)+name+'.csv')
        size=(df['cluster_id'].value_counts())
        
        #print("K = " + str(i))
        #print(sizes)
        sizes.append([size.to_numpy().tolist(), i, name])
        r = random.random()
        b =     random.random()
        g =     random.random()
        color = (r, g, b)
        ax[counter_rows%3][counter_cols].bar(range(i), sizes[count][0], color=color)
        counter_rows+=1
        
        ax[counter_rows%3][counter_cols].set_title("God Class: "+name+", K ="+str(i))
        ax[counter_rows%3][counter_cols].set_ylabel('number')
        ax[counter_rows%3][counter_cols].set_xlabel('cluster ids')
        ax[counter_rows%3][counter_cols].set_xticks((range(i)))
    counter_cols+=1
fig.tight_layout()

print(sizes)
plt.show()

#print(files_kmeans)