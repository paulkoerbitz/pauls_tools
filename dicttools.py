"""Convenience tools for dictionaries"""

def walk_nested_dictionary(nested_dict, f, key_list=[], 
                           abort_cond = lambda x: type(x) is not dict):
    """Walks a nested dictionary by calling itself recursively until
    abort_cond(nested_dict[key]) is true then calls
    f(nested_dict[key],key_list + [key])."""
    for k in nested_dict.keys():
        if abort_cond(nested_dict[k]):
            f(nested_dict[k],key_list + [k])
        else:
            walk_nested_dictionary(nested_dict[k], f, key_list + [k],
                                   abort_cond)
