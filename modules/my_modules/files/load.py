import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)
    

def load(full_file_path):
    ofile = open(full_file_path)
    buffer = ofile.read()
    ofile.close()
    return buffer