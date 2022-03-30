
import pandas as pd
import os
import numpy as np

path_csv='./CSV'
path_keywords='keywords.txt'
ground_truth_path="./GROUND_TRUTH"
metrics_path="./EVALUATION"
metrics_file_name='metrics_final.txt'

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
    
print("Ground truthfiles have been just created")
    
    
    
    
    
            
            
        
        
    
    