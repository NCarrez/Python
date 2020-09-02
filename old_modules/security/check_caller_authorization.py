import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)

from get_caller import get_caller
from authorized import authorized_functions


def check_caller_authorization():
    caller = get_caller(3)
    if caller in authorized_functions:
        return True
    return False
