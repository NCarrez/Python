import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


authorized_apps = [
    'master_manager',
    ''
]

authorized_functions = [
    'build_centralwidget',
    ''
]