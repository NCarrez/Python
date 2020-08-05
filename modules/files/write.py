import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from save import save
from encryption import encrypt    


def write(full_file_name, datas):
    datas = encrypt(datas)
    save(full_file_name, datas)