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


# %% [markdown]
# ### Get methods 

# %%

def get_methods(java_class_):
    array_of_methods=[]
    for i in java_class_.methods:
        array_of_methods.append(i.name)
    return (array_of_methods)

def get_fields(java_class_):
    array_of_fields=[]
    for i in java_class_.fields:
        for k in i.declarators:
            #print(k)
            if k.name not in array_of_fields:
                array_of_fields.append(k.name)
        
    return (array_of_fields)

def get_fields_accessed_by_method(method, fields):
    #print(method)
    tree=method
    array_of_fields_of_this_method=[]
    for i, node in tree.filter(javalang.tree.MemberReference):
        #print(node.member)
        if node.member not in fields and node.member not in array_of_fields_of_this_method:
            array_of_fields_of_this_method.append(node.member)
    return array_of_fields_of_this_method



def get_methods_accessed_by_method(method, methods):
    tree=method
    array_of_methods_of_this_method=[]
    for i, node in tree.filter(javalang.tree.MethodInvocation):
        #print(node.member)
        if( node.member in methods and node.member !=method.name):
            array_of_methods_of_this_method.append(node.member)
        #if node.member not in fields and node.member not in array_of_fields_of_this_method:
        #    array_of_fields_of_this_method.append(node.member)
    return array_of_methods_of_this_method



#java_god_class=god_class_names_final['node'].values[2]
#print(get_methods(java_god_class))
#print(god_class_names_final['path'].values[0])
#print(java_god_class.fields)
#print(get_fields(java_god_class))
#print(len(get_fields(java_god_class)))



#print(frame_final)




# %% [markdown]
# ## Second step, function that works with god classes passed to it

# %%
def second_step(java_god_class):
    
    #print(columns)
    frame_final={}
    frame_final=pd.DataFrame(frame_final)
    all_methods=get_methods(java_god_class)
    all_fields=get_fields(java_god_class)
    print("len of all methods: ", len(all_methods))
    print("len of all fields: ", len(all_fields))
    for i in all_methods:
        frame_final[i]=np.int64(np.zeros(len(all_methods)))
        
    for i in all_fields:
        frame_final[i]=np.int64(np.zeros(len(all_methods)))
    

    
    #frame_final.to_csv("./"+java_god_class.name + ".csv")
    #print(len(java_god_class.methods))
    #print(frame_final.info())
    print("num rows dataframe:", len(all_methods))
    for i in (java_god_class.methods):
    
        fields_accessed_by_method=get_fields_accessed_by_method(i, get_fields(java_god_class))
        methods_accessed_by_method=get_methods_accessed_by_method(i, get_methods(java_god_class))
        for j in frame_final.columns:
            frame_final.at[i.name, j]=np.int32(0)

        for field in fields_accessed_by_method:
            
            frame_final.at[i.name, field]=np.int32(1)
            
            

        for method in methods_accessed_by_method:
            
            frame_final.at[i.name, method]=np.int32(1)
            
        


    frame_final=frame_final.iloc[len(all_methods):]
    frame_final=frame_final.fillna(np.int64(0))

            
    #print(frame_final.info())
    #print(frame_final.std())
    #print("before removing zeros columns: ", len(frame_final.columns))
    frame_final=frame_final.loc[:, (frame_final != 0).any(axis=0)]
    #print("after removing zeros columns: ", len(frame_final.columns))
    from pathlib import Path
    path = Path("./"+java_god_class.name + ".csv")

    if path.is_file():
        print(f'The file {"./"+java_god_class.name + ".csv"} exists')
        os.remove("./"+java_god_class.name + ".csv")
        print("removing file...")
    else:
        print(f'The file {"./"+java_god_class.name + ".csv"} does not exist')
    
    #print(frame_final.info())
    frame_final=frame_final.astype('int32')
    frame_final.to_csv("./"+java_god_class.name + ".csv")

# %% [markdown]
# ## Here second step of the project starts!
# Iterating over all god classes

# %%
for cl in god_class_names_final['node'].values:
    second_step(cl)


