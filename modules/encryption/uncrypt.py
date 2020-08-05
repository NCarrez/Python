import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


def uncrypt(string_to_uncrypt, out_file=None):
    from cryptography.fernet import Fernet

    e_content = string_to_uncrypt.encode("utf-8")

    e_content, crypt_key = e_content.split(b"K=")
    fernet = Fernet(crypt_key)
    u_content = fernet.decrypt(e_content)

    if not out_file:
        return u_content.decode("utf-8")

    u_file = out_file
    file_to_write = open(u_file, "wb")
    file_to_write.write(u_content)
    file_to_write.close()
    return u_file
