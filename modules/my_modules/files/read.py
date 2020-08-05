import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)
    

from load import load
from my_modules.encryption import uncrypt    


def read(full_file_name):    
    buffer = load(full_file_name)
    buffer = uncrypt(buffer)
    return buffer
