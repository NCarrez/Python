from python_tools.convert import to_list


def check_arg(args, args_to_search, must_return_value=False):
    """
    Function Descrition :
    Check if arg_to_check or if short_arg_to_check is in args
    
    Function Arguments : 
    args               : Arguments list
    args_to_search     : List of argument to search
    must_return_value  : Boolean, True if check_arg must return a value instead of a bool
    
    Function Return : 
    if must_return_value is False :
        bool : True if arg_to_check or short_arg_to_check in args, else False
    else:
        *    : Return a value or None 
    """
    args_to_search = to_list(args_to_search)

    for arg_to_check in args_to_search:
        if arg_to_check in args:
            index = args.index(arg_to_check)
            args.remove(arg_to_check)
            if not must_return_value:
                return True
            else:
                val = args[index]
                args.remove(val)
                return val
    if not must_return_value:
        return False
    else:
        return None
