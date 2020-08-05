import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


from account import account


def from_buffer(buffer):
    account_list = []
    buffer = buffer.split("\n")
    for line in buffer:
        username, password, authorizations = line.split("\t")
        account_list.append(account(username, password, authorizations))
    return account_list

