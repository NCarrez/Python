import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


python_path = os.path.join(file_path, "..")
admin_file_path = os.path.join(python_path, "admin.enc")

