import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


from get_file_version import get_file_version
from list_files import list_files
from list_folders import list_folders
