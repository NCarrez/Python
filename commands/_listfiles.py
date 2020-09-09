import tools.file_explorer as fe

import sys, os


def print_files(path):
    """
    Function Descrition :
    Print file found from given path

    Function Arguments : 
    path : The full path to print files from

    Function Return : 
    None : None
    """
    res = fe.list_files(path)
    for line in res:
        print(line)
    print("-" * 20)
    print("\t" + str(len(res)) + " files")


if __name__ == "__main__":
    args = sys.argv
    paths = os.getcwd()
    if args[1:] != []:
        paths = args[1:]

    ### if not a list, transform to list
    if not isinstance(paths, list):
        t_path = paths
        paths = []
        paths.append(t_path)

    ### for each path prints the files
    for path in paths:
        if path[-1] != "\\":
            path = path + "\\"
        print("-> " + path)
        print_files(path)
        if path != paths[-1]:
            print("|" + "-" * 19)
            print()
