# %%
import javalang
import os
import pandas as pd
import time

# %%
d={'class_name':[], 'methods_num':[]}
dataframe= pd.DataFrame(data=d)

# %%
start=time.time()
import numpy as np
array_of_paths={'name':[], 'path':[], 'node':[]}
for root, dirs, files in os.walk(".", topdown=False):
    
    for name in files:
      
      if(name.endswith(".java")):
        
        nome=os.path.join(root, name)
        
        data = open(nome).read()
        tree_tmp=javalang.parse.parse(data)
        
        for klass in tree_tmp.types:
            if isinstance(klass, javalang.tree.ClassDeclaration) and klass.name is not d['class_name']:
                name_class=klass.name
                array_of_paths['name'].append(name_class)
                array_of_paths['path'].append(nome)
                array_of_paths['node'].append(klass)
                d['class_name'].append(name_class)
                d['methods_num'].append(len(klass.methods))
print("time of execution: ", time.time()-start, " seconds")

# %%
dataframe=pd.DataFrame(d)
print(dataframe)
mean_num_methods=dataframe['methods_num'].mean()
std_num_methods=dataframe['methods_num'].std()
print("mean of methods= ", dataframe['methods_num'].mean())
print("std of methods= ", dataframe['methods_num'].std())

names_god=dataframe.loc[dataframe['methods_num']>(mean_num_methods+6*(std_num_methods))]


#print(names)


# %%
print("the God classes are: ")
for i in names_god["class_name"]:
    print(i, end='\n')




# %%
god_class_names=pd.DataFrame(data=array_of_paths)
#print(god_class_names['name'])
#print(names_god, end='\n******************')
god_class_names_final=god_class_names.loc[god_class_names['name'].isin(names_god['class_name'])]

print(god_class_names_final)
def return_output_first_step():
    return god_class_names_final







# %% [markdown]
# ## Second step, function that works with god classes passed to it

# %%




