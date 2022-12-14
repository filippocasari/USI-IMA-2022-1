import javalang
import os
import pandas as pd
import time


d = {'class_name': [] , 'methods_num': []}

start = time.time()

array_of_paths = {'name': [], 'path': [], 'node': []}  # creating a 
number_methods=[]

for root, dirs, files in os.walk("./resources/"):

    for name in files:

        if(name.endswith(".java")):

            nome = os.path.join(root, name)
            
            data = open(nome).read()
            tree_tmp = javalang.parse.parse(data)
            #print(tree_tmp)
            for i, klass in tree_tmp.filter(javalang.tree.ClassDeclaration):
                name_class = klass.name
                
                '''
                if(name_class in d['class_name']):
                    print(f"name of file: {name}, name of the class: {name_class}")
                    #print("discarded because is already in the dict")

                if name.replace('.java', '') != name_class:
                    print(f"name of file: {name}, name of the class: {name_class}")
                    print("discarded because name of class and file do not match")'''
                #print("NAME: "+name)
                number_methods.append(len(klass.methods))
                if name.replace('.java', '') == name_class:
                    
                    
                    array_of_paths['name'].append(name_class)

                    array_of_paths['path'].append(nome)
                    
                    array_of_paths['node'].append(klass)
                    
                    d['class_name'].append(name_class)
                    d['methods_num'].append(len(klass.methods))
                    
                    
                    
import numpy as np
number_methods=np.array(number_methods)
print("time of execution: ", time.time()-start, " seconds")

# %%
dataframe = pd.DataFrame(d)
print(dataframe)
mean_num_methods = number_methods.mean()#dataframe['methods_num'].mean()
std_num_methods = number_methods.std()#dataframe['methods_num'].std()
print(f"mean of # methods= {mean_num_methods:.4f}" )
print(f"std of  # methods= {std_num_methods:.4f}" )
print(f"mean * (6*std): {mean_num_methods+(6.0*std_num_methods)}")
names_god_classes = dataframe.loc[dataframe['methods_num'] > (mean_num_methods+(6.0*std_num_methods))]

print("The God classes are: ")
for i, j  in zip(names_god_classes["class_name"],names_god_classes['methods_num']):
    print(f"Name: {i} with number of methods: {j}")

    
    

god_class_names = pd.DataFrame(data=array_of_paths)


god_class_names_final = god_class_names.loc[god_class_names['name'].isin(
    names_god_classes['class_name'])]

print(god_class_names_final)

def return_name_god_classes():
    return god_class_names_final['name']
    
def return_output_first_step():
    return god_class_names_final

