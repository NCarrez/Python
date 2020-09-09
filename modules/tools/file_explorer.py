from win32api import GetFileVersionInfo, LOWORD, HIWORD
from os import listdir
from os.path import isfile, join


def list_files(path_to_list):
    return [f for f in listdir(path_to_list) if isfile(join(path_to_list, f))]


def list_folders(path_to_list):
    return [f for f in listdir(path_to_list) if isfolder(join(path_to_list, f))]


def get_file_version(fullfilename):
    try:
        info = GetFileVersionInfo(fullfilename, "\\")
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]
        return str(
            str(HIWORD(ms))
            + "."
            + str(LOWORD(ms))
            + "."
            + str(HIWORD(ls))
            + "."
            + str(LOWORD(ls))
        )
    except:
        return "Unknown version"
