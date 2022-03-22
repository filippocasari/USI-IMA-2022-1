from lab1 import return_output_first_step
from lab2 import second_step, write_csv

god_class_names_final=return_output_first_step()

for cl in god_class_names_final['node'].values:
    frame, name=second_step(cl)
    write_csv(frame, name)
    