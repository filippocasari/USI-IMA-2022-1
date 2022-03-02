import javalang
import os

import pandas as pd
d={'class_name':[], 'methods_num':[]}
dataframe= pd.DataFrame(data=d)
import time
start=time.time()
for root, dirs, files in os.walk(".", topdown=False):
    
    for name in files:
      
      if(name.endswith(".java")):
        
        nome=os.path.join(root, name)
        data = open(nome).read()
        tree_tmp=javalang.parse.parse(data)
        
        for klass in tree_tmp.types:
            if isinstance(klass, javalang.tree.ClassDeclaration) and klass.name is not d['class_name']:
                name_class=klass.name
                
                d['class_name'].append(name_class)
                d['methods_num'].append(len(klass.methods))
    
dataframe=pd.DataFrame(d)
print(dataframe)
mean_num_methods=dataframe['methods_num'].mean()
std_num_methods=dataframe['methods_num'].std()
print("mean of methods= ", dataframe['methods_num'].mean())
print("std of methods= ", dataframe['methods_num'].std())

names_god=dataframe.loc[dataframe['methods_num']>(mean_num_methods+6*(std_num_methods))]

#print(names)
print("the God classes are: ")
for i in names_god["class_name"]:
    print(i, end='\n')
print("time of execution: ", time.time()-start, " seconds")

    


            
        



        

