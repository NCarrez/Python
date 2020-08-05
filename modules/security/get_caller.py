import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)
    

def get_caller(level): #level 0 = self, level 1 = calling function, level 2 = calling calling function
    import inspect
    return inspect.stack()[level].function
