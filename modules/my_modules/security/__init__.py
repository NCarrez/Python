import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from get_caller import get_caller
from check_caller_authorization import check_caller_authorization