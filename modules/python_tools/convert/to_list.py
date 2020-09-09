def to_list(list_to_convert):
    """
    Function Descrition :
    If not a list, convert to list
    
    Function Arguments : 
    list_to_convert : variable to return as a list
    
    Function Return : 
    list : list item
    """
    if not isinstance(list_to_convert, list):
        t_arg = list_to_convert
        list_to_convert = []
        list_to_convert.append(t_arg)
    return list_to_convert
