"""Handy tools for working with commandline parameters"""

def get_scriptfile_name(argv_or_full_name):
    if type(argv_or_full_name) is list:
        full_name = argv_or_full_name[0]
    else:
        full_name = argv_or_full_name
    return os.path.split(full_name)
