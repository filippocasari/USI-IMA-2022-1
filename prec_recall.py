
import pandas as pd
import os
import numpy as np

path_csv='./CSV'
path_keywords='keywords.txt'
ground_truth_path="./GROUND_TRUTH"
metrics_path="./EVALUATION"
metrics_file_name_kmeans='metrics_final_kmeans.txt'
metrics_file_name_hier='metrics_final_hier.txt'
list_of_files=os.listdir(path_csv)
path_result_step_third_kmeans='./CLUSTERING_KMEANS/'
path_result_step_third_hier='./CLUSTERING_HIERARCHICAL/'
keywords = np.array(pd.read_csv(path_keywords)).ravel()
######### CLUSTERING WITH KMEANS ###################
'''From the third step I discovered that for Kmeans the best hyperparameter K is = 2
        I have just created all result files in dir SIHLOUETTE, I must just take the file with k=2
    
'''

# NOTE: RESULTS will be in "EVALUATION" folder





def prec_recall_kmeans():
    for i in list_of_files:
        ground_truth=pd.read_csv(ground_truth_path+"/ground_truth_"+i)
        data = pd.read_csv(path_result_step_third_kmeans+'kmeans__k2'+i)
        #print(data)
        class_0=np.array(data.loc[data['cluster_id']==0]['method_name'])
        #print(class_0)
        class_1=np.array(data.loc[data['cluster_id']==1]['method_name'])
        list_of_tuple_class_0=set()
        for m in range(len(class_0)):
            for n in class_0[m+1:]:
                list_of_tuple_class_0.add((class_0[m], n))
        #print("Intra pairs class 0: \n ", list_of_tuple_class_0)
        
        list_of_tuple_class_1=set()
        for m in range(len(class_1)):
            for n in class_1[m+1:]:
                list_of_tuple_class_1.add((class_1[m], n))
        #print("Intra pairs class 1: \n ", list_of_tuple_class_1)
        intrapair_kmeans=list_of_tuple_class_0.union(list_of_tuple_class_1)
        list_of_files_ground_truth=set()
        #print(intrapair_kmeans)
        for m in range(15):
            
            list_tmp=np.array(ground_truth.loc[ground_truth['cluster_id']==m]['method_name'])
            for m in range(len(list_tmp)):
                for n in list_tmp[m+1:]:
                    list_of_files_ground_truth.add((list_tmp[m], n))
        
        ## for ground-truth 'None'
        list_tmp=np.array(ground_truth.loc[ground_truth['cluster_id']=='None']['method_name'])
        for m in range(len(list_tmp)):
            for n in list_tmp[m+1:]:
                list_of_files_ground_truth.add((list_tmp[m], n))
        
        string_for_writing=''
        precision=len(intrapair_kmeans.intersection(list_of_files_ground_truth))/len(intrapair_kmeans)
        name_class=i.replace(".csv", "")
        string_for_writing+=f"\nPrecision for { name_class } is : {precision}\n"
        
        recall=len(intrapair_kmeans.intersection(list_of_files_ground_truth))/len(list_of_files_ground_truth)
        
        string_for_writing+=f"\nRecall for {name_class} is : {recall}\n" 
        F1_score=2*(precision*recall)/(precision+recall)
        string_for_writing+=f"\nF1 score for {name_class} is : {F1_score}\n"
        print( string_for_writing)
        
        if(os.path.isdir(metrics_path)==False):
            os.mkdir(metrics_path)
            
            f=open(metrics_path+"/"+metrics_file_name_kmeans, 'w')
            f.write("\n########### FOR K-MEANS ###################\n")
            f.write(string_for_writing)
            f.write("\n###############################\n")
            f.close()
        else:
            
            f=open(metrics_path+"/"+metrics_file_name_kmeans, 'a')
            f.write("\n########### FOR K-MEANS ###################\n")
            f.write(string_for_writing)
            f.write("\n###############################\n")
            f.close()



def prec_recall_hier():
    for i in list_of_files:
        ground_truth=pd.read_csv(ground_truth_path+"/ground_truth_"+i)
        data = pd.read_csv(path_result_step_third_hier+'hier_k2_'+i)
        #print(data)
        class_0=np.array(data.loc[data['cluster_id']==0]['method_name'])
        #print(class_0)
        class_1=np.array(data.loc[data['cluster_id']==1]['method_name'])
        list_of_tuple_class_0=set()
        for m in range(len(class_0)):
            for n in class_0[m+1:]:
                list_of_tuple_class_0.add((class_0[m], n))
        #print("Intra pairs class 0: \n ", list_of_tuple_class_0)
        
        list_of_tuple_class_1=set()
        for m in range(len(class_1)):
            for n in class_1[m+1:]:
                list_of_tuple_class_1.add((class_1[m], n))
        #print("Intra pairs class 1: \n ", list_of_tuple_class_1)
        intrapair_kmeans=list_of_tuple_class_0.union(list_of_tuple_class_1)
        list_of_files_ground_truth=set()
        #print(intrapair_kmeans)
        for m in range(15):
            
            list_tmp=np.array(ground_truth.loc[ground_truth['cluster_id']==m]['method_name'])
            for m in range(len(list_tmp)):
                for n in list_tmp[m+1:]:
                    list_of_files_ground_truth.add((list_tmp[m], n))
        
        ## for ground-truth 'None'
        list_tmp=np.array(ground_truth.loc[ground_truth['cluster_id']=='None']['method_name'])
        for m in range(len(list_tmp)):
            for n in list_tmp[m+1:]:
                list_of_files_ground_truth.add((list_tmp[m], n))
        
        string_for_writing=''
        precision=len(intrapair_kmeans.intersection(list_of_files_ground_truth))/len(intrapair_kmeans)
        name_class=i.replace(".csv", "")
        string_for_writing+=f"\nPrecision for { name_class } is : {precision}\n"
        
        recall=len(intrapair_kmeans.intersection(list_of_files_ground_truth))/len(list_of_files_ground_truth)
        
        string_for_writing+=f"\nRecall for {name_class} is : {recall}\n" 
        F1_score=2*(precision*recall)/(precision+recall)
        string_for_writing+=f"\nF1 score for {name_class} is : {F1_score}\n"
        print( string_for_writing)
        
        if(os.path.isdir(metrics_path)==False):
            os.mkdir(metrics_path)
            
            f=open(metrics_path+"/"+metrics_file_name_hier, 'w')
            f.write("\n########### FOR K-HIERARCHICAL ###################\n")
            f.write(string_for_writing)
            f.write("\n###############################\n")
            f.close()
        else:
            
            f=open(metrics_path+"/"+metrics_file_name_hier, 'a')
            
            f.write(string_for_writing)
            f.write("\n###############################\n")
            f.close()
prec_recall_hier()
prec_recall_kmeans()

print("Exiting...")