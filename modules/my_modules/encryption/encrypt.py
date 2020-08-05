import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)
    

def encrypt(string_to_encrypt, out_file=None): 
    from cryptography.fernet import Fernet
    u_content = string_to_encrypt.encode('utf-8')

    crypt_key = ''
    fernet = ''
    e_content = ''
    while(True):
        crypt_key = Fernet.generate_key()
        fernet = Fernet(crypt_key)
        e_content = fernet.encrypt(u_content)
        if not (b'K=' in crypt_key 
            or b'K=' in e_content):
            break
    e_content = e_content+b'K='+crypt_key

    if(not out_file):
        return e_content.decode('utf-8')

    e_file = out_file
    file_to_write = open(e_file, 'wb')
    file_to_write.write(e_content)
    file_to_write.close()
    return e_file
