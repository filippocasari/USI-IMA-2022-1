# %% [markdown]
# ### Get methods

# %%
from sys import stdout
import javalang
import os
import pandas as pd
import numpy as np


def get_methods(java_class_):
    array_of_methods = []
    for i in java_class_.methods:
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
        if node.member not in fields and node.member not in array_of_fields_of_this_method:
            array_of_fields_of_this_method.append(node.member)
    return array_of_fields_of_this_method


def get_methods_accessed_by_method(method, methods):
    tree = method
    array_of_methods_of_this_method = []
    for i, node in tree.filter(javalang.tree.MethodInvocation):
        # print(node.member)
        if(node.member in methods and node.member != method.name):
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
    frame_final = {}
    frame_final = pd.DataFrame(frame_final)
    all_methods = get_methods(java_god_class)
    all_fields = get_fields(java_god_class)
    print("len of all methods: ", len(all_methods))
    print("len of all fields: ", len(all_fields))
    df1 = {}

    for i in all_methods:

        # frame_final[i]=pd.Series(np.int64(np.zeros(len(all_methods)))) # previus command
        df1[i] = np.int64(np.zeros(len(all_methods)))

    for i in all_fields:

        df1[i] = np.int64(np.zeros(len(all_methods)))
        # frame_final[i]=pd.Series(np.int64(np.zeros(len(all_methods))))

    # frame_final2=frame_final.copy()
    #del frame_final
    # frame_final=frame_final2.copy()
    frame_final = pd.DataFrame(df1)
    del df1

    #frame_final.to_csv("./"+java_god_class.name + ".csv")
    # print(len(java_god_class.methods))
    # print(frame_final.info())
    print("num rows dataframe:", len(all_methods))
    for i in (java_god_class.methods):

        fields_accessed_by_method = get_fields_accessed_by_method(
            i, get_fields(java_god_class))
        methods_accessed_by_method = get_methods_accessed_by_method(
            i, get_methods(java_god_class))
        for j in frame_final.columns:
            frame_final.at[i.name, j] = np.int32(0)

        for field in fields_accessed_by_method:

            frame_final.at[i.name, field] = np.int32(1)

        for method in methods_accessed_by_method:

            frame_final.at[i.name, method] = np.int32(1)

    frame_final = frame_final.iloc[len(all_methods):]
    frame_final = frame_final.fillna(np.int64(0))

    # print(frame_final.info())
    # print(frame_final.std())
    #print("before removing zeros columns: ", len(frame_final.columns))
    frame_final = frame_final.loc[:, (frame_final != 0).any(axis=0)].copy()
    #print("after removing zeros columns: ", len(frame_final.columns))
    from pathlib import Path
    path = Path("./"+java_god_class.name + ".csv")

    if path.is_file():
        print(f'The file {"./"+java_god_class.name + ".csv"} exists')
        os.remove("./"+java_god_class.name + ".csv")
        print("removing file...")
    else:
        print(f'The file {"./"+java_god_class.name + ".csv"} does not exist')

    # print(frame_final.info())
    frame_final = frame_final.astype('int32')

    print("---------------------------------\n\n")
    print(
        f"number of columns for {java_god_class.name} is: {len(frame_final.columns)}")
    print("\n---------------------------------\n\n")
    return frame_final, java_god_class.name


def write_csv(frame, name):
    if(os.path.isdir('./CSV') == False):
        os.mkdir('./CSV')
    frame.to_csv("./CSV/"+name + ".csv")

    print(f"Csv of {name} was written succesfully ", file=stdout)
