import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)

from my_modules.files import read
from my_modules.accounts import from_buffer
import paths


admin_file = paths.admin_file_path

def check_login(username, password):    
    account_list = from_buffer(read(admin_file))   
    for account in account_list :
        if(account.isEqual(username, password)):
            return (True)
    return (False)