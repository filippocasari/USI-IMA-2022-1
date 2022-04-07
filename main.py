from find_god_classes import return_output_first_step
from extract_feature_vectors import second_step, write_csv

god_class_names_final = return_output_first_step()

names = []
for cl in god_class_names_final['node'].values:
    frame, name = second_step(cl)
    write_csv(frame, name)
    names.append(name)


def get_names_god_classes():
    return names
