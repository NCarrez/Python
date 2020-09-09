import os, sys


def search_file(path_to_search, filename, extension):
    res = []
    for root, dirs, files in os.walk(path_to_search):
        for file in files:
            if file.lower() == filename.lower() + extension.lower():
                res.append(root + "\\" + str(file))
    if res != []:
        return res
    return None
