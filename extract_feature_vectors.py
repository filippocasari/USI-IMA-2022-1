# %% [markdown]
# ### Get methods

# %%
from sys import stdout
import javalang
import os
import pandas as pd
import numpy as np
from find_god_classes import return_name_god_classes

def get_methods(java_class_):
    array_of_methods = []
    for i in java_class_.methods:
        if(i.name not in array_of_methods):
            array_of_methods.append(i.name)
    return (array_of_methods)


def get_fields(java_class_):
    array_of_fields = []
    

    for i in java_class_.fields:
        for k in i.declarators:
            # print(k)
            if k.name not in array_of_fields:
                array_of_fields.append(k.name)

    return (array_of_fields)


def get_fields_accessed_by_method(method, fields):
    # print(method)
    tree = method
    array_of_fields_of_this_method = []

    for i, node in tree.filter(javalang.tree.MemberReference):
        # print(node.member)
        
        if (node.member in fields) and (node.member not in array_of_fields_of_this_method):
            array_of_fields_of_this_method.append(node.member)
    return array_of_fields_of_this_method


def get_methods_accessed_by_method(method, methods):
    tree = method
    array_of_methods_of_this_method = []
    for i, node in tree.filter(javalang.tree.MethodInvocation):
        # print(node.member)
        if(node.member in methods and node.member != method.name and node.member not in array_of_methods_of_this_method):
            array_of_methods_of_this_method.append(node.member)
        # if node.member not in fields and node.member not in array_of_fields_of_this_method:
        #    array_of_fields_of_this_method.append(node.member)
    return array_of_methods_of_this_method


# java_god_class=god_class_names_final['node'].values[2]
# print(get_methods(java_god_class))
# print(god_class_names_final['path'].values[0])
# print(java_god_class.fields)
# print(get_fields(java_god_class))
# print(len(get_fields(java_god_class)))


# print(frame_final)

def get_names_third_step(java_god_class):
    return java_god_class.names


def second_step(java_god_class):

    # print(columns)
    #frame_final = {}
    #frame_final = pd.DataFrame(frame_final)
    array_of_god_classes=return_name_god_classes()
    #print("names: ", array_of_god_classes)
    print(f"Analysing class: {java_god_class.name}")
    i=0
    for node, name in (java_god_class.filter(javalang.tree.ClassDeclaration)):
        
        if(name in array_of_god_classes):
            
            java_god_class = node
            break
        i+=1
        #print(name)
    print(i)
    all_methods = get_methods(java_god_class)
    all_fields = get_fields(java_god_class)
    print("len of all methods: ", len(all_methods))
    print("len of all fields: ", len(all_fields))
    df1 = {'name_method': all_methods}
    
    for i in all_methods:

        # frame_final[i]=pd.Series(np.int64(np.zeros(len(all_methods)))) # previus command
        df1[i] = np.int64(np.zeros(len(all_methods)))

    for i in all_fields:

        df1[i] = np.int64(np.zeros(len(all_methods)))
        # frame_final[i]=pd.Series(np.int64(np.zeros(len(all_methods))))
    
   
    frame_final = pd.DataFrame(df1)
   
    print("shape frame: ", frame_final.shape)
    
    row=-1
    duplicates=[]
    for i in (java_god_class.methods):
        
        if(i.name not in all_methods):
            continue
       
        duplicates.append(i.name)
        row+=1
        fields_accessed_by_method = get_fields_accessed_by_method(
            i, all_fields)
        methods_accessed_by_method = get_methods_accessed_by_method(
            i, all_methods)
        
        for field in fields_accessed_by_method:
           
            frame_final.loc[ frame_final['name_method'] == i.name, field] = np.int32(1)
        
        for method in methods_accessed_by_method:

            frame_final.loc[ frame_final['name_method'] == i.name, method] = np.int32(1)
    print(frame_final)
    #frame_final = frame_final.fillna(np.int64(0))
    #frame_final = frame_final[len(all_methods):]
    #frame_final = frame_final.loc[:,~frame_final.columns.duplicated()]
    
    frame_final_2 = frame_final.loc[:, (frame_final != 0).any()].copy()

    print("shape of frame before removing zeros: ", (frame_final.shape))
    print("shape of frame after removing zeros: ", (frame_final_2.shape))

    from pathlib import Path
    path = Path("./"+java_god_class.name + ".csv")

    if path.is_file():
        print(f'The file {"./"+java_god_class.name + ".csv"} exists')
        os.remove("./"+java_god_class.name + ".csv")
        print("removing file...")
    else:
        print(f'The file {"./"+java_god_class.name + ".csv"} does not exist')

    
    #frame_final_2 = frame_final_2.astype('int32')

    print("---------------------------------\n\n")
    '''
    print(
        f"number of columns for {java_god_class.name} is: {len(frame_final_2.columns)}")
    print(
        f"number of rows for {java_god_class.name} is: {len(frame_final_2.index)}")
    print("\n---------------------------------\n\n")
    '''
    return frame_final_2, java_god_class.name


def write_csv(frame, name):
    if(os.path.isdir('./CSV') == False):
        os.mkdir('./CSV')
    frame.to_csv("./CSV/"+name + ".csv")

    print(f"Csv of {name} was written succesfully ", file=stdout)
