import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)

import paths
from my_modules.files.read import read
from my_modules.accounts import from_buffer

admin_file = paths.admin_file_path


def get_admin_account_list():
    account_list = from_buffer(read(admin_file))
    return account_list
    pass
