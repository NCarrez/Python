from system_tools.file_explorer import get_user_path, get_windows_drives, search_file
from subprocess import call
import os, sys


def get_exe_path(app_name):
    ### Search executable on the system
    print("First time this exe is researched, please, be patient...")
    drives = get_windows_drives()
    res = None
    for drive in drives:
        ### Looking for an exe with the searched name
        res = search_file(drive, app_name, ".exe")
        if res != None:
            break
    ### If multiple answers, user must choose with one to save
    if len(res) != 1:
        index = -1
        while index == -1:
            print()
            print("which path to save ?")
            for i in range(len(res)):
                print("(" + str(i) + ") - " + res[i])
            index = int(input(">"))
            if index < 0 or index > (len(res) - 1):
                print()
                print("PLEASE SELECT A VALUE IN THE AVAILABLE RANGE")
                index = -1
        res = res[index]
    else:
        res = res[0]
    return res


if __name__ == "__main__":
    args = sys.argv
    ### Looking for args
    if args[1:] == []:
        exit((1, "Missing Argument", "Please add program name as parameter"))
    app_name = args[1]
    app_path = ""

    ### Creating variables
    user_path = get_user_path()
    commands_folder = os.path.join(user_path, "NC_commands")
    saved_file_path = os.path.join(commands_folder, "launch.sav")

    must_search = False
    ### Search saved file
    if not os.path.exists(saved_file_path):
        if not os.path.exists(commands_folder):
            try:
                os.mkdir(commands_folder)
            except:
                exit((1, "Can't create saving folder", ""))
    else:
        ### File already exists
        saved_file = open(saved_file_path, "r")
        saved_file_lines = saved_file.readlines()
        saved_file.close()
        for line in saved_file_lines:
            line_datas = line.split("\t")
            if line_datas[0] == app_name:
                app_path = line_datas[1]
                break

    if app_path == "":
        must_search = True
    if must_search:
        ### Search and save path
        res = get_exe_path(app_name)
        saved_file = open(saved_file_path, "a")
        saved_file.write(app_name + "\t" + res)
        saved_file.close()
        print("Saved path")
        app_path = res

    ### Launch App
    if args[2:] != []:
        exit(call(app_path, args[2:]))
    else:
        exit(call(app_path))

