import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)
    
from encrypt import encrypt
from uncrypt import uncrypt

def cryption(string_to_crypt, outfile=None):
    crypted_content = string_to_crypt
    if crypted_content.find('K=') != -1:
        return uncrypt(string_to_crypt, outfile)
    else :
        return encrypt(string_to_crypt, outfile)