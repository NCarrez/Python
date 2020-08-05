import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


def to_buffer(account_list):
    buffer = ""
    for account in account_list:
        buffer = buffer + account + "\n"
    buffer = buffer[:-1]
    return buffer

