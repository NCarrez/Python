from os import listdir
from os.path import isfile, join


def list_files(path_to_list):
    return [f for f in listdir(path_to_list) if isfile(join(path_to_list, f))]
