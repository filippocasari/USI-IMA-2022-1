from lab1 import return_output_first_step
from lab2 import second_step

god_class_names_final=return_output_first_step()

for cl in god_class_names_final['node'].values:
    second_step(cl)