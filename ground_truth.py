from ast import keyword
import pandas as pd
import os
import numpy as np
path_csv='./CSV'
path_keywords='keywords.txt'
ground_truth_path="./GROUND_TRUTH"
if(os.path.isdir(ground_truth_path)==False):
        os.mkdir(ground_truth_path)
list_of_files=os.listdir(path_csv)
#print(list_of_files)
path_result_step_third='./CLUSTERING_KMEANS/'
keywords = np.array(pd.read_csv(path_keywords)).ravel()
#print(keywords)

for i in list_of_files:
    data=pd.read_csv(path_csv+'/'+i)
    data.rename( columns={'Unnamed: 0' :'Name'}, inplace=True )
    methods=np.array(data['Name'])
    #print(methods)
    dictionary={'method_name':[], 'cluster_id':[]}
    
    for name_method in methods:
        counter=0
        flag=False
        for keyw in keywords:
            if((keyw) in name_method.lower()):
                dictionary['cluster_id'].append(counter)
                dictionary['method_name'].append(name_method)
                flag=True
                break
            counter+=1
        if(flag==False):
            dictionary['cluster_id'].append('None')
            dictionary['method_name'].append(name_method)
    ground_truth = pd.DataFrame(dictionary)
    ground_truth.to_csv(ground_truth_path+"/ground_truth_"+i)
    
    
    ######### CLUSTERING WITH KMEANS ###################
    '''From the third step I discovered that for Kmeans the best hyperparameter K is = 2
        I have just created all result files in dir SIHLOUETTE, I must just take the file with k=2
    
    '''
    
    data = pd.read_csv(path_result_step_third+'kmeans__k2'+i)
    print(data)
    
    
    
            
            
        
        
    
    