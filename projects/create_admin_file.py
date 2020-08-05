import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)

import paths


admin_file = paths.admin_file_path


if __name__ == "__main__":
    from my_modules.encryption import cryption
    from my_modules.files import write
    from my_modules.accounts import account

    account_list = []
    auth_list = ['master_login','master_manager']
    authorizations = ''
    for auth in auth_list:
        authorizations = authorizations + auth + '\t'
    authorizations = authorizations[:-1]
    account_list.append(account(cryption('admin'),cryption('admin'),cryption(authorizations)))
    account_list.append(account(cryption('admin1'),cryption('admin1'),cryption(authorizations)))
    buffer = ''
    for account in account_list:
        buffer = buffer + str(account) + '\n'
    buffer = buffer[:-1]
    write(admin_file, buffer)