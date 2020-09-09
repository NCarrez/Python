from os import listdir
from os.path import isdir, join


def list_folders(path_to_list):
    return [f for f in listdir(path_to_list) if isdir(join(path_to_list, f))]
