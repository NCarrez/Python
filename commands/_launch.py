from system_tools.file_explorer import get_windows_drives, search_file
from subprocess import call
import os, sys


if __name__ == "__main__":
    args = sys.argv
    if args[1:] == []:
        exit((1, "Missing Argument", "Please add program name as parameter"))
    print("First time this exe is researched, please, be patient...")
    drives = get_windows_drives()
    print(drives)
    res = None
    for drive in drives:
        res = search_file(drive, args[1], ".exe")
        if res != None:
            break
    if len(res) != 1:
        index = -1
        while index == -1:
            print()
            print("which path to save ?")
            for i in range(len(res)):
                print("(" + str(i) + ") - " + res[i])
            index = int(input())
            if index < 0 or index > (len(res) - 1):
                print()
                print("PLEASE SELECT A VALUE IN THE AVAILABLE RANGE")
                index = -1
        res = res[index]
    else:
        res = res[0]
    exit(res)
