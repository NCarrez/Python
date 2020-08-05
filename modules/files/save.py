import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


def save(full_file_name, datas):
    ofile = open(full_file_name, "w")
    ofile.write(datas)
    ofile.close()
